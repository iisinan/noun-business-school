<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ApplicationController.php';
$content = file_get_contents($file);

$search = <<<PHP
    public function index()
    {
        \$applications = Application::with('user', 'programme')->latest()->paginate(20);
        return Inertia::render('Admin/Applications/Index', [
            'applications' => \$applications
        ]);
    }
PHP;

$replace = <<<PHP
    public function index(\Illuminate\Http\Request \$request)
    {
        \$query = Application::with('user', 'programme')->latest();

        if (\$request->filled('search')) {
            \$searchTerm = \$request->search;
            \$query->where(function (\$q) use (\$searchTerm) {
                \$q->where('application_number', 'like', "%{\$searchTerm}%")
                  ->orWhereHas('user', function (\$uq) use (\$searchTerm) {
                      \$uq->where('first_name', 'like', "%{\$searchTerm}%")
                         ->orWhere('last_name', 'like', "%{\$searchTerm}%")
                         ->orWhere('email', 'like', "%{\$searchTerm}%");
                  });
            });
        }

        if (\$request->filled('status')) {
            \$query->where('status', \$request->status);
        }

        if (\$request->filled('programme_id')) {
            \$query->where('programme_id', \$request->programme_id);
        }

        \$applications = \$query->paginate(20)->withQueryString();
        
        \$programmes = \App\Models\Programme::select('id', 'name')->orderBy('name')->get();

        return Inertia::render('Admin/Applications/Index', [
            'applications' => \$applications,
            'programmes' => \$programmes,
            'filters' => \$request->only(['search', 'status', 'programme_id'])
        ]);
    }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched ApplicationController\n";
