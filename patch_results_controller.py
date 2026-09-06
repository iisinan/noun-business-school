with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = """        $cgpa = $cumulativeCredits > 0 ? round($cumulativePoints / $cumulativeCredits, 2) : 0.00;

        return Inertia::render('Student/Results', [
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits
        ]);"""

replacement = """        $cgpa = $cumulativeCredits > 0 ? round($cumulativePoints / $cumulativeCredits, 2) : 0.00;
        
        // Check if student has at least one actual grade uploaded
        $hasAnyGrades = \\App\\Models\\CourseRegistration::where('user_id', $user->id)
            ->whereNotNull('grade')
            ->exists();

        return Inertia::render('Student/Results', [
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits,
            'hasAnyGrades' => $hasAnyGrades
        ]);"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Patched DashboardController")
else:
    print("Target not found in DashboardController")
