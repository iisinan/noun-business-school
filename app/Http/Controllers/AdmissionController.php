<?php

namespace App\Http\Controllers;

use App\Models\Programme;
use Illuminate\Http\Request;
use Inertia\Inertia;

class AdmissionController extends Controller
{
    public function start()
    {
        $programmes = Programme::with(['specialisations', 'admissionRequirements'])->where('is_active', true)->get();

        return Inertia::render('Admission/Start', [
            'programmes' => $programmes,
            'is_authenticated' => auth()->check(),
        ]);
    }
}
