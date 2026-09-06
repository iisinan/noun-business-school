<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Specialisation;
use App\Models\Course;
use Illuminate\Http\Request;
use Inertia\Inertia;

class SpecialisationController extends Controller
{
    public function show(Specialisation $specialisation)
    {
        $specialisation->load(['programme.courses', 'courses']);
        $allCourses = Course::orderBy('code')->get();
        
        $visibleCourses = $specialisation->programme->courses->merge($specialisation->courses)->unique('id')->sortBy('code')->values();
        
        $programmeCourses = $visibleCourses->map(function($course) use ($specialisation) {
            $specialisationCourse = $specialisation->courses->where('id', $course->id)->first();
            $course->is_attached = $specialisationCourse ? true : false;
            $course->is_elective = $specialisationCourse ? (bool) $specialisationCourse->pivot->is_elective : false;
            return $course;
        });
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'programmeCourses' => $programmeCourses,
            'allCourses' => $allCourses
        ]);
    }

    public function attachCourse(Request $request, Specialisation $specialisation)
    {
        $request->validate([
            'course_id' => 'required|exists:courses,id',
            'is_elective' => 'required|boolean'
        ]);

        $specialisation->courses()->syncWithoutDetaching([
            $request->course_id => ['is_elective' => $request->is_elective]
        ]);

        return back()->with('success', 'Course attached to track successfully.');
    }

    public function detachCourse(Specialisation $specialisation, Course $course)
    {
        $specialisation->courses()->detach($course->id);
        return back()->with('success', 'Course removed from track.');
    }
}