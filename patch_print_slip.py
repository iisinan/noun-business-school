import re

file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        // Ensure semester is registered
        if (!SemesterRegistration::where('user_id', $user->id)->where('academic_session_id', $activeSession->id)->exists()) {
            return redirect()->route('dashboard')->with('error', 'You must register for the semester first.');
        }"""

replace = """        // Ensure semester is registered
        $sessionRegistrationsCount = SemesterRegistration::where('user_id', $user->id)
            ->where('academic_session_id', $activeSession->id)
            ->count();
            
        if ($sessionRegistrationsCount < $activeSession->current_semester) {
            return redirect()->route('dashboard')->with('error', 'You must register for the semester first.');
        }"""

content = content.replace(search, replace)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched printSlip")
