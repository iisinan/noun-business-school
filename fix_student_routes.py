import re

with open('routes/web.php', 'r') as f:
    content = f.read()

target = """    Route::middleware(['role:Student'])->prefix('student')->name('student.')->group(function () {
        Route::get('/dashboard', [\App\Http\Controllers\Student\DashboardController::class, 'index'])->name('dashboard');
        Route::post('/semester/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerSemester'])->name('semester.register');"""

replacement = """    Route::middleware(['role:Student'])->prefix('student')->name('student.')->group(function () {
        Route::get('/dashboard', [\App\Http\Controllers\Student\DashboardController::class, 'index'])->name('dashboard');
        Route::get('/registration', [\App\Http\Controllers\Student\DashboardController::class, 'registration'])->name('registration');
        Route::post('/semester/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerSemester'])->name('semester.register');"""

content = content.replace(target, replacement)

with open('routes/web.php', 'w') as f:
    f.write(content)


with open('resources/js/Layouts/StudentLayout.vue', 'r') as f:
    layout = f.read()

layout = layout.replace(
    "name: 'Course Registration', href: route('student.dashboard'), active: false",
    "name: 'Course Registration', href: route('student.registration'), active: route().current('student.registration')"
)

with open('resources/js/Layouts/StudentLayout.vue', 'w') as f:
    f.write(layout)

