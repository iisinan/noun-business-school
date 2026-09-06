<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Middleware/HandleInertiaRequests.php';
$content = file_get_contents($file);

$search = <<<PHP
            'auth' => [
                'user' => \$request->user(),
            ],
PHP;

$replace = <<<PHP
            'auth' => [
                'user' => function () use (\$request) {
                    \$user = \$request->user();
                    if (\$user) {
                        \$data = \$user->toArray();
                        \$app = \App\Models\Application::where('user_id', \$user->id)->latest()->first();
                        if (\$app && isset(\$app->personal_info['passport_photograph_path'])) {
                            \$data['passport_url'] = \Illuminate\Support\Facades\Storage::disk('s3')->url(\$app->personal_info['passport_photograph_path']);
                        }
                        return \$data;
                    }
                    return null;
                },
            ],
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched HandleInertiaRequests.php\n";
