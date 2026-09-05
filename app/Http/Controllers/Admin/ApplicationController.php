<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Application;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ApplicationController extends Controller
{
    /**
     * Display the DataTables list of all applications.
     */
    public function index(\Illuminate\Http\Request $request)
    {
        $query = Application::with('user', 'programme')->latest();

        if ($request->filled('search')) {
            $searchTerm = $request->search;
            $query->where(function ($q) use ($searchTerm) {
                $q->where('application_number', 'like', "%{$searchTerm}%")
                  ->orWhereHas('user', function ($uq) use ($searchTerm) {
                      $uq->where('first_name', 'like', "%{$searchTerm}%")
                         ->orWhere('last_name', 'like', "%{$searchTerm}%")
                         ->orWhere('email', 'like', "%{$searchTerm}%");
                  });
            });
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        if ($request->filled('programme_id')) {
            $query->where('programme_id', $request->programme_id);
        }

        $applications = $query->paginate(20)->withQueryString();
        
        $programmes = \App\Models\Programme::select('id', 'name')->orderBy('name')->get();

        return Inertia::render('Admin/Applications/Index', [
            'applications' => $applications,
            'programmes' => $programmes,
            'filters' => $request->only(['search', 'status', 'programme_id'])
        ]);
    }

    /**
     * Export applications to CSV.
     */
    public function export()
    {
        $applications = Application::with('user', 'programme', 'specialisation')->get();

        $headers = [
            "Content-type"        => "text/csv",
            "Content-Disposition" => "attachment; filename=applications_" . date('Y-m-d') . ".csv",
            "Pragma"              => "no-cache",
            "Cache-Control"       => "must-revalidate, post-check=0, pre-check=0",
            "Expires"             => "0"
        ];

        $columns = ['Application No', 'First Name', 'Last Name', 'Email', 'Phone', 'Programme', 'Specialisation', 'Status', 'Date Submitted'];

        $callback = function() use($applications, $columns) {
            $file = fopen('php://output', 'w');
            fputcsv($file, $columns);

            foreach ($applications as $app) {
                fputcsv($file, [
                    $app->application_number,
                    $app->user->first_name ?? '',
                    $app->user->last_name ?? '',
                    $app->user->email ?? '',
                    $app->user->phone ?? '',
                    $app->programme->name ?? '',
                    $app->specialisation->name ?? '',
                    $app->status,
                    $app->created_at->format('Y-m-d H:i:s')
                ]);
            }

            fclose($file);
        };

        return response()->stream($callback, 200, $headers);
    }

    /**
     * Show the detailed review interface for a single application.
     */
    public function show(Application $application)
    {
        $application->load('user', 'programme', 'specialisation', 'payments');
        
        $documentUrls = [];
        if (is_array($application->documents)) {
            foreach ($application->documents as $key => $path) {
                if (is_array($path)) {
                    $documentUrls[$key] = array_map(fn($p) => \Illuminate\Support\Facades\Storage::disk('s3')->url($p), $path);
                } else {
                    $documentUrls[$key] = \Illuminate\Support\Facades\Storage::disk('s3')->url($path);
                }
            }
        }
        
        $appData = $application->toArray();
        $appData['document_urls'] = $documentUrls;

        return Inertia::render('Admin/Applications/Show', [
            'application' => $appData
        ]);
    }

    /**
     * Update the workflow status of an application.
     */
    public function updateStatus(Request $request, Application $application)
    {
        $validated = $request->validate([
            'status' => 'required|in:UNDER REVIEW,ADMITTED,REJECTED'
        ]);

        $application->update(['status' => $validated['status']]);

        if ($validated['status'] === 'ADMITTED') {
            // AdmissionLetterService::generate($application);
            // $application->user->notify(new AdmissionOffered($application));
        }

        return redirect()->back()->with('success', 'Application status updated to ' . $validated['status']);
    }
}
