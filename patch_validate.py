import re

file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        $newElectivesCount = $courses->where('type', 'Elective')->count();

        if (($alreadyRegisteredElectivesCount + $newElectivesCount) > 2) {
            return back()->with('error', 'You cannot register for more than 2 elective courses in total.');
        }"""

replace = """        $failedCourseIds = CourseRegistration::where('user_id', $user->id)
            ->where('grade', 'F')
            ->pluck('course_id')
            ->toArray();

        $newElectivesCount = $courses->where('type', 'Elective')->whereNotIn('id', $failedCourseIds)->count();

        if (($alreadyRegisteredElectivesCount + $newElectivesCount) > 2) {
            return back()->with('error', 'You cannot register for more than 2 new elective courses in total.');
        }"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched validation logic")
