<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = <<<PHP
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');
PHP;

$replace = <<<PHP
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');
        Route::post('/sessions/{session}/advance-semester', [AcademicSessionController::class, 'advanceSemester'])->name('sessions.advance-semester');
        Route::post('/sessions/{session}/toggle-registration', [AcademicSessionController::class, 'toggleRegistration'])->name('sessions.toggle-registration');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php routes\n";
