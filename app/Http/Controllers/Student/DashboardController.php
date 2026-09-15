<?php

namespace App\Http\Controllers\Student;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Inertia\Inertia;
use App\Models\AcademicSession;
use App\Models\Course;
use App\Models\SemesterRegistration;
use App\Models\CourseRegistration;
use App\Models\WalletTransaction;

class DashboardController extends Controller
{
    public function index(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->first();

        // Check if student has registered for the current active semester
        $hasRegisteredSemester = false;
        $registeredCourses = [];
        $availableCourses = [];

        if ($activeSession) {
            $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->where('school_semester', $activeSession->current_semester)
                ->exists();
                
            if ($hasRegisteredSemester) {
                $studentSemester = $user->current_semester;
                if ($studentSemester == 0) {
                    $studentSemester = 1;
                }

                $currentSemesterCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->where('semester', $studentSemester)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $currentSemesterCourseIds)->get();

                $passedOrPendingCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('grade')
                          ->orWhere('grade', '!=', 'F');
                    })
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));

                // Get courses for the student's enrolled programme
                $application = $user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                // Count ALL registered electives (including failed ones, because they will be retaken as CO)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where('courses.type', 'Elective')
                    ->count();

                $availableCourses = collect();

                if ($application) {
                    if ($application->programme_id) {
                        $progCourses = $application->programme->courses()
                            ->whereNotIn('courses.id', $excludedCourseIds)
                            ->where('semester', '<=', $studentSemester)
                            ->get();
                        $availableCourses = $availableCourses->concat($progCourses);
                    }

                    if ($application->specialisation_id) {
                        $specCourses = $application->specialisation->courses()
                            ->whereNotIn('courses.id', $excludedCourseIds)
                            ->where('semester', '<=', $studentSemester)
                            ->get();
                        
                        // Map pivot is_elective to course type for UI
                        $specCourses->each(function($course) {
                            if ($course->pivot && $course->pivot->is_elective) {
                                $course->type = 'Elective';
                            }
                        });

                        $availableCourses = $availableCourses->concat($specCourses);
                    }

                    $availableCourses = $availableCourses->unique('id')->values();
                } else {
                    $availableCourses = Course::whereNotIn('id', $excludedCourseIds)
                        ->where('semester', '<=', $studentSemester)
                        ->get();
                }

                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) use ($failedCourseIds) {
                        // Reject electives only if they are NOT carry overs
                        return $course->type === 'Elective' && !in_array($course->id, $failedCourseIds);
                    })->values();
                }

                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });
            }
        }

        // Fetch wallet transactions
        $transactions = WalletTransaction::where('user_id', $user->id)->latest()->take(10)->get();

        $application = $user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();

        return Inertia::render('Student/Dashboard', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses,
            'application' => $application,
        ]);
    }

    public function payments(Request $request)
    {
        $user = $request->user();
        
        $walletTransactions = \App\Models\WalletTransaction::where('user_id', $user->id)
            ->latest()
            ->get();
            
        $gatewayPayments = \App\Models\Payment::where('user_id', $user->id)
            ->latest()
            ->get();

        return Inertia::render('Student/Payments', [
            'wallet_balance' => (float) $user->wallet_balance,
            'walletTransactions' => $walletTransactions,
            'gatewayPayments' => $gatewayPayments,
        ]);
    }

    public function registration(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->first();

        $hasRegisteredSemester = false;
        $registeredCourses = [];
        $availableCourses = [];

        if ($activeSession) {
            $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->where('school_semester', $activeSession->current_semester)
                ->exists();
                
            if ($hasRegisteredSemester) {
                $studentSemester = $user->current_semester;
                if ($studentSemester == 0) {
                    $studentSemester = 1;
                }

                $currentSemesterCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->where('semester', $studentSemester)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $currentSemesterCourseIds)->get();

                $passedOrPendingCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('grade')
                          ->orWhere('grade', '!=', 'F');
                    })
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));

                $application = $user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                // Count ALL registered electives (including failed ones, because they will be retaken as CO)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where('courses.type', 'Elective')
                    ->count();

                $availableCourses = collect();

                if ($application) {
                    if ($application->programme_id) {
                        $progCourses = $application->programme->courses()
                            ->whereNotIn('courses.id', $excludedCourseIds)
                            ->where('semester', '<=', $studentSemester)
                            ->get();
                        $availableCourses = $availableCourses->concat($progCourses);
                    }

                    if ($application->specialisation_id) {
                        $specCourses = $application->specialisation->courses()
                            ->whereNotIn('courses.id', $excludedCourseIds)
                            ->where('semester', '<=', $studentSemester)
                            ->get();
                        
                        // Map pivot is_elective to course type for UI
                        $specCourses->each(function($course) {
                            if ($course->pivot && $course->pivot->is_elective) {
                                $course->type = 'Elective';
                            }
                        });

                        $availableCourses = $availableCourses->concat($specCourses);
                    }

                    $availableCourses = $availableCourses->unique('id')->values();
                } else {
                    $availableCourses = Course::whereNotIn('id', $excludedCourseIds)
                        ->where('semester', '<=', $studentSemester)
                        ->get();
                }

                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) use ($failedCourseIds) {
                        // Reject electives only if they are NOT carry overs
                        return $course->type === 'Elective' && !in_array($course->id, $failedCourseIds);
                    })->values();
                }

                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });
            }
        }

        $transactions = WalletTransaction::where('user_id', $user->id)->latest()->take(10)->get();

        $completedSemesters = [];
        for ($i = 1; $i < $user->current_semester; $i++) {
            $hasSummer = SemesterRegistration::where('user_id', $user->id)
                ->where('semester', $i)
                ->where('is_summer', true)
                ->exists();
                
            $summerCourses = [];
            if ($hasSummer) {
                $summerCourses = CourseRegistration::with('course')
                    ->where('user_id', $user->id)
                    ->where('semester', $i)
                    ->where('is_summer', true)
                    ->get();
            }

            $completedSemesters[] = [
                'semester' => $i,
                'summer_activated' => $hasSummer,
                'registered_courses' => $summerCourses
            ];
        }

        return Inertia::render('Student/Registration', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses ?? [],
            'studentSemester' => $studentSemester ?? 1,
            'completedSemesters' => $completedSemesters,
        ]);
    }

    public function registerSemester(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();

        $cost = 35000.00;

        if ($user->wallet_balance < $cost) {
            return back()->with('error', 'Insufficient wallet balance. Please top up your wallet.');
        }

        $nextSemester = $user->current_semester;
        if ($nextSemester == 0) {
            $nextSemester = 1;
        }

        // Prevent registering if they already paid for the school's current semester
        $alreadyRegistered = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->where('school_semester', $activeSession->current_semester)
            ->exists();
            
        if ($alreadyRegistered) {
            return back()->with('error', 'You have already registered for the current active semester.');
        }

        // Deduct from wallet
        $user->wallet_balance -= $cost;
        $user->save();

        $reg = SemesterRegistration::create([
            'user_id' => $user->id,
            'academic_session_id' => $activeSession->id,
            'school_semester' => $activeSession->current_semester,
            'semester' => $nextSemester,
            'amount' => $cost,
            'status' => 'paid',
        ]);

        WalletTransaction::create([
            'user_id' => $user->id,
            'type' => 'semester_registration',
            'amount' => -$cost,
            'description' => 'Semester Registration Fee',
            'reference_id' => $reg->id,
        ]);

        return back()->with('success', 'Semester registration successful.');
    }

    public function registerCourses(Request $request)
    {
        $request->validate([
            'course_ids' => 'required|array',
            'course_ids.*' => 'exists:courses,id',
        ]);

        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();

        // Ensure semester is registered for the current session's school semester
        $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->where('school_semester', $activeSession->current_semester)
            ->exists();
            
        if (!$hasRegisteredSemester) {
            return back()->with('error', 'You must register for the semester first.');
        }

        $studentSemester = $user->current_semester;
        if ($studentSemester == 0) $studentSemester = 1;

        $passedCourseIds = CourseRegistration::where('user_id', $user->id)
            ->whereNotNull('grade')
            ->where('grade', '!=', 'F')
            ->pluck('course_id')
            ->toArray();

        $courses = Course::whereIn('id', $request->course_ids)
            ->where('semester', '<=', $studentSemester)
            ->whereNotIn('id', $passedCourseIds)
            ->get();

        if ($courses->count() !== count($request->course_ids)) {
            return back()->with('error', 'Some selected courses are invalid or already passed.');
        }

        // Count how many electives they already have registered in total
        $alreadyRegisteredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('course_registrations.user_id', $user->id)
            ->where('courses.type', 'Elective')
            ->count();

        $failedCourseIds = CourseRegistration::where('user_id', $user->id)
            ->where('grade', 'F')
            ->pluck('course_id')
            ->toArray();

        $newElectivesCount = $courses->where('type', 'Elective')->whereNotIn('id', $failedCourseIds)->count();

        if (($alreadyRegisteredElectivesCount + $newElectivesCount) > 2) {
            return back()->with('error', 'You cannot register for more than 2 new elective courses in total.');
        }

        $alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->where('course_registrations.semester', $studentSemester)
            ->sum('courses.units');

        $newCredits = $courses->sum('units');

        if (($alreadyRegisteredCredits + $newCredits) > 24) {
            return back()->with('error', 'You cannot exceed the maximum of 24 credit units per semester.');
        }

        $totalCost = 0;
        foreach ($courses as $course) {
            if ($course->units == 2) {
                $totalCost += 2500;
            } elseif ($course->units == 3) {
                $totalCost += 3500;
            } else {
                // Fallback for other units
                $totalCost += ($course->units * 1000); 
            }
        }

        if ($user->wallet_balance < $totalCost) {
            return back()->with('error', 'Insufficient wallet balance. Please top up your wallet. Cost is NGN ' . number_format($totalCost, 2));
        }

        foreach ($courses as $course) {
            // Check if already registered
            $exists = CourseRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->where('course_id', $course->id)
                ->exists();

            if (!$exists) {
                $cost = ($course->units == 2) ? 2500 : (($course->units == 3) ? 3500 : ($course->units * 1000));
                
                $user->wallet_balance -= $cost;
                $user->save();

                $reg = CourseRegistration::create([
                    'user_id' => $user->id,
                    'academic_session_id' => $activeSession->id,
                    'semester' => $studentSemester,
                    'course_id' => $course->id,
                    'amount' => $cost,
                    'status' => 'paid',
                ]);

                WalletTransaction::create([
                    'user_id' => $user->id,
                    'type' => 'course_registration',
                    'amount' => -$cost,
                    'description' => 'Course Registration: ' . $course->code,
                    'reference_id' => $reg->id,
                ]);
            }
        }

        return back()->with('success', 'Courses registered successfully.');
    }

    public function statement(Request $request)
    {
        $user = $request->user();

        $walletTransactions = \App\Models\WalletTransaction::where('user_id', $user->id)
            ->oldest() // chronological order for a statement
            ->get();
            
        $application = $user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();

        return Inertia::render('Student/Statement', [
            'user' => $user,
            'application' => $application,
            'walletTransactions' => $walletTransactions,
            'wallet_balance' => (float) $user->wallet_balance,
        ]);
    }

    public function downloadResults(Request $request)
    {
        $user = $request->user();

        // Get all academic sessions where the user has registered for courses
        $sessionIds = \App\Models\CourseRegistration::where('user_id', $user->id)
            ->pluck('academic_session_id')
            ->unique();

        $sessions = \App\Models\AcademicSession::whereIn('id', $sessionIds)
            ->orderBy('id', 'asc') // Usually transcripts are chronological
            ->get();

        $resultsBySession = [];
        $cumulativeCredits = 0;
        $cumulativePoints = 0;

        foreach ($sessions as $session) {
            $registrations = \App\Models\CourseRegistration::with('course')
                ->where('user_id', $user->id)
                ->where('academic_session_id', $session->id)
                ->get();

            $sessionCredits = 0;
            $sessionPoints = 0;
            $hasPendingGrades = false;

            foreach ($registrations as $reg) {
                if ($reg->grade === null) {
                    $hasPendingGrades = true;
                } else {
                    $sessionCredits += $reg->course->units;
                    $sessionPoints += ($reg->grade_points * $reg->course->units);
                }
            }

            $cumulativeCredits += $sessionCredits;
            $cumulativePoints += $sessionPoints;

            $gpa = $sessionCredits > 0 ? round($sessionPoints / $sessionCredits, 2) : 0.00;

            $resultsBySession[] = [
                'session' => $session,
                'registrations' => $registrations,
                'gpa' => $gpa,
                'session_credits' => $sessionCredits,
                'has_pending_grades' => $hasPendingGrades
            ];
        }

        $cgpa = $cumulativeCredits > 0 ? round($cumulativePoints / $cumulativeCredits, 2) : 0.00;

        $application = $user->applications()->with(['programme', 'specialisation'])->latest()->first();

        // Get logo base64
        $logoPath = public_path('nbs-logo.png');
        $logoBase64 = '';
        if (file_exists($logoPath)) {
            $logoData = file_get_contents($logoPath);
            $logoBase64 = 'data:image/png;base64,' . base64_encode($logoData);
        }

        // Get passport base64
        $passportBase64 = '';
        if ($application && isset($application->personal_info['passport_photograph_path'])) {
            $passportPath = storage_path('app/public/' . $application->personal_info['passport_photograph_path']);
            if (file_exists($passportPath)) {
                $passportData = file_get_contents($passportPath);
                $type = pathinfo($passportPath, PATHINFO_EXTENSION);
                $passportBase64 = 'data:image/' . $type . ';base64,' . base64_encode($passportData);
            }
        }

        $pdf = \Barryvdh\DomPDF\Facade\Pdf::loadView('student.results-pdf', [
            'user' => $user,
            'application' => $application,
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits,
            'logoBase64' => $logoBase64,
            'passportBase64' => $passportBase64
        ]);

        $safeAppNumber = str_replace(['/', '\\'], '-', $application->application_number);
        return $pdf->stream('results-'.$safeAppNumber.'.pdf');
    }

    public function results(Request $request)
    {
        $user = $request->user();

        // Get all academic sessions where the user has registered for courses
        $sessionIds = \App\Models\CourseRegistration::where('user_id', $user->id)
            ->pluck('academic_session_id')
            ->unique();

        $sessions = \App\Models\AcademicSession::whereIn('id', $sessionIds)
            ->orderBy('id', 'desc')
            ->get();

        $resultsBySession = [];
        $cumulativeCredits = 0;
        $cumulativePoints = 0;

        foreach ($sessions as $session) {
            $registrations = \App\Models\CourseRegistration::with('course')
                ->where('user_id', $user->id)
                ->where('academic_session_id', $session->id)
                ->get();

            $sessionCredits = 0;
            $sessionPoints = 0;
            $hasPendingGrades = false;

            foreach ($registrations as $reg) {
                if ($reg->grade === null) {
                    $hasPendingGrades = true;
                } else {
                    $sessionCredits += $reg->course->units;
                    $sessionPoints += ($reg->grade_points * $reg->course->units);
                }
            }

            $cumulativeCredits += $sessionCredits;
            $cumulativePoints += $sessionPoints;

            $gpa = $sessionCredits > 0 ? round($sessionPoints / $sessionCredits, 2) : 0.00;

            $resultsBySession[] = [
                'session' => $session,
                'registrations' => $registrations,
                'gpa' => $gpa,
                'session_credits' => $sessionCredits,
                'has_pending_grades' => $hasPendingGrades
            ];
        }

        $cgpa = $cumulativeCredits > 0 ? round($cumulativePoints / $cumulativeCredits, 2) : 0.00;
        
        // Check if student has at least one actual grade uploaded
        $hasAnyGrades = \App\Models\CourseRegistration::where('user_id', $user->id)
            ->whereNotNull('grade')
            ->exists();

        return Inertia::render('Student/Results', [
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits,
            'hasAnyGrades' => $hasAnyGrades
        ]);
    }

    public function printSlip(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();

        // Ensure semester is registered
        $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->where('school_semester', $activeSession->current_semester)
            ->exists();
            
        if (!$hasRegisteredSemester) {
            return redirect()->route('dashboard')->with('error', 'You must register for the semester first.');
        }

        $application = $user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();

        $studentSemester = $user->current_semester;

        $registeredCourses = CourseRegistration::with('course')
            ->where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->where('semester', $studentSemester)
            ->get();

        if ($registeredCourses->isEmpty()) {
            return redirect()->route('dashboard')->with('error', "No registered courses found for Semester $studentSemester in the active session.");
        }

        return Inertia::render('Student/Slip', [
            'user' => $user,
            'application' => $application,
            'session' => $activeSession,
            'studentSemester' => $studentSemester,
            'registeredCourses' => $registeredCourses,
        ]);
    }

    public function idCard(Request $request)
    {
        $user = $request->user();
        $application = $user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();

        if (!$application) {
            return redirect()->route('dashboard')->with('error', 'No active enrollment found to generate ID card.');
        }

        return Inertia::render('Student/IdCard', [
            'user' => $user,
            'application' => $application,
        ]);
    }

    public function activateSummer(Request $request)
    {
        $request->validate(['semester' => 'required|integer|min:1']);
        $user = $request->user();
        $semester = $request->semester;

        if ($semester >= $user->current_semester) {
            return back()->with('error', 'You can only activate summer for completed semesters.');
        }

        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();
        $cost = 15000.00;

        if ($user->wallet_balance < $cost) {
            return back()->with('error', 'Insufficient wallet balance for Summer Registration (N15,000).');
        }

        $alreadyActivated = SemesterRegistration::where('user_id', $user->id)
            ->where('semester', $semester)
            ->where('is_summer', true)
            ->exists();

        if ($alreadyActivated) {
            return back()->with('error', 'Summer is already activated for Semester ' . $semester);
        }

        $user->wallet_balance -= $cost;
        $user->save();

        SemesterRegistration::create([
            'user_id' => $user->id,
            'academic_session_id' => $activeSession->id,
            'school_semester' => $activeSession->current_semester,
            'semester' => $semester,
            'amount' => $cost,
            'type' => 'semester_registration',
            'description' => 'Summer Registration Fee for Sem ' . $semester,
            'is_summer' => true,
        ]);

        WalletTransaction::create([
            'user_id' => $user->id,
            'amount' => $cost,
            'type' => 'semester_registration',
            'description' => 'Summer Registration for Sem ' . $semester,
            'reference_id' => 'SUMMER_REG_' . $user->id . '_' . time(),
            'is_credit' => false,
        ]);

        return back()->with('success', 'Summer session activated successfully for Semester ' . $semester . '!');
    }

    public function registerSummerCourses(Request $request)
    {
        $request->validate([
            'semester' => 'required|integer',
            'course_ids' => 'required|array|min:1',
            'course_ids.*' => 'exists:courses,id'
        ]);

        $user = $request->user();
        $semester = $request->semester;
        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();

        $hasSummer = SemesterRegistration::where('user_id', $user->id)
            ->where('semester', $semester)
            ->where('is_summer', true)
            ->exists();

        if (!$hasSummer) {
            return back()->with('error', 'You must activate Summer for Semester ' . $semester . ' first.');
        }

        $passedCourseIds = CourseRegistration::where('user_id', $user->id)
            ->whereNotNull('grade')
            ->where('grade', '!=', 'F')
            ->pluck('course_id')
            ->toArray();

        $courses = Course::whereIn('id', $request->course_ids)
            ->whereNotIn('id', $passedCourseIds)
            ->get();

        if ($courses->isEmpty()) {
            return back()->with('error', 'All selected courses are either already passed or invalid.');
        }

        $totalCost = 0;
        foreach ($courses as $c) {
            $totalCost += ($c->units == 2) ? 2500 : (($c->units == 3) ? 3500 : ($c->units * 1000));
        }

        if ($user->wallet_balance < $totalCost) {
            return back()->with('error', 'Insufficient wallet balance for selected courses.');
        }

        $registeredCount = 0;
        foreach ($courses as $course) {
            $exists = CourseRegistration::where('user_id', $user->id)
                ->where('semester', $semester)
                ->where('is_summer', true)
                ->where('course_id', $course->id)
                ->exists();

            if (!$exists) {
                $cost = ($course->units == 2) ? 2500 : (($course->units == 3) ? 3500 : ($course->units * 1000));
                
                $user->wallet_balance -= $cost;
                $user->save();

                CourseRegistration::create([
                    'user_id' => $user->id,
                    'academic_session_id' => $activeSession->id,
                    'semester' => $semester,
                    'course_id' => $course->id,
                    'amount' => $cost,
                    'type' => 'course_registration',
                    'description' => 'Summer Course: ' . $course->code,
                    'is_summer' => true,
                ]);

                WalletTransaction::create([
                    'user_id' => $user->id,
                    'amount' => $cost,
                    'type' => 'course_registration',
                    'description' => 'Summer Registration for ' . $course->code,
                    'reference_id' => 'SUMMER_CRS_' . $user->id . '_' . $course->id . '_' . time(),
                    'is_credit' => false,
                ]);

                $registeredCount++;
            }
        }

        return back()->with('success', "Successfully registered $registeredCount courses for Summer $semester.");
    }
}
