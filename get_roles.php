<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$users = App\Models\User::with('roles')->get();
foreach ($users as $user) {
    echo "User: " . $user->email . "\n";
    foreach ($user->roles as $role) {
        echo " - Role: " . $role->name . "\n";
    }
}
