file_path = '/Users/sinan/Herd/Business School/app/Models/CourseRegistration.php'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace(
    "protected $fillable = ['user_id', 'academic_session_id', 'semester', 'course_id', 'amount', 'status'];",
    "protected $fillable = ['user_id', 'academic_session_id', 'semester', 'course_id', 'amount', 'status', 'score', 'grade', 'grade_points'];"
)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched fillable attributes")
