<?php
$file = '/Users/sinan/Herd/Business School/app/Models/AcademicSession.php';
$content = file_get_contents($file);

$additions = <<<PHP

    public function applications()
    {
        return \$this->hasMany(Application::class);
    }
}
PHP;

$content = preg_replace('/\}\s*$/', $additions, $content);
file_put_contents($file, $content);
echo "Patched AcademicSession.php\n";
