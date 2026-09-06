file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace("course->is_co", "course->is_carry_over")

with open(file_path, 'w') as f:
    f.write(content)
print("Patched is_carry_over")
