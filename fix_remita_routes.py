import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add Remita Gateway routes (needs to be available to logged in users)
remita_routes = """    // Remita Simulation Routes
    Route::middleware('auth')->group(function () {
        Route::get('/remita/gateway', [PaymentController::class, 'gateway'])->name('remita.gateway');
        Route::post('/remita/pay', [PaymentController::class, 'simulatePay'])->name('remita.pay');
    });

    // Applicant Routes"""
content = content.replace("    // Applicant Routes", remita_routes)

with open('routes/web.php', 'w') as f:
    f.write(content)

