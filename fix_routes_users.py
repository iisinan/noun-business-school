import re

with open('routes/web.php', 'r') as f:
    content = f.read()

# Add use statement at top
content = content.replace(
    "use App\\Http\\Controllers\\Admin\\ApplicationController as AdminApplicationController;",
    "use App\\Http\\Controllers\\Admin\\ApplicationController as AdminApplicationController;\nuse App\\Http\\Controllers\\Admin\\UsersController;"
)

# Add route
users_route = """        Route::get('/programmes', function() { return Inertia::render('Admin/Programmes/Index', ['programmes' => \App\Models\Programme::with('specialisations')->get()]); })->name('programmes.index');
        Route::get('/users', [UsersController::class, 'index'])->name('users.index');"""

content = content.replace("        Route::get('/programmes', function() { return Inertia::render('Admin/Programmes/Index', ['programmes' => \App\Models\Programme::with('specialisations')->get()]); })->name('programmes.index');", users_route)

with open('routes/web.php', 'w') as f:
    f.write(content)

