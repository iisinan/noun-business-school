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

        return Inertia::render('Admin/Users/Show', [
            'user' => $user,
        ]);
    }
}
