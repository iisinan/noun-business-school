import os

# Update PaymentController.php
pc_file = "app/Http/Controllers/PaymentController.php"
with open(pc_file, "r") as f:
    pc_content = f.read()

# Add WALLET_TOPUP validation
pc_content = pc_content.replace(
    "'type' => 'nullable|string|in:APPLICATION_FEE,ACCEPTANCE_FEE,TUITION'",
    "'type' => 'nullable|string|in:APPLICATION_FEE,ACCEPTANCE_FEE,TUITION,WALLET_TOPUP'"
)

# Update Amount logic
amount_logic_old = """        $type = $request->input('type', 'APPLICATION_FEE');
        $application = $request->user()->applications()->latest()->firstOrFail();

        // Determine Amount
        $amount = 25000.00;
        if ($type === 'ACCEPTANCE_FEE') {
            $amount = 50000.00;
        } elseif ($type === 'TUITION') {
            $amount = 250000.00; // Just as an example
        }"""
amount_logic_new = """        $type = $request->input('type', 'APPLICATION_FEE');
        $application = $request->user()->applications()->latest()->first();

        // Determine Amount
        $amount = 25000.00;
        if ($type === 'ACCEPTANCE_FEE') {
            $amount = 50000.00;
        } elseif ($type === 'TUITION') {
            $amount = 250000.00;
        } elseif ($type === 'WALLET_TOPUP') {
            $amount = $request->input('amount');
        }"""
pc_content = pc_content.replace(amount_logic_old, amount_logic_new)

# Update application_id nullability in Payment create
payment_create_old = """        $payment = Payment::create([
            'user_id' => $request->user()->id,
            'application_id' => $application->id,
            'payment_type' => $type,
            'amount' => $amount,
            'transaction_reference' => 'NBS-' . strtoupper(uniqid()),
            'status' => 'PENDING',
        ]);"""
payment_create_new = """        $payment = Payment::create([
            'user_id' => $request->user()->id,
            'application_id' => $application ? $application->id : null,
            'payment_type' => $type,
            'amount' => $amount,
            'transaction_reference' => 'NBS-' . strtoupper(uniqid()),
            'status' => 'PENDING',
        ]);"""
pc_content = pc_content.replace(payment_create_old, payment_create_new)

# Update simulatePay webhook logic
simulate_pay_old = """        if ($payment->payment_type === 'APPLICATION_FEE') {
            $payment->application->update(['status' => 'SUBMITTED']);
        } elseif ($payment->payment_type === 'ACCEPTANCE_FEE') {
            $payment->application->update(['status' => 'ENROLLED']);
            // Automatically assign role Student
            if (!$payment->user->hasRole('Student')) {
                $payment->user->assignRole('Student');
            }
        }"""
simulate_pay_new = """        if ($payment->payment_type === 'APPLICATION_FEE' && $payment->application) {
            $payment->application->update(['status' => 'SUBMITTED']);
        } elseif ($payment->payment_type === 'ACCEPTANCE_FEE' && $payment->application) {
            $payment->application->update(['status' => 'ENROLLED']);
            // Automatically assign role Student
            if (!$payment->user->hasRole('Student')) {
                $payment->user->assignRole('Student');
            }
        } elseif ($payment->payment_type === 'WALLET_TOPUP') {
            $user = $payment->user;
            $user->wallet_balance += $payment->amount;
            $user->save();

            \App\Models\WalletTransaction::create([
                'user_id' => $user->id,
                'type' => 'topup',
                'amount' => $payment->amount,
                'description' => 'Wallet Topup via Remita',
                'reference_id' => $payment->id
            ]);
        }"""
pc_content = pc_content.replace(simulate_pay_old, simulate_pay_new)

with open(pc_file, "w") as f:
    f.write(pc_content)

# Update routes/web.php
web_file = "routes/web.php"
with open(web_file, "r") as f:
    web_content = f.read()

dashboard_old = """    // Dashboard redirection based on role
    Route::get('/dashboard', function () {
        if (auth()->user()->hasRole('Super Admin')) {
            return redirect()->route('admin.dashboard');
        }
        $latestApplication = auth()->user()->applications()->with('programme')->latest()->first();
        return Inertia::render('Applicant/Dashboard', [
            'application' => $latestApplication,
        ]);
    })->name('dashboard');"""
dashboard_new = """    // Dashboard redirection based on role
    Route::get('/dashboard', function () {
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
web_content = web_content.replace(dashboard_old, dashboard_new)

student_routes = """
    // Student Routes
    Route::middleware(['role:Student'])->prefix('student')->name('student.')->group(function () {
        Route::get('/dashboard', [\App\Http\Controllers\Student\DashboardController::class, 'index'])->name('dashboard');
        Route::post('/semester/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerSemester'])->name('semester.register');
        Route::post('/courses/register', [\App\Http\Controllers\Student\DashboardController::class, 'registerCourses'])->name('courses.register');
    });

    // Admin Routes"""
web_content = web_content.replace("    // Admin Routes", student_routes)

with open(web_file, "w") as f:
    f.write(web_content)

print("PaymentController and web.php updated.")
