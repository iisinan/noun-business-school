<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();

$count = \App\Models\Programme::count();
$names = \App\Models\Programme::pluck('name');
echo "Count: \$count\n";
echo "Names: " . json_encode($names) . "\n";
