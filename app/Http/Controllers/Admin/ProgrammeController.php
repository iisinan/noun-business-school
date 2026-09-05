<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Programme;
use App\Models\Specialisation;
use Illuminate\Http\Request;
use Inertia\Inertia;

class ProgrammeController extends Controller
{
    public function index()
    {
        $programmes = Programme::with('specialisations')->latest()->get();
        return Inertia::render('Admin/Programmes/Index', [
            'programmes' => $programmes
        ]);
    }

    public function create()
    {
        return Inertia::render('Admin/Programmes/Create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'type' => 'required|string|in:PGD,MBA,MSc,PhD',
            'description' => 'nullable|string',
            'duration' => 'required|integer|min:1',
            'admission_requirements' => 'nullable|array',
            'specialisations' => 'nullable|array',
            'specialisations.*.name' => 'required|string|max:255'
        ]);

        $programme = Programme::create([
            'name' => $validated['name'],
            'type' => $validated['type'],
            'description' => $validated['description'],
            'duration' => $validated['duration'],
            'admission_requirements' => $validated['admission_requirements'] ?? []
        ]);

        if (!empty($validated['specialisations'])) {
            foreach ($validated['specialisations'] as $spec) {
                $programme->specialisations()->create(['name' => $spec['name']]);
            }
        }

        return redirect()->route('admin.programmes.index')->with('success', 'Programme created successfully.');
    }

    public function show(Programme $programme)
    {
        $programme->load('courses', 'specialisations');
        $allCourses = \App\Models\Course::orderBy('code')->get();
        
        return Inertia::render('Admin/Programmes/Show', [
            'programme' => $programme,
            'allCourses' => $allCourses
        ]);
    }

    public function attachCourse(Request $request, Programme $programme)
    {
        $request->validate([
            'course_id' => 'required|exists:courses,id'
        ]);

        $programme->courses()->syncWithoutDetaching([$request->course_id]);

        return back()->with('success', 'Course attached to programme successfully.');
    }

    public function detachCourse(Programme $programme, \App\Models\Course $course)
    {
        $programme->courses()->detach($course->id);
        return back()->with('success', 'Course removed from programme.');
    }

    public function toggleStatus(Programme $programme)
    {
        $programme->update([
            'is_active' => !$programme->is_active
        ]);

        $status = $programme->is_active ? 'activated' : 'suspended';
        return back()->with('success', "Programme has been {$status}.");
    }
}