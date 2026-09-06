file_path = '/Users/sinan/Herd/Business School/routes/web.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        Route::get('/courses/slip', [\App\Http\Controllers\Student\DashboardController::class, 'printSlip'])->name('courses.slip');
        Route::get('/results', [\App\Http\Controllers\Student\DashboardController::class, 'results'])->name('results');"""

replace = """        Route::get('/courses/slip', [\App\Http\Controllers\Student\DashboardController::class, 'printSlip'])->name('courses.slip');
        Route::get('/results', [\App\Http\Controllers\Student\DashboardController::class, 'results'])->name('results');
        Route::get('/id-card', [\App\Http\Controllers\Student\DashboardController::class, 'idCard'])->name('idcard');"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched web.php")
else:
    print("Search block not found")
