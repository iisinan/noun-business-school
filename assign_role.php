<?php
require __DIR__.'/vendor/autoload.php';
$app = require_once __DIR__.'/bootstrap/app.php';
$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);
$kernel->bootstrap();

$user = App\Models\User::where('email', 'sinanismailaidris@gmail.com')->first();
if ($user && !$user->hasRole('Student')) {
    $user->assignRole('Student');
    echo "Assigned Student role to sinanismailaidris@gmail.com\n";
}
