<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Models\Referee;
use Inertia\Inertia;

class RefereeController extends Controller
{
    public function show($token)
    {
        $referee = Referee::with(['application.user', 'application.programme'])->where('token', $token)->firstOrFail();

        if ($referee->status === 'SUBMITTED') {
            return Inertia::render('Referee/Submitted');
        }

        return Inertia::render('Referee/Form', [
            'referee' => $referee
        ]);
    }

    public function store(Request $request, $token)
    {
        $referee = Referee::where('token', $token)->firstOrFail();

        if ($referee->status === 'SUBMITTED') {
            return back()->with('error', 'Reference has already been submitted.');
        }

        $request->validate([
            'reference_content' => 'required|string|min:50',
        ]);

        $referee->update([
            'reference_content' => $request->reference_content,
            'status' => 'SUBMITTED'
        ]);

        return redirect()->route('referee.submitted')->with('success', 'Reference submitted successfully.');
    }

    public function submitted()
    {
        return Inertia::render('Referee/Submitted');
    }
}
