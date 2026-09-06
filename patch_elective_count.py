file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """                // Count registered electives (not failed)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where(function($q) {
                        $q->whereNull('course_registrations.grade')
                          ->orWhere('course_registrations.grade', '!=', 'F');
                    })
                    ->where('courses.type', 'Elective')
                    ->count();"""

replace = """                // Count ALL registered electives (including failed ones, because they will be retaken as CO)
                $registeredElectivesCount = \App\Models\CourseRegistration::join('courses', 'course_registrations.course_id', '=', 'courses.id')
                    ->where('course_registrations.user_id', $user->id)
                    ->where('courses.type', 'Elective')
                    ->count();"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched elective count")
