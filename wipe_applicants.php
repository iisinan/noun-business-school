<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\Application;
use App\Models\ApplicantDocument;
use App\Models\ApplicantEmployment;
use App\Models\ApplicantQualification;
use App\Models\Payment;
use App\Models\User;

\Schema::disableForeignKeyConstraints();

ApplicantDocument::truncate();
ApplicantEmployment::truncate();
ApplicantQualification::truncate();
Application::truncate();
Payment::truncate();
\DB::table('wallet_transactions')->truncate();
\DB::table('course_registrations')->truncate();
\DB::table('semester_registrations')->truncate();

$users = User::all();
foreach ($users as $user) {
    if (!$user->hasRole('admin') && !$user->hasRole('super-admin')) {
        $user->delete();
    }
}

\Schema::enableForeignKeyConstraints();

echo "All applicant data cleared!";
