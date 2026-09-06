import re

file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if ($studentSemester == 0) $studentSemester = 1;"""

replace = """                $studentSemester = SemesterRegistration::where('user_id', $user->id)->count();
                if (!$hasRegisteredSemester) {
                    $studentSemester += 1;
                }
                if ($studentSemester == 0) $studentSemester = 1;"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched studentSemester display logic")
