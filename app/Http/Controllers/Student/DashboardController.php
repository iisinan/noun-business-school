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
            $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->count();
                
            $hasRegisteredSemester = $sessionRegistrationsCount >= $activeSession->current_semester;
            
            if ($hasRegisteredSemester) {
                // Get already registered courses in this session
                $currentSessionCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $currentSessionCourseIds)->get();

                $passedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->whereNotNull('grade')
                    ->where('grade', '!=', 'F')
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSessionCourseIds, $passedCourseIds));

                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if ($studentSemester == 0) $studentSemester = 1;

                // Get courses for the student's enrolled programme
                $application = $user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                // Count registered electives (not failed)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('course_registrations.grade')
                          ->orWhere('course_registrations.grade', '!=', 'F');
                    })
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

                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) {
                        return $course->type === 'Elective';
                    })->values();
                }

                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

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
            $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->count();
                
            $hasRegisteredSemester = $sessionRegistrationsCount >= $activeSession->current_semester;
            
            if ($hasRegisteredSemester) {
                $currentSessionCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $currentSessionCourseIds)->get();

                $passedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->whereNotNull('grade')
                    ->where('grade', '!=', 'F')
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSessionCourseIds, $passedCourseIds));

                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if ($studentSemester == 0) $studentSemester = 1;

                $application = $user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                // Count registered electives (not failed)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('course_registrations.grade')
                          ->orWhere('course_registrations.grade', '!=', 'F');
                    })
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

                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) {
                        return $course->type === 'Elective';
                    })->values();
                }

                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });
            }
        }

        $transactions = WalletTransaction::where('user_id', $user->id)->latest()->take(10)->get();

        return Inertia::render('Student/Registration', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses ?? [],
            'studentSemester' => $studentSemester ?? 1,
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

        $nextSemester = SemesterRegistration::where('user_id', $user->id)->count() + 1;

        // Prevent registering for more semesters than the active session's current semester
        $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->count();
            
        if ($sessionRegistrationsCount >= $activeSession->current_semester) {
            return back()->with('error', 'You have already registered for the current active semester.');
        }

        // Deduct from wallet
        $user->wallet_balance -= $cost;
        $user->save();

        $reg = SemesterRegistration::create([
            'user_id' => $user->id,
            'academic_session_id' => $activeSession->id,
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

        // Ensure semester is registered for the current session's semester limit
        $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->count();
            
        if ($sessionRegistrationsCount < $activeSession->current_semester) {
            return back()->with('error', 'You must register for the semester first.');
        }

        $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
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
            ->where(function($q) {
                $q->whereNull('course_registrations.grade')
                  ->orWhere('course_registrations.grade', '!=', 'F');
            })
            ->where('courses.type', 'Elective')
            ->count();

        $newElectivesCount = $courses->where('type', 'Elective')->count();

        if (($alreadyRegisteredElectivesCount + $newElectivesCount) > 2) {
            return back()->with('error', 'You cannot register for more than 2 elective courses in total.');
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

        return Inertia::render('Student/Results', [
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits
        ]);
    }

    public function printSlip(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->firstOrFail();

        // Ensure semester is registered
        $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->count();
            
        if ($sessionRegistrationsCount < $activeSession->current_semester) {
            return redirect()->route('dashboard')->with('error', 'You must register for the semester first.');
        }

        $application = $user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();

        $studentSemester = SemesterRegistration::where('user_id', $user->id)->max('semester');

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
}
