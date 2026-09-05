<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$apps = \App\Models\Application::all();
foreach ($apps as $a) {
    echo "App ID: " . $a->id . ", User ID: " . $a->user_id . ", Status: " . $a->status . "\n";
}
