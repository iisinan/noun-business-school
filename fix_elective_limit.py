with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = """                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) {
                        return $course->type === 'Elective';
                    })->values();
                }"""

replacement = """                if ($registeredElectivesCount >= 2) {
                    $availableCourses = $availableCourses->reject(function($course) {
                        return $course->type === 'Elective' || (isset($course->pivot) && $course->pivot->is_elective);
                    })->values();
                }"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Fixed elective limit")
else:
    print("Target not found")
