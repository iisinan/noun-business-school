<?php
require 'vendor/autoload.php';
$app = require_once 'bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

use App\Models\User;
use Illuminate\Support\Facades\Hash;
use Spatie\Permission\Models\Role;

$email = 'abbello@noun.edu.ng';
$password = 'Ezzeddin@#321';

// Create or update the user
$user = User::updateOrCreate(
    ['email' => $email],
    [
        'first_name' => 'Admin',
        'last_name' => 'Bello',
        'password' => Hash::make($password)
    ]
);

// Ensure the "Super Admin" role exists
$role = Role::firstOrCreate(['name' => 'Super Admin', 'guard_name' => 'web']);

// Assign the role
$user->assignRole($role);

echo "Admin created successfully.\n";
