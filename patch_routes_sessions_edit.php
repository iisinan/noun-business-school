<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = <<<PHP
        Route::post('/sessions/{session}/toggle-registration', [AcademicSessionController::class, 'toggleRegistration'])->name('sessions.toggle-registration');
PHP;

$replace = <<<PHP
        Route::post('/sessions/{session}/toggle-registration', [AcademicSessionController::class, 'toggleRegistration'])->name('sessions.toggle-registration');
        Route::put('/sessions/{session}', [AcademicSessionController::class, 'update'])->name('sessions.update');
        Route::delete('/sessions/{session}', [AcademicSessionController::class, 'destroy'])->name('sessions.destroy');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php routes\n";
