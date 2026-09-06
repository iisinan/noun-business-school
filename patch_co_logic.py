file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) {
                        return $course->type === 'Elective';
                    })->values();
                }

                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();"""

replace = """                // Identify Carry Over (CO) courses
                $failedCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('grade', 'F')
                    ->pluck('course_id')
                    ->toArray();

                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) use ($failedCourseIds) {
                        // Reject electives only if they are NOT carry overs
                        return $course->type === 'Elective' && !in_array($course->id, $failedCourseIds);
                    })->values();
                }

                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_co = in_array($course->id, $failedCourseIds);
                });"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched DashboardController CO logic")
