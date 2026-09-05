<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$apps = \App\Models\Application::whereNotNull('documents')->where('documents', '!=', '[]')->get();
if ($apps->count() > 0) {
    echo "Found application with documents: " . $apps->first()->id . "\n";
    echo json_encode($apps->first()->documents);
} else {
    echo "No applications with documents found. Updating the latest one to have a dummy document.\n";
    $a = \App\Models\Application::latest()->first();
    $a->documents = [
        'resume' => 'applications/documents/dummy_resume.pdf',
        'degree_certificate' => [
            'applications/documents/dummy_cert1.jpg',
            'applications/documents/dummy_cert2.jpg'
        ]
    ];
    $a->save();
    echo "Updated application " . $a->id . " with dummy documents.\n";
}
