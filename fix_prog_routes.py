import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add use statement
content = content.replace(
    "use App\\Http\\Controllers\\Admin\\UsersController;",
    "use App\\Http\\Controllers\\Admin\\UsersController;\nuse App\\Http\\Controllers\\Admin\\ProgrammeController;"
)

# Replace Route
old_route = "        Route::get('/programmes', function() { return Inertia::render('Admin/Programmes/Index', ['programmes' => \App\Models\Programme::with('specialisations')->get()]); })->name('programmes.index');"
new_routes = """        Route::get('/programmes', [ProgrammeController::class, 'index'])->name('programmes.index');
        Route::get('/programmes/create', [ProgrammeController::class, 'create'])->name('programmes.create');
        Route::post('/programmes', [ProgrammeController::class, 'store'])->name('programmes.store');"""

content = content.replace(old_route, new_routes)

with open('routes/web.php', 'w') as f:
    f.write(content)

