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
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\IOFactory;
use PhpOffice\PhpSpreadsheet\Style\Fill;
use PhpOffice\PhpSpreadsheet\Style\Color;
use PhpOffice\PhpSpreadsheet\Style\Protection;
use Symfony\Component\HttpFoundation\StreamedResponse;

class ResultController extends Controller
{
    public function create()
    {
        return Inertia::render('Admin/Results/Upload', [
            'courses' => Course::orderBy('code')->get(),
            'sessions' => AcademicSession::orderBy('id', 'desc')->get(),
        ]);
    }

    public function downloadTemplate(Request $request)
    {
        $request->validate([
            'mode' => 'required|in:single,multiple',
            'course_id' => 'required_if:mode,single|nullable|exists:courses,id',
            'academic_session_id' => 'required|exists:academic_sessions,id',
            'semester' => 'required_if:mode,multiple|nullable|integer|min:1|max:6',
        ]);

        $session = AcademicSession::find($request->academic_session_id);
        
        $query = CourseRegistration::with(['user.applications' => function($q) {
                $q->latest();
            }, 'course'])
            ->where('academic_session_id', $request->academic_session_id)
            ->orderBy('user_id');
            
        if ($request->mode === 'single') {
            $query->where('course_id', $request->course_id);
            $course = Course::find($request->course_id);
            $fileName = "results_template_{$course->code}_{$session->name}.xlsx";
        } else {
            $query->where('semester', $request->semester);
            $fileName = "results_template_sem{$request->semester}_{$session->name}.xlsx";
        }
        
        $registrations = $query->get();

        $spreadsheet = new Spreadsheet();
        $sheet = $spreadsheet->getActiveSheet();
        $sheet->setTitle('Results Template');

        // Headers
        $sheet->setCellValue('A1', 'Student Name');
        $sheet->setCellValue('B1', 'Matric Number');
        $sheet->setCellValue('C1', 'Course Code');
        $sheet->setCellValue('D1', 'Course Title');
        $sheet->setCellValue('E1', 'Units');
        $sheet->setCellValue('F1', 'Score');

        // Style Headers
        $headerStyle = [
            'font' => ['bold' => true, 'color' => ['argb' => Color::COLOR_WHITE]],
            'fill' => ['fillType' => Fill::FILL_SOLID, 'startColor' => ['argb' => 'FF004d26']] // dark green
        ];
        $sheet->getStyle('A1:F1')->applyFromArray($headerStyle);

        // Populate Data
        $row = 2;
        foreach ($registrations as $reg) {
            $user = $reg->user;
            $app = $user->applications->first();
            $matric = $app ? "NBS/{$session->id}/" . str_pad($app->id, 4, '0', STR_PAD_LEFT) : 'N/A';
            
            $sheet->setCellValue('A' . $row, $user->first_name . ' ' . $user->last_name);
            $sheet->setCellValue('B' . $row, $matric);
            $sheet->setCellValue('C' . $row, $reg->course->code);
            $sheet->setCellValue('D' . $row, $reg->course->title);
            $sheet->setCellValue('E' . $row, $reg->course->units);
            
            // Format score column in yellow to indicate it's editable
            $sheet->getStyle('F' . $row)->getFill()->setFillType(Fill::FILL_SOLID)->getStartColor()->setARGB('FFFFFF99');
            
            // Unlock score column
            $sheet->getStyle('F' . $row)->getProtection()->setLocked(Protection::PROTECTION_UNPROTECTED);
            
            $row++;
        }

        // Auto-size columns
        foreach (range('A', 'F') as $col) {
            $sheet->getColumnDimension($col)->setAutoSize(true);
        }

        // Protect worksheet so only unlocked cells (Scores) can be edited
        $sheet->getProtection()->setPassword('NBS_Secure_123!');
        $sheet->getProtection()->setSheet(true);

        $writer = new Xlsx($spreadsheet);
        // $fileName is set above

        return new StreamedResponse(function () use ($writer) {
            $writer->save('php://output');
        }, 200, [
            'Content-Type' => 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'Content-Disposition' => 'attachment; filename="' . $fileName . '"',
        ]);
    }

