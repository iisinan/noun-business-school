<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
                    if (\$application->specialisation_id) {
                        \$specCourses = \$application->specialisation->courses()
                            ->whereNotIn('courses.id', \$excludedCourseIds)
                            ->where('semester', '<=', \$studentSemester)
                            ->get();
                        \$availableCourses = \$availableCourses->concat(\$specCourses);
                    }
PHP;

$replace = <<<PHP
                    if (\$application->specialisation_id) {
                        \$specCourses = \$application->specialisation->courses()
                            ->whereNotIn('courses.id', \$excludedCourseIds)
                            ->where('semester', '<=', \$studentSemester)
                            ->get();
                        
                        // Map pivot is_elective to course type for UI
                        \$specCourses->each(function(\$course) {
                            if (\$course->pivot && \$course->pivot->is_elective) {
                                \$course->type = 'Elective';
                            }
                        });

                        \$availableCourses = \$availableCourses->concat(\$specCourses);
                    }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched DashboardController with pivot mapping!\n";
