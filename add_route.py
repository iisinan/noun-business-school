with open('routes/web.php', 'r') as f:
    lines = f.readlines()

new_route = """Route::get('/programmes', function () {
    return Inertia::render('Programmes');
})->name('programmes');
"""

for i, line in enumerate(lines):
    if "Route::get('/resources'" in line:
        lines.insert(i, new_route)
        break

with open('routes/web.php', 'w') as f:
    f.writelines(lines)
    
print("Added /programmes route")
