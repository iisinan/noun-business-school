<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Auth\Events\Verified;
use Illuminate\Foundation\Auth\EmailVerificationRequest;
use Illuminate\Http\RedirectResponse;

class VerifyEmailController extends Controller
{
    /**
     * Mark the authenticated user's email address as verified.
     */
    public function __invoke(EmailVerificationRequest $request): RedirectResponse
    {
        if ($request->user()->hasVerifiedEmail()) {
            return $this->redirectAfterVerification();
        }

        if ($request->user()->markEmailAsVerified()) {
            event(new Verified($request->user()));
        }

        return $this->redirectAfterVerification();
    }

    protected function redirectAfterVerification(): RedirectResponse
    {
        // If the user was on their way to apply for a specific programme, send them there
        if (session()->has('preselected_programme')) {
            return redirect()->route('applicant.application.create')
                ->with('success', 'Email verified! You can now complete your application.');
        }

        return redirect()->route('dashboard')
            ->with('success', 'Email verified! Welcome to NOUN Business School.');
    }
}
