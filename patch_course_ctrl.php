<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/CourseController.php';
$content = file_get_contents($file);

$search = <<<PHP
    public function index(Request \$request)
    {
        \$query = Course::query();

        if (\$request->has('search') && \$request->search != '') {
            \$search = \$request->search;
            \$query->where('code', 'like', "%{\$search}%")
                  ->orWhere('title', 'like', "%{\$search}%");
        }

        \$courses = \$query->latest()->paginate(20)->withQueryString();

        return Inertia::render('Admin/Courses/Index', [
            'courses' => \$courses,
            'filters' => \$request->only('search')
        ]);
    }
PHP;

$replace = <<<PHP
    public function index(Request \$request)
    {
        \$query = Course::query();

        if (\$request->filled('search')) {
            \$search = \$request->search;
            \$query->where(function(\$q) use (\$search) {
                \$q->where('code', 'like', "%{\$search}%")
                  ->orWhere('title', 'like', "%{\$search}%");
            });
        }

        if (\$request->filled('programme_id')) {
            \$query->whereHas('programmes', function(\$q) use (\$request) {
                \$q->where('programmes.id', \$request->programme_id);
            });
        }

        \$courses = \$query->latest()->paginate(20)->withQueryString();
        \$programmes = \App\Models\Programme::select('id', 'name')->orderBy('name')->get();

        return Inertia::render('Admin/Courses/Index', [
            'courses' => \$courses,
            'programmes' => \$programmes,
            'filters' => \$request->only(['search', 'programme_id'])
        ]);
    }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched CourseController\n";
