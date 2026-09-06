file_path = '/Users/sinan/Herd/Business School/routes/web.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        Route::get('/results/upload', [\App\Http\Controllers\Admin\ResultController::class, 'create'])->name('results.upload');"""

replace = """        Route::get('/results/template', [\App\Http\Controllers\Admin\ResultController::class, 'downloadTemplate'])->name('results.template');
        Route::get('/results/upload', [\App\Http\Controllers\Admin\ResultController::class, 'create'])->name('results.upload');"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched routes")
else:
    print("Failed to patch routes")
