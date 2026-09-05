<?php
$file = '/Users/sinan/Herd/Business School/app/Models/AcademicSession.php';
$content = file_get_contents($file);

$search = <<<PHP
    protected \$casts = [
        'is_active' => 'boolean'
    ];
PHP;

$replace = <<<PHP
    protected \$casts = [
        'is_active' => 'boolean',
        'registration_open' => 'boolean',
    ];
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched AcademicSession.php\n";
