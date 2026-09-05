<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

// 1. When registering a course, save the student's current semester
$search = <<<PHP
                \$reg = CourseRegistration::create([
                    'user_id' => \$user->id,
                    'academic_session_id' => \$activeSession->id,
                    'course_id' => \$course->id,
PHP;
$replace = <<<PHP
                \$reg = CourseRegistration::create([
                    'user_id' => \$user->id,
                    'academic_session_id' => \$activeSession->id,
                    'semester' => \$studentSemester,
                    'course_id' => \$course->id,
PHP;
$content = str_replace($search, $replace, $content);

// 2. When checking alreadyRegisteredCredits, check by the student's current semester
$search2 = <<<PHP
        \$alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', \$user->id)
            ->where('academic_session_id', \$activeSession->id)
            ->sum('courses.units');
PHP;
$replace2 = <<<PHP
        \$alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', \$user->id)
            ->where('academic_session_id', \$activeSession->id)
            ->where('course_registrations.semester', \$studentSemester)
            ->sum('courses.units');
PHP;
$content = str_replace($search2, $replace2, $content);

file_put_contents($file, $content);
echo "Patched DashboardController\n";
