import os

# Update routes/web.php
web_file = "routes/web.php"
with open(web_file, "r") as f:
    web_content = f.read()

closure_old = """    Route::get('/dashboard', function () {
        if (auth()->user()->hasRole('Super Admin')) {
            return redirect()->route('admin.dashboard');
        }
        if (auth()->user()->hasRole('Student')) {
            return redirect()->route('student.dashboard');
        }
        $latestApplication = auth()->user()->applications()->with('programme')->latest()->first();
        return Inertia::render('Applicant/Dashboard', [
            'application' => $latestApplication,
        ]);
    })->name('dashboard');"""

closure_new = """    Route::get('/dashboard', function () {
        if (auth()->user()->hasRole('Super Admin')) {
            return redirect()->route('admin.dashboard');
        }
        
        $user = auth()->user();
        $latestApplication = $user->applications()->with('programme', 'specialisation')->latest()->first();

        // If enrolled student, get student dashboard data
        if ($user->hasRole('Student')) {
            $activeSession = \\App\\Models\\AcademicSession::where('is_active', true)->first();
            
            $hasRegisteredSemester = false;
            $registeredCourses = [];
            $availableCourses = [];
            
            if ($activeSession) {
                $hasRegisteredSemester = \\App\\Models\\SemesterRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->exists();
                
                if ($hasRegisteredSemester) {
                    $registeredCourseIds = \\App\\Models\\CourseRegistration::where('user_id', $user->id)
                        ->where('academic_session_id', $activeSession->id)
                        ->pluck('course_id')
                        ->toArray();
    
                    $registeredCourses = \\App\\Models\\Course::whereIn('id', $registeredCourseIds)->get();
    
                    if ($latestApplication && $latestApplication->programme_id) {
                        $availableCourses = $latestApplication->programme->courses()
                            ->whereNotIn('courses.id', $registeredCourseIds)
                            ->get();
                    } else {
                        $availableCourses = \\App\\Models\\Course::whereNotIn('id', $registeredCourseIds)->get();
                    }
                }
            }
            
            $transactions = \\App\\Models\\WalletTransaction::where('user_id', $user->id)->latest()->take(10)->get();

            return Inertia::render('Applicant/Dashboard', [
                'application' => $latestApplication,
                'is_student' => true,
                'wallet_balance' => (float) $user->wallet_balance,
                'transactions' => $transactions,
                'activeSession' => $activeSession,
                'hasRegisteredSemester' => $hasRegisteredSemester,
                'registeredCourses' => $registeredCourses,
                'availableCourses' => $availableCourses,
            ]);
        }

        return Inertia::render('Applicant/Dashboard', [
            'application' => $latestApplication,
            'is_student' => false
        ]);
    })->name('dashboard');"""

web_content = web_content.replace(closure_old, closure_new)

# Remove the GET route for student dashboard to avoid conflict if any, although not needed.
web_content = web_content.replace(
    "Route::get('/dashboard', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'index'])->name('dashboard');",
    "// Route::get('/dashboard', [\\App\\Http\\Controllers\\Student\\DashboardController::class, 'index'])->name('dashboard');"
)

with open(web_file, "w") as f:
    f.write(web_content)

print("routes/web.php updated.")
