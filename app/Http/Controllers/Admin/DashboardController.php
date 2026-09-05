<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Application;
use App\Models\Payment;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Illuminate\Support\Facades\DB;

class DashboardController extends Controller
{
    public function index()
    {
        $stats = [
            'total_applications' => Application::count(),
            'under_review' => Application::whereIn('status', ['UNDER REVIEW', 'SCREENING', 'SHORTLISTED'])->count(),
            'admitted' => Application::where('status', 'ADMITTED')->count(),
            'enrolled' => Application::where('status', 'ENROLLED')->count(),
            'total_revenue' => Payment::whereIn('status', ['PAID', 'SUCCESSFUL'])->sum('amount'),
        ];

        $recent_applications = Application::with(['user', 'programme'])
            ->latest()
            ->take(6)
            ->get();

        $applications_by_programme = Application::join('programmes', 'applications.programme_id', '=', 'programmes.id')
            ->select('programmes.name', DB::raw('count(*) as total'))
            ->groupBy('programmes.name')
            ->orderByDesc('total')
            ->take(5)
            ->get();

        return Inertia::render('Admin/Dashboard', [
            'stats' => $stats,
            'recent_applications' => $recent_applications,
            'applications_by_programme' => $applications_by_programme
        ]);
    }
}
