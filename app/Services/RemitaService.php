<?php

namespace App\Services;

use App\Models\Payment;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Str;

class RemitaService
{
    protected string $merchantId;
    protected string $apiKey;
    protected string $environmentUrl;

    public function __construct()
    {
        $this->merchantId = config('services.remita.merchant_id', 'DEMO_MERCHANT');
        $this->apiKey = config('services.remita.api_key', 'DEMO_API_KEY');
        $this->environmentUrl = config('services.remita.env_url', 'https://remitademo.net/remita/exapp/api/v1/send/api');
    }

    /**
     * Generate a Remita Retrieval Reference (RRR) for a payment.
     */
    public function generateRRR(Payment $payment): ?string
    {
        // Mock generation for the scope of the implementation plan
        // In production, this makes a POST request to Remita's /echannelsvc/merchant/api/paymentinit endpoint
        
        $payment->update([
            'rrr' => '123456789' . rand(100, 999),
            'transaction_reference' => 'TXN-' . Str::uuid()->toString(),
        ]);

        return $payment->rrr;
    }

    /**
     * Verify a payment status with Remita.
     */
    public function verifyPayment(Payment $payment): bool
    {
        // Mock verification
        // In production, this makes a GET request to /echannelsvc/{merchantId}/{transactionReference}/{hash}/status.reg
        
        if ($payment->status === 'PENDING') {
            $payment->update([
                'status' => 'SUCCESSFUL',
                'remita_transaction_id' => 'REM-' . rand(100000, 999999),
                'paid_at' => now(),
                'verified_at' => now(),
            ]);
            return true;
        }

        return $payment->status === 'SUCCESSFUL';
    }

    /**
     * Process asynchronous callback/webhook from Remita.
     */
    public function processWebhook(array $payload): bool
    {
        // Verify hash from payload
        // Locate payment by RRR or Reference
        // Update status to SUCCESSFUL
        return true;
    }
}
