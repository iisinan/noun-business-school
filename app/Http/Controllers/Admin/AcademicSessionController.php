<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\AcademicSession;
use Illuminate\Http\Request;
use Inertia\Inertia;

class AcademicSessionController extends Controller
{
    public function index()
    {
        $sessions = AcademicSession::withCount([
            'applications as total_applications',
            'applications as enrolled_students' => function($query) {
                $query->where('status', 'ENROLLED');
            }
        ])->latest()->get();
        
        return Inertia::render('Admin/Sessions/Index', [
            'sessions' => $sessions
        ]);
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required|string|unique:academic_sessions,name',
            'is_active' => 'boolean'
        ]);

        if ($request->is_active) {
            // Deactivate all others
            AcademicSession::query()->update(['is_active' => false]);
        }

        AcademicSession::create([
            'name' => $request->name,
            'is_active' => $request->is_active ?? false
        ]);

        return redirect()->route('admin.sessions.index')->with('success', 'Session created successfully.');
    }

    public function activate(AcademicSession $session)
    {
        AcademicSession::query()->update(['is_active' => false]);
        $session->update(['is_active' => true]);

        return redirect()->route('admin.sessions.index')->with('success', 'Session activated successfully.');
    }

    public function advanceSemester(AcademicSession $session)
    {
        // Increment all students' semesters
        $students = \App\Models\User::role('Student')->get();
        foreach ($students as $student) {
            $student->increment('current_semester');
        }

        if ($session->current_semester >= 2) {
            // Find or create next session
            $nextSessionName = $session->name . ' (Next)';
            if (preg_match('/^(\d{4})\/(\d{4})$/', $session->name, $matches)) {
                $year1 = (int)$matches[1] + 1;
                $year2 = (int)$matches[2] + 1;
                $nextSessionName = "$year1/$year2";
            }

            $nextSession = AcademicSession::firstOrCreate(
                ['name' => $nextSessionName],
                ['is_active' => false]
            );

            // Deactivate current
            $session->update(['is_active' => false]);
            
            // Activate next
            $nextSession->update([
                'is_active' => true,
                'current_semester' => 1,
                'registration_open' => true,
            ]);

            return redirect()->route('admin.sessions.index')->with('success', 'Advanced to Semester 1 of ' . $nextSessionName . '. All students have been moved to their next semester.');
        } else {
            $session->update([
                'current_semester' => $session->current_semester + 1,
                'registration_open' => true,
            ]);

            return redirect()->route('admin.sessions.index')->with('success', 'Advanced to Semester ' . $session->current_semester . '. All students have been moved to their next semester.');
        }
    }

    public function toggleRegistration(AcademicSession $session)
    {
        $session->update([
            'registration_open' => !$session->registration_open
        ]);

        $status = $session->registration_open ? 'opened' : 'closed';
        return redirect()->route('admin.sessions.index')->with('success', "Registration has been {$status} for Semester {$session->current_semester}.");
    }

    public function update(Request $request, AcademicSession $session)
    {
        $request->validate([
            'name' => 'required|string|unique:academic_sessions,name,' . $session->id,
        ]);

        $session->update(['name' => $request->name]);
        return redirect()->route('admin.sessions.index')->with('success', 'Session updated successfully.');
    }

    public function destroy(AcademicSession $session)
    {
        if ($session->is_active) {
            return back()->with('error', 'Cannot delete the currently active session.');
        }

        if ($session->applications()->count() > 0) {
            return back()->with('error', 'Cannot delete a session that already has applications attached to it.');
        }

        $session->delete();
        return redirect()->route('admin.sessions.index')->with('success', 'Session deleted successfully.');
    }
}