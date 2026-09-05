<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<'PHP'
        $courses = Course::whereIn('id', $request->course_ids)->get();
        
        $totalCost = 0;
PHP;

$replace = <<<'PHP'
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

        $alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->sum('courses.units');

        $newCredits = $courses->sum('units');

        if (($alreadyRegisteredCredits + $newCredits) > 24) {
            return back()->with('error', 'You cannot exceed the maximum of 24 credit units per semester.');
        }

        $totalCost = 0;
PHP;

if (strpos($content, $search) !== false) {
    file_put_contents($file, str_replace($search, $replace, $content));
    echo "Patched successfully\n";
} else {
    echo "Search string not found\n";
}
