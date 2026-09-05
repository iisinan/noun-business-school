<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$a = \App\Models\Application::find(4) ?? \App\Models\Application::latest()->first();
echo "DOCS:\n";
echo json_encode($a->documents);
echo "\nURLS:\n";
$documentUrls = [];
if (is_array($a->documents)) {
    foreach ($a->documents as $key => $path) {
        if (is_array($path)) {
            $documentUrls[$key] = array_map(fn($p) => \Illuminate\Support\Facades\Storage::disk('s3')->url($p), $path);
        } else {
            $documentUrls[$key] = \Illuminate\Support\Facades\Storage::disk('s3')->url($path);
        }
    }
}
echo json_encode($documentUrls);
