<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();

$specs = \App\Models\Specialisation::take(5)->pluck('name');
echo json_encode($specs) . "\n";
