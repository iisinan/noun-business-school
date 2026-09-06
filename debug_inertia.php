<?php
$user = App\Models\User::find(4);
$activeSession = App\Models\AcademicSession::where('is_active', true)->first();

$sessionRegistrationsCount = App\Models\SemesterRegistration::where('user_id', $user->id)
    ->where('academic_session_id', $activeSession->id)
    ->count();
$hasRegisteredSemester = $sessionRegistrationsCount >= $activeSession->current_semester;

$studentSemester = App\Models\SemesterRegistration::where('user_id', $user->id)->count();
if (!$hasRegisteredSemester) {
    $studentSemester += 1;
}
if ($studentSemester == 0) $studentSemester = 1;

$currentSemesterCourseIds = App\Models\CourseRegistration::where('user_id', $user->id)
    ->where('academic_session_id', $activeSession->id)
    ->where('semester', $studentSemester)
    ->pluck('course_id')
    ->toArray();

$passedOrPendingCourseIds = App\Models\CourseRegistration::where('user_id', $user->id)
    ->where(function($q) {
        $q->whereNull('grade')
          ->orWhere('grade', '!=', 'F');
    })
    ->pluck('course_id')
    ->toArray();

$excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));

$application = $user->applications()->where('status', 'ENROLLED')->first();
$availableCourses = collect();

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
    $specCourses->each(function($course) {
        if ($course->pivot && $course->pivot->is_elective) {
            $course->type = 'Elective';
        }
    });
    $availableCourses = $availableCourses->concat($specCourses);
}

$availableCourses = $availableCourses->unique('id')->values();

$registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
    ->where('course_registrations.user_id', $user->id)
    ->where('courses.type', 'Elective')
    ->count();

$failedCourseIds = App\Models\CourseRegistration::where('user_id', $user->id)
    ->where('grade', 'F')
    ->pluck('course_id')
    ->toArray();

if ($registeredElectivesCount >= 2) {
    $availableCourses = $availableCourses->reject(function($course) use ($failedCourseIds) {
        return $course->type === 'Elective' && !in_array($course->id, $failedCourseIds);
    })->values();
}

$availableCourses->each(function($course) use ($failedCourseIds) {
    $course->is_carry_over = in_array($course->id, $failedCourseIds);
});

// Output exactly what Inertia would serialize!
echo collect($availableCourses)->toJson();
