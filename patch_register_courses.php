<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
        \$courses = Course::whereIn('id', \$request->course_ids)
            ->where('semester', '<=', \$studentSemester)
            ->whereNotIn('id', \$passedCourseIds)
            ->get();

        if (\$courses->count() !== count(\$request->course_ids)) {
            return back()->with('error', 'Some selected courses are invalid or already passed.');
        }

        \$alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', \$user->id)
            ->where('academic_session_id', \$activeSession->id)
            ->where('course_registrations.semester', \$studentSemester)
            ->sum('courses.units');
PHP;

$replace = <<<PHP
        \$courses = Course::whereIn('id', \$request->course_ids)
            ->where('semester', '<=', \$studentSemester)
            ->whereNotIn('id', \$passedCourseIds)
            ->get();

        if (\$courses->count() !== count(\$request->course_ids)) {
            return back()->with('error', 'Some selected courses are invalid or already passed.');
        }

        // Count how many electives they already have registered in total
        \$alreadyRegisteredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('course_registrations.user_id', \$user->id)
            ->where(function(\$q) {
                \$q->whereNull('course_registrations.grade')
                  ->orWhere('course_registrations.grade', '!=', 'F');
            })
            ->where('courses.type', 'Elective')
            ->count();

        \$newElectivesCount = \$courses->where('type', 'Elective')->count();

        if ((\$alreadyRegisteredElectivesCount + \$newElectivesCount) > 2) {
            return back()->with('error', 'You cannot register for more than 2 elective courses in total.');
        }

        \$alreadyRegisteredCredits = CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
            ->where('user_id', \$user->id)
            ->where('academic_session_id', \$activeSession->id)
            ->where('course_registrations.semester', \$studentSemester)
            ->sum('courses.units');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched registerCourses method!\n";
