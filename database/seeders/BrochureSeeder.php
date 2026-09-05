<?php

namespace Database\Seeders;

use App\Models\AdmissionRequirement;
use App\Models\Course;
use App\Models\Programme;
use App\Models\Specialisation;
use Illuminate\Database\Seeder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\File;

class BrochureSeeder extends Seeder
{
    public function run(): void
    {
        $json = File::get(database_path('seeders/brochure_data.json'));
        $data = json_decode($json, true);

        Model::unguard();

        foreach ($data['programmes'] as $progKey => $progData) {
            $programme = Programme::firstOrCreate(
                ['name' => $progData['name']],
                [
                    'code' => $progData['type'],
                    'type' => $progData['type'],
                ]
            );

            // Requirements
            foreach ($progData['requirements'] as $req) {
                AdmissionRequirement::firstOrCreate([
                    'programme_id' => $programme->id,
                    'description' => $req['desc'],
                    'is_document' => $req['is_doc']
                ]);
            }

            // Foundational Core
            foreach ($progData['foundational_core'] as $courseData) {
                $course = Course::firstOrCreate(
                    ['code' => $courseData['code']],
                    ['title' => $courseData['title'], 'units' => $courseData['units']]
                );
                $programme->courses()->syncWithoutDetaching([$course->id]);
            }

            // Specialisations
            foreach ($progData['specialisations'] as $specData) {
                $spec = Specialisation::firstOrCreate([
                    'programme_id' => $programme->id,
                    'name' => $specData['name'],
                ]);

                // Spec Courses
                foreach ($specData['courses'] as $courseData) {
                    $course = Course::firstOrCreate(
                        ['code' => $courseData['code']],
                        ['title' => $courseData['title'], 'units' => $courseData['units']]
                    );
                    $spec->courses()->syncWithoutDetaching([$course->id => ['is_elective' => false]]);
                }

                // Spec Electives
                foreach ($specData['electives'] as $courseData) {
                    $course = Course::firstOrCreate(
                        ['code' => $courseData['code']],
                        ['title' => $courseData['title'], 'units' => $courseData['units']]
                    );
                    $spec->courses()->syncWithoutDetaching([$course->id => ['is_elective' => true]]);
                }
            }
        }

        Model::reguard();
    }
}
