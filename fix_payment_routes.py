import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add use statement
content = content.replace(
    "use App\\Http\\Controllers\\Admin\\AcademicSessionController;",
    "use App\\Http\\Controllers\\Admin\\AcademicSessionController;\nuse App\\Http\\Controllers\\Admin\\PaymentController as AdminPaymentController;"
)

# Add routes
new_routes = """        Route::get('/sessions', [AcademicSessionController::class, 'index'])->name('sessions.index');
        Route::post('/sessions', [AcademicSessionController::class, 'store'])->name('sessions.store');
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');
        
        Route::get('/payments', [AdminPaymentController::class, 'index'])->name('payments.index');"""

content = content.replace("""        Route::get('/sessions', [AcademicSessionController::class, 'index'])->name('sessions.index');
        Route::post('/sessions', [AcademicSessionController::class, 'store'])->name('sessions.store');
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');""", new_routes)

with open('routes/web.php', 'w') as f:
    f.write(content)

