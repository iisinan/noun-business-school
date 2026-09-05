<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/AcademicSessionController.php';
$content = file_get_contents($file);

$additions = <<<PHP

    public function advanceSemester(AcademicSession \$session)
    {
        \$session->update([
            'current_semester' => \$session->current_semester + 1,
            'registration_open' => true,
        ]);

        return redirect()->route('admin.sessions.index')->with('success', 'Advanced to Semester ' . \$session->current_semester . '.');
    }

    public function toggleRegistration(AcademicSession \$session)
    {
        \$session->update([
            'registration_open' => !\$session->registration_open
        ]);

        \$status = \$session->registration_open ? 'opened' : 'closed';
        return redirect()->route('admin.sessions.index')->with('success', "Registration has been {\$status} for Semester {\$session->current_semester}.");
    }
}
PHP;

$content = preg_replace('/\}\s*$/', $additions, $content);
file_put_contents($file, $content);
echo "Patched AcademicSessionController\n";
