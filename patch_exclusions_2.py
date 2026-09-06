file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """                // Courses currently registered in the semester being viewed
                $currentSemesterCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->where('semester', SemesterRegistration::where('user_id', $user->id)->count())
                    ->pluck('course_id')
                    ->toArray();

                // Courses that are passed OR pending (grade is null)
                $passedOrPendingCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('grade')
                          ->orWhere('grade', '!=', 'F');
                    })
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));

                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if (!$hasRegisteredSemester) {
                    $studentSemester += 1;
                }
                if ($studentSemester == 0) $studentSemester = 1;"""

replace = """                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if (!$hasRegisteredSemester) {
                    $studentSemester += 1;
                }
                if ($studentSemester == 0) $studentSemester = 1;

                // Courses currently registered in the semester being viewed
                $currentSemesterCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->where('semester', $studentSemester)
                    ->pluck('course_id')
                    ->toArray();

                // Courses that are passed OR pending (grade is null)
                $passedOrPendingCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('grade')
                          ->orWhere('grade', '!=', 'F');
                    })
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched exclusions 2")
