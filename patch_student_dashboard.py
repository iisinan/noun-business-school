import re

file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

# In registration()
search1 = """        if ($activeSession) {
            $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->exists();"""

replace1 = """        if ($activeSession) {
            $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->count();
                
            $hasRegisteredSemester = $sessionRegistrationsCount >= $activeSession->current_semester;"""

content = content.replace(search1, replace1)

# In registerSemester()
search2 = """        // Prevent registering for multiple semesters within the same active session
        if (SemesterRegistration::where('user_id', $user->id)->where('academic_session_id', $activeSession->id)->exists()) {
            return back()->with('error', 'You have already registered for the current active semester.');
        }"""

replace2 = """        // Prevent registering for more semesters than the active session's current semester
        $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->count();
            
        if ($sessionRegistrationsCount >= $activeSession->current_semester) {
            return back()->with('error', 'You have already registered for the current active semester.');
        }"""

content = content.replace(search2, replace2)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched DashboardController")
