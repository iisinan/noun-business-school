<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ApplicationController.php';
$content = file_get_contents($file);

$search = <<<PHP
        \$appData = \$application->toArray();
        \$appData['document_urls'] = \$documentUrls;
PHP;

$replace = <<<PHP
        \$appData = \$application->toArray();
        \$appData['document_urls'] = \$documentUrls;
        
        if (isset(\$application->personal_info['passport_photograph_path'])) {
            \$appData['passport_url'] = \Illuminate\Support\Facades\Storage::disk('s3')->url(\$application->personal_info['passport_photograph_path']);
        }
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Admin/ApplicationController.php\n";
