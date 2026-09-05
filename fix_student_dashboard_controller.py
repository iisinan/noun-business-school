import re

with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = """        return Inertia::render('Student/Dashboard', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses,
        ]);"""

replacement = """        $application = $user->applications()->with('programme')->where('status', 'ENROLLED')->latest()->first();

        return Inertia::render('Student/Dashboard', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses,
            'application' => $application,
        ]);"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
    f.write(content)

