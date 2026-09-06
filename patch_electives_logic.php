<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
                \$application = \$user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                \$availableCourses = collect();

                if (\$application) {
                    if (\$application->programme_id) {
PHP;

$replace = <<<PHP
                \$application = \$user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                // Count registered electives (not failed)
                \$registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', \$user->id)
                    ->where(function(\$q) {
                        \$q->whereNull('course_registrations.grade')
                          ->orWhere('course_registrations.grade', '!=', 'F');
                    })
                    ->where('courses.type', 'Elective')
                    ->count();

                \$availableCourses = collect();

                if (\$application) {
                    if (\$application->programme_id) {
PHP;

$content = str_replace($search, $replace, $content);

$search2 = <<<PHP
                    \$availableCourses = \$availableCourses->unique('id')->values();
                } else {
                    \$availableCourses = Course::whereNotIn('id', \$excludedCourseIds)
                        ->where('semester', '<=', \$studentSemester)
                        ->get();
                }
PHP;

$replace2 = <<<PHP
                    \$availableCourses = \$availableCourses->unique('id')->values();
                } else {
                    \$availableCourses = Course::whereNotIn('id', \$excludedCourseIds)
                        ->where('semester', '<=', \$studentSemester)
                        ->get();
                }

                if (\$registeredElectivesCount >= 2) {
                    \$availableCourses = \$availableCourses->reject(function(\$course) {
                        return \$course->type === 'Elective';
                    })->values();
                }
PHP;

$content = str_replace($search2, $replace2, $content);

file_put_contents($file, $content);
echo "Patched DashboardController!\n";
