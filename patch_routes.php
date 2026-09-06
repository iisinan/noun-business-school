<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = "Route::get('/users/{user}', [UsersController::class, 'show'])->name('users.show');";
$replace = $search . "\n        Route::delete('/users/{user}', [UsersController::class, 'destroy'])->name('users.destroy');";

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php\n";
