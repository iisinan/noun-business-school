with open('routes/web.php', 'r') as f:
    content = f.read()

target = "Route::get('/courses/slip', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'printSlip'])->name('courses.slip');"
replacement = """Route::get('/courses/slip', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'printSlip'])->name('courses.slip');
        Route::get('/results', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'results'])->name('results');"""

content = content.replace(target, replacement)

with open('routes/web.php', 'w') as f:
    f.write(content)
