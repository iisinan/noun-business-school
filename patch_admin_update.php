<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ApplicationController.php';
$content = file_get_contents($file);

$search = <<<PHP
    public function updateStatus(Request \$request, Application \$application)
    {
        \$validated = \$request->validate([
            'status' => 'required|in:UNDER REVIEW,ADMITTED,REJECTED'
        ]);
PHP;

$replace = <<<PHP
    public function updateStatus(Request \$request, Application \$application)
    {
        if (\$application->status === 'STARTED') {
            return redirect()->back()->with('error', 'Cannot make admissions decisions on unpaid applications.');
        }

        \$validated = \$request->validate([
            'status' => 'required|in:UNDER REVIEW,ADMITTED,REJECTED'
        ]);
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Admin/ApplicationController.php\n";
