<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\RemitaService;
use App\Models\Payment;
use Illuminate\Support\Facades\Log;
use Inertia\Inertia;

class PaymentController extends Controller
{
    /**
     * Initiate a payment.
     */
    public function initiate(Request $request, RemitaService $remita)
    {
        $request->validate([
            'type' => 'nullable|string|in:APPLICATION_FEE,ACCEPTANCE_FEE,TUITION,WALLET_TOPUP'
        ]);

        $type = $request->input('type', 'APPLICATION_FEE');
        $application = $request->user()->applications()->latest()->first();

        // Determine Amount
        $amount = 25000.00;
        if ($type === 'ACCEPTANCE_FEE') {
            $amount = 50000.00;
        } elseif ($type === 'TUITION') {
            $amount = 250000.00;
        } elseif ($type === 'WALLET_TOPUP') {
            $amount = $request->input('amount');
        }

        $payment = Payment::create([
            'user_id' => $request->user()->id,
            'application_id' => $application ? $application->id : null,
            'payment_type' => $type,
            'amount' => $amount,
            'transaction_reference' => 'NBS-' . strtoupper(uniqid()),
            'status' => 'PENDING',
        ]);

        // Generate RRR
        $rrr = $remita->generateRRR($payment);

        return redirect()->route('remita.gateway', ['rrr' => $rrr]);
    }

    /**
     * Simulated Remita Gateway Page
     */
    public function gateway(Request $request)
    {
        $rrr = $request->query('rrr');
        $payment = Payment::where('rrr', $rrr)->with('user')->firstOrFail();
        
        return Inertia::render('Remita/Gateway', [
            'payment' => $payment
        ]);
    }

    /**
     * Simulated Remita Payment Action
     */
    public function simulatePay(Request $request, RemitaService $remita)
    {
        $rrr = $request->input('rrr');
        $payment = Payment::where('rrr', $rrr)->firstOrFail();

        // Simulate Remita verifying the payment internally
        $payment->update([
            'status' => 'PAID',
            'paid_at' => now(),
            'remita_transaction_id' => 'REM-' . rand(100000, 999999)
        ]);
        
        if ($payment->payment_type === 'APPLICATION_FEE' && $payment->application) {
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
        }

        return redirect()->route('dashboard')->with('success', 'Payment processed successfully via Remita!');
    }

    /**
     * Handle incoming Remita Webhook
     */
    public function webhook(Request $request, RemitaService $remita)
    {
        Log::info('Remita Webhook Received', $request->all());

        $payment = Payment::where('rrr', $request->input('rrr'))->first();

        if ($payment) {
            $remita->processWebhook($request->all());
            
            if ($payment->payment_type === 'APPLICATION_FEE') {
                $payment->application->update(['status' => 'SUBMITTED']);
            } elseif ($payment->payment_type === 'ACCEPTANCE_FEE') {
                $payment->application->update(['status' => 'ENROLLED']);
                if (!$payment->user->hasRole('Student')) {
                    $payment->user->assignRole('Student');
                }
            }
            
            return response()->json(['status' => 'success', 'message' => 'Payment processed']);
        }

        return response()->json(['status' => 'error', 'message' => 'Transaction not found'], 404);
    }
}
