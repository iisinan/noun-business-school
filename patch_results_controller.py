with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = "    public function printSlip(Request $request)"
replacement = """    public function results(Request $request)
    {
        $user = $request->user();

        // Get all academic sessions where the user has registered for courses
        $sessionIds = \\App\\Models\\CourseRegistration::where('user_id', $user->id)
            ->pluck('academic_session_id')
            ->unique();

        $sessions = \\App\\Models\\AcademicSession::whereIn('id', $sessionIds)
            ->orderBy('start_date', 'desc')
            ->get();

        $resultsBySession = [];
        $cumulativeCredits = 0;
        $cumulativePoints = 0;

        foreach ($sessions as $session) {
            $registrations = \\App\\Models\\CourseRegistration::with('course')
                ->where('user_id', $user->id)
                ->where('academic_session_id', $session->id)
                ->get();

            $sessionCredits = 0;
            $sessionPoints = 0;
            $hasPendingGrades = false;

            foreach ($registrations as $reg) {
                if ($reg->grade === null) {
                    $hasPendingGrades = true;
                } else {
                    $sessionCredits += $reg->course->units;
                    $sessionPoints += ($reg->grade_points * $reg->course->units);
                }
            }

            $cumulativeCredits += $sessionCredits;
            $cumulativePoints += $sessionPoints;

            $gpa = $sessionCredits > 0 ? round($sessionPoints / $sessionCredits, 2) : 0.00;

            $resultsBySession[] = [
                'session' => $session,
                'registrations' => $registrations,
                'gpa' => $gpa,
                'session_credits' => $sessionCredits,
                'has_pending_grades' => $hasPendingGrades
            ];
        }

        $cgpa = $cumulativeCredits > 0 ? round($cumulativePoints / $cumulativeCredits, 2) : 0.00;

        return Inertia::render('Student/Results', [
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits
        ]);
    }

    public function printSlip(Request $request)"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
    f.write(content)
