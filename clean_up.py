file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

import re

search_pattern = r"""                \$excludedCourseIds = array_unique\(array_merge\(\$currentSemesterCourseIds, \$passedOrPendingCourseIds\)\);\s*if \(!\$hasRegisteredSemester\) \{\s*\$studentSemester \+= 1;\s*\}\s*if \(\$studentSemester == 0\) \$studentSemester = 1;"""

replace_string = """                $excludedCourseIds = array_unique(array_merge($currentSemesterCourseIds, $passedOrPendingCourseIds));"""

content = re.sub(search_pattern, replace_string, content)

with open(file_path, 'w') as f:
    f.write(content)
print("Cleaned up")
