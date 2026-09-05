<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$passedIds = \App\Models\CourseRegistration::where('user_id', 1) // dummy
    ->whereNotNull('grade')
    ->where('grade', '!=', 'F')
    ->pluck('course_id')
    ->toArray();
echo json_encode($passedIds);
