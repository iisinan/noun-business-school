<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/AcademicSessionController.php';
$content = file_get_contents($file);

$search = <<<PHP
    public function index()
    {
        \$sessions = AcademicSession::latest()->get();
        return Inertia::render('Admin/Sessions/Index', [
            'sessions' => \$sessions
        ]);
    }
PHP;

$replace = <<<PHP
    public function index()
    {
        \$sessions = AcademicSession::withCount([
            'applications as total_applications',
            'applications as enrolled_students' => function(\$query) {
                \$query->where('status', 'ENROLLED');
            }
        ])->latest()->get();
        
        return Inertia::render('Admin/Sessions/Index', [
            'sessions' => \$sessions
        ]);
    }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched AcademicSessionController\n";
