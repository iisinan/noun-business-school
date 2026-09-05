<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$programmes = App\Models\Programme::with(['admissionRequirements' => function($q) {
    $q->where('is_document', 1);
}])->get();

foreach($programmes as $p) {
    echo 'Course: ' . $p->name . ' (' . $p->code . ')' . PHP_EOL;
    if ($p->admissionRequirements->isEmpty()) {
        echo '  - No documents required' . PHP_EOL;
    } else {
        foreach($p->admissionRequirements as $req) {
            echo '  - ' . $req->description . PHP_EOL;
        }
    }
    echo PHP_EOL;
}
