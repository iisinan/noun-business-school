<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Auth\Events\Registered;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\Rules;
use Illuminate\Validation\ValidationException;
use Inertia\Inertia;
use Inertia\Response;

use Illuminate\Support\Str;

class RegisteredUserController extends Controller
{
    /**
     * Display the registration view.
     */
    public function create(): Response
    {
        return Inertia::render('Auth/Register');
    }

    /**
     * Handle an incoming registration request.
     *
     * @throws ValidationException
     */
    public function store(Request $request): RedirectResponse
    {
        $request->validate([
            'first_name' => 'required|string|max:255',
            'middle_name' => 'nullable|string|max:255',
            'last_name' => 'required|string|max:255',
            'phone' => 'required|string|max:20',
            'email' => 'required|string|lowercase|email|max:255|unique:'.User::class,
            'referral_code' => 'nullable|string|exists:users,personal_referral_code',
            'password' => ['required', 'confirmed', Rules\Password::defaults()],
        ], [
            'referral_code.exists' => 'The provided referral code is invalid.',
        ]);

        $user = User::create([
            'first_name' => $request->first_name,
            'middle_name' => $request->middle_name,
            'last_name' => $request->last_name,
            'phone' => $request->phone,
            'email' => $request->email,
            'referral_code' => $request->referral_code,
            'personal_referral_code' => strtoupper(substr(preg_replace('/[^A-Za-z]/', '', $request->first_name), 0, 3)) . rand(1000, 9999),
            'password' => Hash::make($request->password),
        ]);

        $user->assignRole('Applicant');

        // Dispatching Registered event sends the verification email automatically
        event(new Registered($user));

        Auth::login($user);

        // Store programme/specialisation in session so it survives email verification
        if ($request->filled('programme_id')) {
            session(['preselected_programme' => $request->programme_id]);
            if ($request->filled('specialisation_id')) {
                session(['preselected_specialisation' => $request->specialisation_id]);
            }
        }

        // Redirect directly to the verify-email notice screen
        return redirect()->route('verification.notice');
    }
}
