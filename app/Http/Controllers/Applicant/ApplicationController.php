<?php

namespace App\Http\Controllers\Applicant;

use App\Http\Controllers\Controller;
use App\Models\Programme;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ApplicationController extends Controller
{
    /**
     * Show the application form.
     */
    public function create(Request $request)
    {
        // Load programmes and their specialisations/requirements
        $programmes = Programme::with(['specialisations', 'admissionRequirements'])->where('is_active', true)->get();

        $preselectedProgramme = $request->query('programme_id') ?? session('preselected_programme');
        $preselectedSpecialisation = $request->query('specialisation_id') ?? session('preselected_specialisation');

        return Inertia::render('Applicant/ApplicationForm', [
            'programmes' => $programmes,
            'active_session' => \App\Models\AcademicSession::where('is_active', true)->first(),
            'preselected_programme' => $preselectedProgramme ? (int)$preselectedProgramme : null,
            'preselected_specialisation' => $preselectedSpecialisation ? (int)$preselectedSpecialisation : null,
        ]);
    }

    /**
     * Store the submitted application.
     */
    public function store(Request $request)
    {
        $fileErrors = [];
        $passport = $request->file('passport_photograph');
        if ($passport) {
            $fileErrors['passport'] = $passport->getError();
        }
        $docs = $request->file('documents');
        if ($docs) {
            foreach ($docs as $key => $files) {
                if (is_array($files)) {
                    foreach ($files as $i => $file) {
                        $fileErrors["doc_{$key}_{$i}"] = $file->getError();
                    }
                }
            }
        }
        \Log::info('FILE ERRORS', $fileErrors);
        \Log::info('UPLOAD_MAX_FILESIZE', ['size' => ini_get('upload_max_filesize')]);
        \Log::info('POST_MAX_SIZE', ['size' => ini_get('post_max_size')]);
        \Log::info('UPLOAD_TMP_DIR', ['dir' => ini_get('upload_tmp_dir') ?: sys_get_temp_dir()]);
        \Log::info('STORE PAYLOAD', $request->all());
        try {
            $validated = $request->validate([
            'programme_id' => 'required|exists:programmes,id',
            'specialisation_id' => 'nullable|exists:specialisations,id',
            'personal_info' => 'required|array',
            'academic_background' => 'required|array',
            'olevel_results' => 'required|array',
            'employment_info' => 'required|array',
            'passport_photograph' => 'required|image|max:2048', // 2MB passport photo
            // Documents are passed as files
            'documents' => 'required|array',
            'documents.*' => 'required|array',
            'documents.*.*' => 'file|mimes:pdf,jpg,jpeg,png|max:5120', // 5MB limit
        ]);
        } catch (\Illuminate\Validation\ValidationException $e) {
            \Log::error('VALIDATION FAILED', $e->errors());
            throw $e;
        }

        $session = \App\Models\AcademicSession::where('is_active', true)->firstOrFail();

        // Handle document uploads
        $documentPaths = [];
        $documents = $request->file('documents');
        if (!empty($documents)) {
            foreach ($documents as $key => $fileOrFiles) {
                if (is_array($fileOrFiles)) {
                    $paths = [];
                    foreach ($fileOrFiles as $f) {
                        $paths[] = $f->store('applications/documents', 's3');
                    }
                    $documentPaths[$key] = $paths;
                } else {
                    $documentPaths[$key] = $fileOrFiles->store('applications/documents', 's3');
                }
            }
        }

        // Handle passport upload
        $personalInfo = $validated['personal_info'];
        if ($request->hasFile('passport_photograph')) {
            $personalInfo['passport_photograph_path'] = $request->file('passport_photograph')->store('applications/passports', 's3');
        }

        // Generate application number
        $applicationNumber = 'APP/' . date('Y') . '/' . str_pad(rand(1, 99999), 5, '0', STR_PAD_LEFT);

        $application = $request->user()->applications()->create([
            'academic_session_id' => $session->id,
            'programme_id' => $validated['programme_id'],
            'specialisation_id' => $validated['specialisation_id'] ?? null,
            'application_number' => $applicationNumber,
            'personal_info' => $personalInfo,
            'academic_background' => $validated['academic_background'],
            'olevel_results' => $validated['olevel_results'],
            'employment_info' => $validated['employment_info'],
            'documents' => $documentPaths,
            'status' => 'STARTED', // Set to started, pending payment
        ]);

        try {
            \Illuminate\Support\Facades\Mail::to($request->user())->send(new \App\Mail\ApplicationSubmittedMail($application));
        } catch (\Exception $e) {
            \Log::error('Failed to send application submitted mail: ' . $e->getMessage());
        }

        return redirect()->route('dashboard')->with('success', 'Application drafted successfully. Please proceed to pay the application fee.');
    }

    /**
     * Generate the Application Docket (Printable HTML).
     */
    public function docket(Request $request)
    {
        $application = $request->user()->applications()->with(['programme', 'specialisation', 'academicSession'])->latest()->firstOrFail();
        return view('applicant.application-docket', compact('application'));
    }

    /**
     * Generate the Admission Letter (Printable HTML).
     */
    public function letter(Request $request)
    {
        $application = $request->user()->applications()->with(['programme', 'specialisation', 'academicSession'])->where('status', 'ENROLLED')->latest()->firstOrFail();
        return view('applicant.admission-letter', compact('application'));
    }
}
