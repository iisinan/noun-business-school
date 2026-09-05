import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Fix middleware
content = content.replace("middleware('role:Applicant')", "middleware('role:Applicant|Student')")

# Add admission letter route
letter_route = """        Route::get('/application', [ApplicationController::class, 'create'])->name('application.create');
        Route::get('/admission-letter', [ApplicationController::class, 'letter'])->name('application.letter');"""
content = content.replace("Route::get('/application', [ApplicationController::class, 'create'])->name('application.create');", letter_route)

with open('routes/web.php', 'w') as f:
    f.write(content)

