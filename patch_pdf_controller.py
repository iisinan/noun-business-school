with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = """        $pdf = \\Barryvdh\\DomPDF\\Facade\\Pdf::loadView('student.results-pdf', [
            'user' => $user,
            'application' => $user->applications()->with(['programme', 'specialisation'])->latest()->first(),
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits
        ]);

        return $pdf->download('results-'.$user->matric_number.'.pdf');"""

replacement = """        $application = $user->applications()->with(['programme', 'specialisation'])->latest()->first();

        // Get logo base64
        $logoPath = public_path('nbs-logo.png');
        $logoBase64 = '';
        if (file_exists($logoPath)) {
            $logoData = file_get_contents($logoPath);
            $logoBase64 = 'data:image/png;base64,' . base64_encode($logoData);
        }

        // Get passport base64
        $passportBase64 = '';
        if ($application && isset($application->personal_info['passport_photograph_path'])) {
            $passportPath = storage_path('app/public/' . $application->personal_info['passport_photograph_path']);
            if (file_exists($passportPath)) {
                $passportData = file_get_contents($passportPath);
                $type = pathinfo($passportPath, PATHINFO_EXTENSION);
                $passportBase64 = 'data:image/' . $type . ';base64,' . base64_encode($passportData);
            }
        }

        $pdf = \\Barryvdh\\DomPDF\\Facade\\Pdf::loadView('student.results-pdf', [
            'user' => $user,
            'application' => $application,
            'resultsBySession' => $resultsBySession,
            'cgpa' => $cgpa,
            'cumulativeCredits' => $cumulativeCredits,
            'logoBase64' => $logoBase64,
            'passportBase64' => $passportBase64
        ]);

        return $pdf->stream('results-'.$application->application_number.'.pdf');"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Patched DashboardController")
else:
    print("Target not found in DashboardController")
