<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
                \$application = \$user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();
                if (\$application && \$application->programme_id) {
                    \$availableCourses = \$application->programme->courses()
                        ->whereNotIn('courses.id', \$excludedCourseIds)
                        ->where('semester', '<=', \$studentSemester)
                        ->get();
                } else {
                    \$availableCourses = Course::whereNotIn('id', \$excludedCourseIds)
                        ->where('semester', '<=', \$studentSemester)
                        ->get();
                }
PHP;

$replace = <<<PHP
                \$application = \$user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();
                
                \$availableCourses = collect();

                if (\$application) {
                    if (\$application->programme_id) {
                        \$progCourses = \$application->programme->courses()
                            ->whereNotIn('courses.id', \$excludedCourseIds)
                            ->where('semester', '<=', \$studentSemester)
                            ->get();
                        \$availableCourses = \$availableCourses->concat(\$progCourses);
                    }

                    if (\$application->specialisation_id) {
                        \$specCourses = \$application->specialisation->courses()
                            ->whereNotIn('courses.id', \$excludedCourseIds)
                            ->where('semester', '<=', \$studentSemester)
                            ->get();
                        \$availableCourses = \$availableCourses->concat(\$specCourses);
                    }

                    \$availableCourses = \$availableCourses->unique('id')->values();
                } else {
                    \$availableCourses = Course::whereNotIn('id', \$excludedCourseIds)
                        ->where('semester', '<=', \$studentSemester)
                        ->get();
                }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched DashboardController!\n";
