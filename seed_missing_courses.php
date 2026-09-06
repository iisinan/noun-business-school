<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$json = file_get_contents('parsed_courses.json');
$data = json_decode($json, true);

foreach ($data as $key => $details) {
    if (!isset($details['shortTitle'])) continue;
    
    $specName = $details['shortTitle'];
    $spec = \App\Models\Specialisation::where('name', $specName)->first();
    
    if (!$spec) {
        continue;
    }
    
    if (isset($details['coreCourses'])) {
        foreach ($details['coreCourses'] as $courseData) {
            $course = \App\Models\Course::firstOrCreate(
                ['code' => $courseData['code']],
                [
                    'title' => $courseData['title'], 
                    'units' => $courseData['units'],
                    'semester' => 2,
                    'type' => 'Core'
                ]
            );
            $spec->courses()->syncWithoutDetaching([$course->id => ['is_elective' => false]]);
        }
    }
    
    if (isset($details['electiveCourses'])) {
        foreach ($details['electiveCourses'] as $courseData) {
            $course = \App\Models\Course::firstOrCreate(
                ['code' => $courseData['code']],
                [
                    'title' => $courseData['title'], 
                    'units' => $courseData['units'],
                    'semester' => 2,
                    'type' => 'Elective'
                ]
            );
            $spec->courses()->syncWithoutDetaching([$course->id => ['is_elective' => true]]);
        }
    }
}
echo "Done seeding missing courses!\n";
