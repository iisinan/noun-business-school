import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add use statement
content = content.replace(
    "use App\\Http\\Controllers\\Admin\\ProgrammeController;",
    "use App\\Http\\Controllers\\Admin\\ProgrammeController;\nuse App\\Http\\Controllers\\Admin\\CourseController;"
)

# Replace Route
old_route = "        Route::get('/courses', function() { return Inertia::render('Admin/Courses/Index', ['courses' => \App\Models\Course::paginate(50)]); })->name('courses.index');"
new_routes = """        Route::get('/courses', [CourseController::class, 'index'])->name('courses.index');
        Route::get('/courses/create', [CourseController::class, 'create'])->name('courses.create');
        Route::post('/courses', [CourseController::class, 'store'])->name('courses.store');"""

content = content.replace(old_route, new_routes)

with open('routes/web.php', 'w') as f:
    f.write(content)

