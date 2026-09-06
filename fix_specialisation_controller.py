with open('app/Http/Controllers/Admin/SpecialisationController.php', 'r') as f:
    content = f.read()

target = """    public function show(Specialisation $specialisation)
    {
        $specialisation->load(['programme.courses', 'courses']);
        
        $programmeCourses = $specialisation->programme->courses->map(function($course) use ($specialisation) {
            $specialisationCourse = $specialisation->courses->where('id', $course->id)->first();
            $course->is_attached = $specialisationCourse ? true : false;
            $course->is_elective = $specialisationCourse ? (bool) $specialisationCourse->pivot->is_elective : false;
            return $course;
        });
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'programmeCourses' => $programmeCourses
        ]);
    }"""

replacement = """    public function show(Specialisation $specialisation)
    {
        $specialisation->load('courses', 'programme');
        
        // Show ALL courses in the system, allowing them to be attached directly to the track
        $allCourses = \App\Models\Course::orderBy('code')->get()->map(function($course) use ($specialisation) {
            $specialisationCourse = $specialisation->courses->where('id', $course->id)->first();
            $course->is_attached = $specialisationCourse ? true : false;
            $course->is_elective = $specialisationCourse ? (bool) $specialisationCourse->pivot->is_elective : false;
            return $course;
        });
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'programmeCourses' => $allCourses // Keeping variable name same so Vue doesn't break
        ]);
    }"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Admin/SpecialisationController.php', 'w') as f:
        f.write(content)
    print("Fixed SpecialisationController")
else:
    print("Target not found in SpecialisationController")
