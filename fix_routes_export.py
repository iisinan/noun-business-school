import re

with open('routes/web.php', 'r') as f:
    content = f.read()

export_route = """        Route::get('/applications', [AdminApplicationController::class, 'index'])->name('applications.index');
        Route::get('/applications/export', [AdminApplicationController::class, 'export'])->name('applications.export');
        Route::get('/applications/{application}', [AdminApplicationController::class, 'show'])->name('applications.show');"""
content = content.replace("        Route::get('/applications', [AdminApplicationController::class, 'index'])->name('applications.index');\n        Route::get('/applications/{application}', [AdminApplicationController::class, 'show'])->name('applications.show');", export_route)

with open('routes/web.php', 'w') as f:
    f.write(content)

