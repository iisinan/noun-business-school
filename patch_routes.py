with open('routes/web.php', 'r') as f:
    content = f.read()

target = "Route::get('/registration', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'registration'])->name('registration');"
replacement = """Route::get('/registration', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'registration'])->name('registration');
        Route::get('/payments', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'payments'])->name('payments');"""

content = content.replace(target, replacement)

with open('routes/web.php', 'w') as f:
    f.write(content)
