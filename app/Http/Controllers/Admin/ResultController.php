<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Inertia\Inertia;
use App\Models\Course;
use App\Models\AcademicSession;
use App\Models\CourseRegistration;
use App\Models\Application;
use Illuminate\Support\Facades\DB;

class ResultController extends Controller
{
    public function create()
    {
        return Inertia::render('Admin/Results/Upload', [
            'courses' => Course::orderBy('code')->get(),
            'sessions' => AcademicSession::orderBy('id', 'desc')->get(),
        ]);
    }

    public function store(Request $request)
    {
        $request->validate([
            'upload_mode' => 'required|in:single,multiple',
            'course_id' => 'required_if:upload_mode,single|nullable|exists:courses,id',
            'academic_session_id' => 'required|exists:academic_sessions,id',
            'file' => 'required|file|mimes:csv,txt|max:5120',
        ]);

        $file = $request->file('file');
        $handle = fopen($file->path(), 'r');
        $header = fgetcsv($handle); // skip header or process it

        if (!$header) {
            return back()->with('error', 'The uploaded CSV file is empty or invalid.');
        }

        // Normalize header
        $header = array_map('strtolower', array_map('trim', $header));
        
        $matricIndex = array_search('matric number', $header) !== false ? array_search('matric number', $header) : 0;
        $scoreIndex = array_search('score', $header) !== false ? array_search('score', $header) : (count($header) - 1);
        
        $courseCodeIndex = false;
        if ($request->upload_mode === 'multiple') {
            $courseCodeIndex = array_search('course code', $header);
            if ($courseCodeIndex === false) {
                return back()->with('error', 'For multiple courses mode, the CSV must have a "Course Code" column.');
            }
        }

        $updatedCount = 0;
        $errors = [];
        $rowNum = 1;

        DB::beginTransaction();
        try {
            while (($row = fgetcsv($handle)) !== false) {
                $rowNum++;
                
                if (count($row) < 2) continue; // skip empty rows

                $matricNumber = trim($row[$matricIndex] ?? '');
                $score = floatval(trim($row[$scoreIndex] ?? '0'));
                
                // Parse Matric Number NBS/{session_id}/{app_id}
                $parts = explode('/', $matricNumber);
                if (count($parts) !== 3 || $parts[0] !== 'NBS') {
                    $errors[] = "Row $rowNum: Invalid matric number format ($matricNumber)";
                    continue;
                }
                
                $appId = (int) $parts[2];
                $application = Application::find($appId);
                
                if (!$application || !$application->user_id) {
                    $errors[] = "Row $rowNum: Student not found for matric ($matricNumber)";
                    continue;
                }
                
                $userId = $application->user_id;

                $courseId = null;
                if ($request->upload_mode === 'single') {
                    $courseId = $request->course_id;
                } else {
                    $courseCode = trim($row[$courseCodeIndex] ?? '');
                    $course = Course::where('code', $courseCode)->first();
                    if (!$course) {
                        $errors[] = "Row $rowNum: Course not found ($courseCode)";
                        continue;
                    }
                    $courseId = $course->id;
                }

                // Check if they registered for this course
                $registration = CourseRegistration::where('user_id', $userId)
                    ->where('academic_session_id', $request->academic_session_id)
                    ->where('course_id', $courseId)
                    ->first();

                if (!$registration) {
                    $errors[] = "Row $rowNum: Student ($matricNumber) is not registered for the course in this session.";
                    continue;
                }

                // Calculate Grade
                $grade = 'F';
                $gradePoints = 0;
                
                if ($score >= 70) {
                    $grade = 'A'; $gradePoints = 5;
                } elseif ($score >= 60) {
                    $grade = 'B'; $gradePoints = 4;
                } elseif ($score >= 50) {
                    $grade = 'C'; $gradePoints = 3;
                } elseif ($score >= 45) {
                    $grade = 'D'; $gradePoints = 2;
                } elseif ($score >= 40) {
                    $grade = 'E'; $gradePoints = 1;
                }

                $registration->update([
                    'score' => $score,
                    'grade' => $grade,
                    'grade_points' => $gradePoints,
                ]);

                $updatedCount++;
            }

            if (empty($errors)) {
                DB::commit();
                return back()->with('success', "Successfully uploaded results for $updatedCount student records.");
            } else {
                DB::rollBack();
                return back()->with('error', "Upload failed. Please fix the following errors:\n" . implode("\n", array_slice($errors, 0, 5)) . (count($errors) > 5 ? "\n...and " . (count($errors) - 5) . " more." : ""));
            }
        } catch (\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'An error occurred processing the file: ' . $e->getMessage());
        }
    }
}
