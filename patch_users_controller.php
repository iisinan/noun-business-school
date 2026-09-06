<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/UsersController.php';
$content = file_get_contents($file);

$search = <<<PHP
        return Inertia::render('Admin/Users/Show', [
            'user' => \$user,
        ]);
PHP;

$replace = <<<PHP
        \$userData = \$user->toArray();
        \$app = \App\Models\Application::where('user_id', \$user->id)->latest()->first();
        if (\$app && isset(\$app->personal_info['passport_photograph_path'])) {
            \$userData['passport_url'] = \Illuminate\Support\Facades\Storage::disk('s3')->url(\$app->personal_info['passport_photograph_path']);
        }

        return Inertia::render('Admin/Users/Show', [
            'user' => \$userData,
        ]);
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched UsersController.php\n";
