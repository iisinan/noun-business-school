file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

import re

search_pattern = r"""            if \(\$hasRegisteredSemester\) \{.*?\$excludedCourseIds = array_unique\(array_merge\(\$currentSessionCourseIds, \$passedCourseIds\)\);.*?\$studentSemester = SemesterRegistration::where\('user_id', \$user->id\)->count\(\);"""

replace_string = """            if ($hasRegisteredSemester) {
                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if (!$hasRegisteredSemester) {
                    $studentSemester += 1;
                }
                if ($studentSemester == 0) $studentSemester = 1;

                $currentSemesterCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->where('semester', $studentSemester)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $currentSemesterCourseIds)->get();

                $passedOrPendingCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('grade')
                          ->orWhere('grade', '!=', 'F');
                    })
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));"""

content = re.sub(search_pattern, replace_string, content, flags=re.DOTALL)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched registration logic")
