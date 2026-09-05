<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = <<<PHP
        Route::get('/programmes', [ProgrammeController::class, 'index'])->name('programmes.index');
        Route::get('/programmes/create', [ProgrammeController::class, 'create'])->name('programmes.create');
        Route::post('/programmes', [ProgrammeController::class, 'store'])->name('programmes.store');
PHP;

$replace = <<<PHP
        Route::get('/programmes', [ProgrammeController::class, 'index'])->name('programmes.index');
        Route::get('/programmes/create', [ProgrammeController::class, 'create'])->name('programmes.create');
        Route::post('/programmes', [ProgrammeController::class, 'store'])->name('programmes.store');
        Route::get('/programmes/{programme}', [ProgrammeController::class, 'show'])->name('programmes.show');
        Route::post('/programmes/{programme}/courses', [ProgrammeController::class, 'attachCourse'])->name('programmes.courses.attach');
        Route::delete('/programmes/{programme}/courses/{course}', [ProgrammeController::class, 'detachCourse'])->name('programmes.courses.detach');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php routes\n";
