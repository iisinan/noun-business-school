import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add docket route
docket_route = """        Route::get('/application', [ApplicationController::class, 'create'])->name('application.create');
        Route::get('/application/docket', [ApplicationController::class, 'docket'])->name('application.docket');
        Route::get('/admission-letter', [ApplicationController::class, 'letter'])->name('application.letter');"""
content = content.replace("Route::get('/application', [ApplicationController::class, 'create'])->name('application.create');\n        Route::get('/admission-letter', [ApplicationController::class, 'letter'])->name('application.letter');", docket_route)

with open('routes/web.php', 'w') as f:
    f.write(content)

