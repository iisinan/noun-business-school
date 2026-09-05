with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = "    public function results(Request $request)"
replacement = """    public function statement(Request $request)
    {
        $user = $request->user();

        $walletTransactions = \\App\\Models\\WalletTransaction::where('user_id', $user->id)
            ->oldest() // chronological order for a statement
            ->get();
            
        $application = $user->applications()->where('status', 'ENROLLED')->latest()->first();

        return Inertia::render('Student/Statement', [
            'user' => $user,
            'application' => $application,
            'walletTransactions' => $walletTransactions,
            'wallet_balance' => (float) $user->wallet_balance,
        ]);
    }

    public function results(Request $request)"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
    f.write(content)
