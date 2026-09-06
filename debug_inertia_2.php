<?php
$user = App\Models\User::find(4);
$activeSession = App\Models\AcademicSession::where('is_active', true)->first();

$studentSemester = App\Models\SemesterRegistration::where('user_id', $user->id)->count() + 1; // force semester 2 logic

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

$progCourses = $application->programme->courses()
    ->whereNotIn('courses.id', $excludedCourseIds)
    ->where('semester', '<=', $studentSemester)
    ->get();
$availableCourses = $availableCourses->concat($progCourses);

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
$availableCourses = $availableCourses->unique('id')->values();

$failedCourseIds = App\Models\CourseRegistration::where('user_id', $user->id)
    ->where('grade', 'F')
    ->pluck('course_id')
    ->toArray();

$availableCourses->each(function($course) use ($failedCourseIds) {
    $course->is_carry_over = in_array($course->id, $failedCourseIds);
});

foreach($availableCourses as $c) {
    echo $c->code . " - CO: " . ($c->is_carry_over ? 'true' : 'false') . "\n";
}
