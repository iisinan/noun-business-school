file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """                $currentSessionCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->pluck('course_id')
                    ->toArray();

                $passedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->whereNotNull('grade')
                    ->where('grade', '!=', 'F')
                    ->pluck('course_id')
                    ->toArray();

                $excludedCourseIds = array_unique(array_merge($currentSessionCourseIds, $passedCourseIds));"""

replace = """                // Courses currently registered in the semester being viewed
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

                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched exclusions")
