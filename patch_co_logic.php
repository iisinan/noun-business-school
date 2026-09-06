<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
                if (\$registeredElectivesCount >= 2) {
                    \$availableCourses = \$availableCourses->reject(function(\$course) {
                        return \$course->type === 'Elective';
                    })->values();
                }
PHP;

$replace = <<<PHP
                if (\$registeredElectivesCount >= 2) {
                    \$availableCourses = \$availableCourses->reject(function(\$course) {
                        return \$course->type === 'Elective';
                    })->values();
                }

                // Identify Carry Over (CO) courses
                \$failedCourseIds = CourseRegistration::where('user_id', \$user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

                \$availableCourses->each(function(\$course) use (\$failedCourseIds) {
                    \$course->is_carry_over = in_array(\$course->id, \$failedCourseIds);
                });
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched DashboardController for CO!\n";
