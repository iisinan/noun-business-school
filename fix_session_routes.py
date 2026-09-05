import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add use statement
content = content.replace(
    "use App\\Http\\Controllers\\Admin\\CourseController;",
    "use App\\Http\\Controllers\\Admin\\CourseController;\nuse App\\Http\\Controllers\\Admin\\AcademicSessionController;"
)

# Add routes
new_routes = """        Route::get('/courses', [CourseController::class, 'index'])->name('courses.index');
        Route::get('/courses/create', [CourseController::class, 'create'])->name('courses.create');
        Route::post('/courses', [CourseController::class, 'store'])->name('courses.store');
        
        Route::get('/sessions', [AcademicSessionController::class, 'index'])->name('sessions.index');
        Route::post('/sessions', [AcademicSessionController::class, 'store'])->name('sessions.store');
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');"""

content = content.replace("        Route::get('/courses', [CourseController::class, 'index'])->name('courses.index');\n        Route::get('/courses/create', [CourseController::class, 'create'])->name('courses.create');\n        Route::post('/courses', [CourseController::class, 'store'])->name('courses.store');", new_routes)

with open('routes/web.php', 'w') as f:
    f.write(content)

