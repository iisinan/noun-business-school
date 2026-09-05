with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = "    public function registration(Request $request)"
replacement = """    public function payments(Request $request)
    {
        $user = $request->user();
        
        $walletTransactions = \\App\\Models\\WalletTransaction::where('user_id', $user->id)
            ->latest()
            ->get();
            
        $gatewayPayments = \\App\\Models\\Payment::where('user_id', $user->id)
            ->latest()
            ->get();

        return Inertia::render('Student/Payments', [
            'wallet_balance' => (float) $user->wallet_balance,
            'walletTransactions' => $walletTransactions,
            'gatewayPayments' => $gatewayPayments,
        ]);
    }

    public function registration(Request $request)"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
    f.write(content)
