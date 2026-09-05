<?php
$file = '/Users/sinan/Herd/Business School/routes/web.php';
$content = file_get_contents($file);

$search = <<<PHP
        Route::delete('/programmes/{programme}/courses/{course}', [ProgrammeController::class, 'detachCourse'])->name('programmes.courses.detach');
PHP;

$replace = <<<PHP
        Route::delete('/programmes/{programme}/courses/{course}', [ProgrammeController::class, 'detachCourse'])->name('programmes.courses.detach');
        Route::patch('/programmes/{programme}/toggle-status', [ProgrammeController::class, 'toggleStatus'])->name('programmes.toggle-status');
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched web.php routes\n";
