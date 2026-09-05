<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = <<<PHP
        Route::patch('/programmes/{programme}/toggle-status', [ProgrammeController::class, 'toggleStatus'])->name('programmes.toggle-status');
PHP;

$replace = <<<PHP
        Route::patch('/programmes/{programme}/toggle-status', [ProgrammeController::class, 'toggleStatus'])->name('programmes.toggle-status');

        Route::get('/specialisations/{specialisation}', [\App\Http\Controllers\Admin\SpecialisationController::class, 'show'])->name('specialisations.show');
        Route::post('/specialisations/{specialisation}/courses', [\App\Http\Controllers\Admin\SpecialisationController::class, 'attachCourse'])->name('specialisations.courses.attach');
        Route::delete('/specialisations/{specialisation}/courses/{course}', [\App\Http\Controllers\Admin\SpecialisationController::class, 'detachCourse'])->name('specialisations.courses.detach');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php routes\n";
