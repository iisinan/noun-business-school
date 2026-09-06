<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Inertia\Inertia;

class UsersController extends Controller
{
    public function index(Request $request)
    {
        $query = User::with('roles');

        if ($request->has('search') && $request->search != '') {
            $search = $request->search;
            $query->where('first_name', 'like', "%{$search}%")
                  ->orWhere('last_name', 'like', "%{$search}%")
                  ->orWhere('email', 'like', "%{$search}%");
        }

        if ($request->has('role') && $request->role != '') {
            $query->role($request->role);
        }

        $users = $query->latest()->paginate(20)->withQueryString();

        return Inertia::render('Admin/Users/Index', [
            'users' => $users,
            'filters' => $request->only(['search', 'role'])
        ]);
    }

    public function show(User $user)
    {
        $user->load([
            'roles', 
            'walletTransactions' => function($q) { $q->latest(); },
            'semesterRegistrations.academicSession',
            'courseRegistrations.course',
            'courseRegistrations.academicSession'
        ]);

        $userData = $user->toArray();
        $app = \App\Models\Application::where('user_id', $user->id)->latest()->first();
        if ($app && isset($app->personal_info['passport_photograph_path'])) {
            $userData['passport_url'] = \Illuminate\Support\Facades\Storage::disk('s3')->url($app->personal_info['passport_photograph_path']);
        }

        return Inertia::render('Admin/Users/Show', [
            'user' => $userData,
        ]);
    }

    public function destroy(User $user)
    {
        // Don't allow super admin to delete themselves
        if (auth()->id() === $user->id) {
            return back()->with('error', 'You cannot delete yourself.');
        }

        $user->delete();

        return redirect()->route('admin.users.index')->with('success', 'User deleted successfully.');
    }
}
