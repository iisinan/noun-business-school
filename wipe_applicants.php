<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

Schema::disableForeignKeyConstraints();

DB::table('applications')->truncate();
DB::table('payments')->truncate();
DB::table('wallet_transactions')->truncate();
DB::table('course_registrations')->truncate();
DB::table('semester_registrations')->truncate();

$users = User::all();
$deleted = 0;
foreach ($users as $user) {
    if (!$user->hasRole('Super Admin')) {
        $user->delete();
        $deleted++;
    }
}

Schema::enableForeignKeyConstraints();

echo "Cleared all application data and deleted {$deleted} applicants/students!\n";
