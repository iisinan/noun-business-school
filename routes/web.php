<?php

use App\Http\Controllers\ProfileController;
use App\Http\Controllers\Applicant\ApplicationController;
use App\Http\Controllers\Admin\DashboardController as AdminDashboardController;
use App\Http\Controllers\Admin\ApplicationController as AdminApplicationController;
use App\Http\Controllers\Admin\UsersController;
use App\Http\Controllers\Admin\ProgrammeController;
use App\Http\Controllers\Admin\CourseController;
use App\Http\Controllers\Admin\AcademicSessionController;
use App\Http\Controllers\Admin\PaymentController as AdminPaymentController;
use App\Http\Controllers\PaymentController;
use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;

Route::get('/', function () {
    return Inertia::render('Welcome', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
    ]);
})->name('home');

Route::get('/about', function () {
    return Inertia::render('About');
})->name('about');

Route::get('/media', function () {
    return Inertia::render('Media');
})->name('media');

Route::get('/programmes', function () {
    return Inertia::render('Programmes');
})->name('programmes');
Route::get('/resources', function () {
    return Inertia::render('Resources');
})->name('resources');

Route::get('/apply', [\App\Http\Controllers\AdmissionController::class, 'start'])->name('admission.start');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    // Dashboard redirection based on role
    Route::get('/dashboard', function () {
        if (auth()->user()->hasRole('Super Admin')) {
            return redirect()->route('admin.dashboard');
        }
        
        $user = auth()->user();
        $latestApplication = $user->applications()->with('programme', 'specialisation')->latest()->first();

        // If enrolled student, redirect to student dashboard
        if ($user->hasRole('Student')) {
            return redirect()->route('student.dashboard');
        }

        return Inertia::render('Applicant/Dashboard', [
            'application' => $latestApplication,
            'is_student' => false
        ]);
    })->name('dashboard');

    // Remita Simulation Routes
    Route::middleware('auth')->group(function () {
        Route::get('/remita/gateway', [PaymentController::class, 'gateway'])->name('remita.gateway');
        Route::post('/remita/pay', [PaymentController::class, 'simulatePay'])->name('remita.pay');
    });

    // Applicant Routes
    Route::middleware('role:Applicant|Student')->prefix('applicant')->name('applicant.')->group(function () {
                        Route::get('/application', [ApplicationController::class, 'create'])->name('application.create');
        Route::get('/application/docket', [ApplicationController::class, 'docket'])->name('application.docket');
        Route::get('/admission-letter', [ApplicationController::class, 'letter'])->name('application.letter');
        Route::post('/application', [ApplicationController::class, 'store'])->name('application.store');
        Route::get('/payment/initiate', [PaymentController::class, 'initiate'])->name('payment.initiate');
    });


    // Student Routes
    Route::middleware(['role:Student'])->prefix('student')->name('student.')->group(function () {
        Route::get('/dashboard', [\App\Http\Controllers\Student\DashboardController::class, 'index'])->name('dashboard');
        Route::get('/registration', [\App\Http\Controllers\Student\DashboardController::class, 'registration'])->name('registration');
        Route::get('/payments', [\App\Http\Controllers\Student\DashboardController::class, 'payments'])->name('payments');
        Route::get('/payments/statement', [\App\Http\Controllers\Student\DashboardController::class, 'statement'])->name('payments.statement');
        Route::post('/semester/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerSemester'])->name('semester.register');
        Route::post('/courses/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerCourses'])->name('courses.register');
        Route::get('/courses/slip', [\App\Http\Controllers\Student\DashboardController::class, 'printSlip'])->name('courses.slip');
        Route::get('/results', [\App\Http\Controllers\Student\DashboardController::class, 'results'])->name('results');
        Route::get('/id-card', [\App\Http\Controllers\Student\DashboardController::class, 'idCard'])->name('idcard');
    });

    // Admin Routes
    Route::middleware('role:Super Admin')->prefix('admin')->name('admin.')->group(function () {
        Route::get('/dashboard', [AdminDashboardController::class, 'index'])->name('dashboard');
        Route::get('/applications', [AdminApplicationController::class, 'index'])->name('applications.index');
        Route::get('/applications/export', [AdminApplicationController::class, 'export'])->name('applications.export');
        Route::get('/applications/{application}', [AdminApplicationController::class, 'show'])->name('applications.show');
        Route::post('/applications/{application}/status', [AdminApplicationController::class, 'updateStatus'])->name('applications.updateStatus');
        
        // Settings / Academics routes
        Route::get('/programmes', [ProgrammeController::class, 'index'])->name('programmes.index');
        Route::get('/programmes/create', [ProgrammeController::class, 'create'])->name('programmes.create');
        Route::post('/programmes', [ProgrammeController::class, 'store'])->name('programmes.store');
        Route::get('/programmes/{programme}', [ProgrammeController::class, 'show'])->name('programmes.show');
        Route::post('/programmes/{programme}/courses', [ProgrammeController::class, 'attachCourse'])->name('programmes.courses.attach');
        Route::delete('/programmes/{programme}/courses/{course}', [ProgrammeController::class, 'detachCourse'])->name('programmes.courses.detach');
        Route::patch('/programmes/{programme}/toggle-status', [ProgrammeController::class, 'toggleStatus'])->name('programmes.toggle-status');

        Route::get('/specialisations/{specialisation}', [\App\Http\Controllers\Admin\SpecialisationController::class, 'show'])->name('specialisations.show');
        Route::post('/specialisations/{specialisation}/courses', [\App\Http\Controllers\Admin\SpecialisationController::class, 'attachCourse'])->name('specialisations.courses.attach');
        Route::delete('/specialisations/{specialisation}/courses/{course}', [\App\Http\Controllers\Admin\SpecialisationController::class, 'detachCourse'])->name('specialisations.courses.detach');
        Route::get('/users', [UsersController::class, 'index'])->name('users.index');
        Route::get('/users/{user}', [UsersController::class, 'show'])->name('users.show');
        Route::delete('/users/{user}', [UsersController::class, 'destroy'])->name('users.destroy');
        Route::get('/courses', [CourseController::class, 'index'])->name('courses.index');
        Route::get('/courses/create', [CourseController::class, 'create'])->name('courses.create');
        Route::post('/courses', [CourseController::class, 'store'])->name('courses.store');
        
        Route::get('/sessions', [AcademicSessionController::class, 'index'])->name('sessions.index');
        Route::post('/sessions', [AcademicSessionController::class, 'store'])->name('sessions.store');
        Route::post('/sessions/{session}/activate', [AcademicSessionController::class, 'activate'])->name('sessions.activate');
        Route::post('/sessions/{session}/advance-semester', [AcademicSessionController::class, 'advanceSemester'])->name('sessions.advance-semester');
        Route::post('/sessions/{session}/toggle-registration', [AcademicSessionController::class, 'toggleRegistration'])->name('sessions.toggle-registration');
        Route::put('/sessions/{session}', [AcademicSessionController::class, 'update'])->name('sessions.update');
        Route::delete('/sessions/{session}', [AcademicSessionController::class, 'destroy'])->name('sessions.destroy');
        
        Route::get('/results/upload', [\App\Http\Controllers\Admin\ResultController::class, 'create'])->name('results.upload');
        Route::post('/results/upload', [\App\Http\Controllers\Admin\ResultController::class, 'store'])->name('results.store');
        
        Route::get('/payments', [AdminPaymentController::class, 'index'])->name('payments.index');
    });
});

require __DIR__.'/auth.php';
