with open('routes/web.php', 'r') as f:
    content = f.read()

target = "Route::get('/payments', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'payments'])->name('payments');"
replacement = """Route::get('/payments', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'payments'])->name('payments');
        Route::get('/payments/statement', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'statement'])->name('payments.statement');"""

content = content.replace(target, replacement)

with open('routes/web.php', 'w') as f:
    f.write(content)