    public function store(Request $request)
    {
        $request->validate([
            'upload_mode' => 'required|in:single,multiple',
            'course_id' => 'required_if:upload_mode,single|nullable|exists:courses,id',
            'academic_session_id' => 'required|exists:academic_sessions,id',
            'file' => 'required|file|mimes:csv,txt,xlsx,xls|max:10240',
        ]);

        $file = $request->file('file');
        $extension = $file->getClientOriginalExtension();
        
        $updatedCount = 0;
        $errors = [];

        DB::beginTransaction();
        try {
            if (in_array(strtolower($extension), ['xlsx', 'xls'])) {
                // Excel Processing
                $spreadsheet = IOFactory::load($file->path());
                $worksheet = $spreadsheet->getActiveSheet();
                
                $rowNum = 1;
                foreach ($worksheet->getRowIterator() as $rowObj) {
                    if ($rowNum === 1) { // Skip header
                        $rowNum++;
                        continue;
                    }
                    
                    $cellIterator = $rowObj->getCellIterator();
                    $cellIterator->setIterateOnlyExistingCells(false); 
                    $row = [];
                    foreach ($cellIterator as $cell) {
                        $row[] = $cell->getValue();
                    }
                    
                    // Column B (1) is Matric, C (2) is Course Code, F (5) is Score
                    $matricNumber = trim((string)($row[1] ?? ''));
                    $courseCode = trim((string)($row[2] ?? ''));
                    $scoreValue = trim((string)($row[5] ?? ''));
                    
                    if (empty($matricNumber) || $scoreValue === '') {
                        $rowNum++;
                        continue; // Skip blank score rows gracefully
                    }
                    
                    $score = floatval($scoreValue);
                    
                    // Parse Matric
                    $parts = explode('/', $matricNumber);
                    if (count($parts) !== 3 || $parts[0] !== 'NBS') {
                        $errors[] = "Row $rowNum: Invalid matric number format ($matricNumber)";
                        $rowNum++;
                        continue;
                    }
                    
                    $appId = (int) $parts[2];
                    $application = Application::find($appId);
                    
                    if (!$application || !$application->user_id) {
                        $errors[] = "Row $rowNum: Student not found for matric ($matricNumber)";
                        $rowNum++;
                        continue;
                    }
                    
                    $userId = $application->user_id;
                    $courseId = null;

                    if ($request->upload_mode === 'single') {
                        $courseId = $request->course_id;
                    } else {
                        $course = Course::where('code', $courseCode)->first();
                        if (!$course) {
                            $errors[] = "Row $rowNum: Course not found ($courseCode)";
                            $rowNum++;
                            continue;
                        }
                        $courseId = $course->id;
                    }

                    $registration = CourseRegistration::where('user_id', $userId)
                        ->where('academic_session_id', $request->academic_session_id)
                        ->where('course_id', $courseId)
                        ->first();

                    if (!$registration) {
                        $errors[] = "Row $rowNum: Student ($matricNumber) is not registered for the course in this session.";
                        $rowNum++;
                        continue;
                    }

                    // Calculate Grade
                    $grade = 'F';
                    $gradePoints = 0;
                    if ($score >= 70) { $grade = 'A'; $gradePoints = 5; } 
                    elseif ($score >= 60) { $grade = 'B'; $gradePoints = 4; } 
                    elseif ($score >= 50) { $grade = 'C'; $gradePoints = 3; } 
                    elseif ($score >= 45) { $grade = 'D'; $gradePoints = 2; } 
                    elseif ($score >= 40) { $grade = 'E'; $gradePoints = 1; }

                    $registration->update([
                        'score' => $score,
                        'grade' => $grade,
                        'grade_points' => $gradePoints,
                    ]);

                    $updatedCount++;
                    $rowNum++;
                }

            } else {
                // CSV Processing
                $handle = fopen($file->path(), 'r');
                $header = fgetcsv($handle);
                if (!$header) {
                    return back()->with('error', 'The uploaded CSV file is empty or invalid.');
                }

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

                $rowNum = 1;
                while (($row = fgetcsv($handle)) !== false) {
                    $rowNum++;
                    if (count($row) < 2) continue;

                    $matricNumber = trim($row[$matricIndex] ?? '');
                    $scoreValue = trim($row[$scoreIndex] ?? '');
                    
                    if (empty($matricNumber) || $scoreValue === '') continue;
                    
                    $score = floatval($scoreValue);
                    
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

                    $registration = CourseRegistration::where('user_id', $userId)
                        ->where('academic_session_id', $request->academic_session_id)
                        ->where('course_id', $courseId)
                        ->first();

                    if (!$registration) {
                        $errors[] = "Row $rowNum: Student ($matricNumber) is not registered for the course in this session.";
                        continue;
                    }

                    $grade = 'F';
                    $gradePoints = 0;
                    if ($score >= 70) { $grade = 'A'; $gradePoints = 5; } 
                    elseif ($score >= 60) { $grade = 'B'; $gradePoints = 4; } 
                    elseif ($score >= 50) { $grade = 'C'; $gradePoints = 3; } 
                    elseif ($score >= 45) { $grade = 'D'; $gradePoints = 2; } 
                    elseif ($score >= 40) { $grade = 'E'; $gradePoints = 1; }

                    $registration->update([
                        'score' => $score,
                        'grade' => $grade,
                        'grade_points' => $gradePoints,
                    ]);

                    $updatedCount++;
                }
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
