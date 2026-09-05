<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Course;
use Illuminate\Http\Request;
use Inertia\Inertia;

class CourseController extends Controller
{
    public function index(Request $request)
    {
        $query = Course::query();

        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function($q) use ($search) {
                $q->where('code', 'like', "%{$search}%")
                  ->orWhere('title', 'like', "%{$search}%");
            });
        }

        if ($request->filled('programme_id')) {
            $query->whereHas('programmes', function($q) use ($request) {
                $q->where('programmes.id', $request->programme_id);
            });
        }

        $courses = $query->latest()->paginate(20)->withQueryString();
        $programmes = \App\Models\Programme::select('id', 'name')->orderBy('name')->get();

        return Inertia::render('Admin/Courses/Index', [
            'courses' => $courses,
            'programmes' => $programmes,
            'filters' => $request->only(['search', 'programme_id'])
        ]);
    }

    public function create()
    {
        return Inertia::render('Admin/Courses/Create');
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'code' => 'required|string|max:20|unique:courses',
            'title' => 'required|string|max:255',
            'type' => 'required|string|in:Core,Elective',
            'credits' => 'required|integer|min:1',
            'semester' => 'required|integer|in:1,2',
            'level' => 'required|integer|in:700,800,900',
            'description' => 'nullable|string'
        ]);

        $courseData = $validated;
        $courseData['units'] = $courseData['credits'];
        unset($courseData['credits']);
        
        Course::create($courseData);

        return redirect()->route('admin.courses.index')->with('success', 'Course created successfully.');
    }
}
