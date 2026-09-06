with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = """        if (SemesterRegistration::where('user_id', $user->id)->where('academic_session_id', $activeSession->id)->where('semester', $nextSemester)->exists()) {
            return back()->with('error', 'You have already registered for this semester.');
        }"""

replacement = """        // Prevent registering for multiple semesters within the same active session
        if (SemesterRegistration::where('user_id', $user->id)->where('academic_session_id', $activeSession->id)->exists()) {
            return back()->with('error', 'You have already registered for the current active semester.');
        }"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Backend patched!")
else:
    print("Target not found in backend!")
