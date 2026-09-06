<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

try {
    // In PostgreSQL, TRUNCATE ... CASCADE ignores FK constraints and wipes dependent tables too
    DB::statement('TRUNCATE TABLE applications CASCADE;');
    DB::statement('TRUNCATE TABLE payments CASCADE;');
    DB::statement('TRUNCATE TABLE wallet_transactions CASCADE;');
    DB::statement('TRUNCATE TABLE course_registrations CASCADE;');
    DB::statement('TRUNCATE TABLE semester_registrations CASCADE;');
    
    // We should not truncate users table because we want to keep Super Admins
    // We will just delete them one by one. But wait, if they have foreign keys,
    // we should delete them manually.
    $users = User::all();
    $deleted = 0;
    foreach ($users as $user) {
        if (!$user->hasRole('Super Admin')) {
            $user->delete();
            $deleted++;
        }
    }

    echo "Cleared all application data and deleted {$deleted} applicants/students!\n";
} catch (\Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
