<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$json = file_get_contents('parsed_courses.json');
$data = json_decode($json, true);
$missing = [];
foreach ($data as $key => $details) {
    if (!isset($details['shortTitle'])) continue;
    $specName = $details['shortTitle'];
    $spec = \App\Models\Specialisation::where('name', $specName)->first();
    if (!$spec) {
        $missing[] = $specName;
    }
}
echo "Missing: " . count($missing) . "\n";
print_r(array_slice($missing, 0, 5));
