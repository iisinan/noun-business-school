file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

bad_block = """                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });

                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });"""
                
good_block = """                $availableCourses->each(function($course) use ($failedCourseIds) {
                    $course->is_carry_over = in_array($course->id, $failedCourseIds);
                });"""

content = content.replace(bad_block, good_block)

with open(file_path, 'w') as f:
    f.write(content)
print("Fixed dupe")
