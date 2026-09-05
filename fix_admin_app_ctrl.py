import re

with open('app/Http/Controllers/Admin/ApplicationController.php', 'r') as f:
    content = f.read()

export_method = """    /**
     * Display the DataTables list of all applications.
     */
    public function index()
    {
        $applications = Application::with('user', 'programme')->latest()->paginate(20);
        return Inertia::render('Admin/Applications/Index', [
            'applications' => $applications
        ]);
    }

    /**
     * Export applications to CSV.
     */
    public function export()
    {
        $applications = Application::with('user', 'programme', 'specialisation')->get();

        $headers = [
            "Content-type"        => "text/csv",
            "Content-Disposition" => "attachment; filename=applications_" . date('Y-m-d') . ".csv",
            "Pragma"              => "no-cache",
            "Cache-Control"       => "must-revalidate, post-check=0, pre-check=0",
            "Expires"             => "0"
        ];

        $columns = ['Application No', 'First Name', 'Last Name', 'Email', 'Phone', 'Programme', 'Specialisation', 'Status', 'Date Submitted'];

        $callback = function() use($applications, $columns) {
            $file = fopen('php://output', 'w');
            fputcsv($file, $columns);

            foreach ($applications as $app) {
                fputcsv($file, [
                    $app->application_number,
                    $app->user->first_name ?? '',
                    $app->user->last_name ?? '',
                    $app->user->email ?? '',
                    $app->user->phone ?? '',
                    $app->programme->name ?? '',
                    $app->specialisation->name ?? '',
                    $app->status,
                    $app->created_at->format('Y-m-d H:i:s')
                ]);
            }

            fclose($file);
        };

        return response()->stream($callback, 200, $headers);
    }"""

content = content.replace("""    /**
     * Display the DataTables list of all applications.
     */
    public function index()
    {
        $applications = Application::with('user', 'programme')->latest()->paginate(20);
        return Inertia::render('Admin/Applications/Index', [
            'applications' => $applications
        ]);
    }""", export_method)

with open('app/Http/Controllers/Admin/ApplicationController.php', 'w') as f:
    f.write(content)

