with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = "    public function results(Request $request)"
replacement = """    public function downloadResults(Request $request)
    {
        $user = $request->user();

        // Get all academic sessions where the user has registered for courses
        $sessionIds = \\App\\Models\\CourseRegistration::where('user_id', $user->id)
            ->pluck('academic_session_id')
            ->unique();

        $sessions = \\App\\Models\\AcademicSession::whereIn('id', $sessionIds)
            ->orderBy('id', 'asc') // Usually transcripts are chronological
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

        $pdf = \\Barryvdh\\DomPDF\\Facade\\Pdf::loadView('student.results-pdf', [
            'user' => $user,
            'application' => $user->applications()->with(['programme', 'specialisation'])->latest()->first(),
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits
        ]);

        return $pdf->download('results-'.$user->matric_number.'.pdf');
    }

    public function results(Request $request)"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Patched DashboardController")
else:
    print("Target not found in DashboardController")
