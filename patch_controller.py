with open('app/Http/Controllers/Admin/SpecialisationController.php', 'r') as f:
    content = f.read()

target = """    public function show(Specialisation $specialisation)
    {
        $specialisation->load('programme', 'courses');
        $allCourses = Course::orderBy('code')->get();
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'allCourses' => $allCourses
        ]);
    }"""

replacement = """    public function show(Specialisation $specialisation)
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

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Admin/SpecialisationController.php', 'w') as f:
        f.write(content)
    print("Controller Patched")
else:
    print("Target not found")
