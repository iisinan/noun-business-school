with open('routes/web.php', 'r') as f:
    content = f.read()

target = "Route::get('/results', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'results'])->name('results');"
replacement = "Route::get('/results', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'results'])->name('results');\n        Route::get('/results/download', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'downloadResults'])->name('results.download');"

if target in content:
    content = content.replace(target, replacement)
    with open('routes/web.php', 'w') as f:
        f.write(content)
    print("Patched routes")
else:
    print("Target not found in routes/web.php")
