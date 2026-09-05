<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Payment;
use Illuminate\Http\Request;
use Inertia\Inertia;

class PaymentController extends Controller
{
    public function index(Request $request)
    {
        $query = Payment::with(['user', 'application.programme']);

        if ($request->has('search') && $request->search != '') {
            $search = $request->search;
            $query->where('transaction_reference', 'like', "%{$search}%")
                  ->orWhere('rrr', 'like', "%{$search}%")
                  ->orWhereHas('user', function($q) use ($search) {
                      $q->where('first_name', 'like', "%{$search}%")
                        ->orWhere('last_name', 'like', "%{$search}%");
                  });
        }

        if ($request->has('status') && $request->status != '') {
            $query->where('status', $request->status);
        }

        $payments = $query->latest()->paginate(20)->withQueryString();

        $stats = [
            'total_revenue' => Payment::whereIn('status', ['PAID', 'SUCCESSFUL'])->sum('amount'),
            'total_transactions' => Payment::whereIn('status', ['PAID', 'SUCCESSFUL'])->count(),
            'pending_amount' => Payment::where('status', 'PENDING')->sum('amount'),
        ];

        return Inertia::render('Admin/Payments/Index', [
            'payments' => $payments,
            'filters' => $request->only(['search', 'status']),
            'stats' => $stats
        ]);
    }
}
