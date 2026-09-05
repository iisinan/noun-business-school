<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ProgrammeController.php';
$content = file_get_contents($file);

$additions = <<<PHP

    public function toggleStatus(Programme \$programme)
    {
        \$programme->update([
            'is_active' => !\$programme->is_active
        ]);

        \$status = \$programme->is_active ? 'activated' : 'suspended';
        return back()->with('success', "Programme has been {\$status}.");
    }
}
PHP;

$content = preg_replace('/\}\s*$/', $additions, $content);
file_put_contents($file, $content);
echo "Patched ProgrammeController toggleStatus\n";
