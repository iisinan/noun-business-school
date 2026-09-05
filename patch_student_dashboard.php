<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

// 1. Pass registration_open to the Registration page
$searchReg = <<<PHP
        return Inertia::render('Student/Registration', [
            'application' => \$application,
            'hasRegisteredSemester' => \$hasRegisteredSemester,
            'availableCourses' => \$availableCourses,
            'registeredCourses' => \$registeredCourses,
        ]);
PHP;

$replaceReg = <<<PHP
        return Inertia::render('Student/Registration', [
            'application' => \$application,
            'hasRegisteredSemester' => \$hasRegisteredSemester,
            'availableCourses' => \$availableCourses,
            'registeredCourses' => \$registeredCourses,
            'registrationOpen' => \$activeSession ? \$activeSession->registration_open : false,
        ]);
PHP;

$content = str_replace($searchReg, $replaceReg, $content);

// 2. Add validation block to registerSemester
$searchRegSem = <<<PHP
    public function registerSemester(Request \$request)
    {
        \$user = \$request->user();
        \$activeSession = AcademicSession::where('is_active', true)->first();

        if (!\$activeSession) {
            return back()->with('error', 'No active academic session.');
        }

        \$fee = 25000;
PHP;

$replaceRegSem = <<<PHP
    public function registerSemester(Request \$request)
    {
        \$user = \$request->user();
        \$activeSession = AcademicSession::where('is_active', true)->first();

        if (!\$activeSession) {
            return back()->with('error', 'No active academic session.');
        }
        
        if (!\$activeSession->registration_open) {
            return back()->with('error', 'Registration for this semester is currently closed.');
        }

        \$fee = 25000;
PHP;

$content = str_replace($searchRegSem, $replaceRegSem, $content);

// 3. Add validation block to registerCourses
$searchRegCour = <<<PHP
    public function registerCourses(Request \$request)
    {
        \$user = \$request->user();
        \$activeSession = AcademicSession::where('is_active', true)->first();

        if (!\$activeSession) {
            return back()->with('error', 'No active academic session.');
        }
PHP;

$replaceRegCour = <<<PHP
    public function registerCourses(Request \$request)
    {
        \$user = \$request->user();
        \$activeSession = AcademicSession::where('is_active', true)->first();

        if (!\$activeSession) {
            return back()->with('error', 'No active academic session.');
        }
        
        if (!\$activeSession->registration_open) {
            return back()->with('error', 'Registration for this semester is currently closed.');
        }
PHP;

$content = str_replace($searchRegCour, $replaceRegCour, $content);

file_put_contents($file, $content);
echo "Patched DashboardController\n";
