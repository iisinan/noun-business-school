with open('app/Http/Controllers/Admin/ProgrammeController.php', 'r') as f:
    content = f.read()

target = """    public function show(Programme $programme)
    {
        $programme->load('courses', 'specialisations');
        $allCourses = \App\Models\Course::orderBy('code')->get();
        
        return Inertia::render('Admin/Programmes/Show', [
            'programme' => $programme,
            'allCourses' => $allCourses
        ]);
    }"""

replacement = """    public function show(Programme $programme)
    {
        $programme->load('courses', 'specialisations');
        
        $allCourses = \App\Models\Course::orderBy('code')->get()->map(function($course) use ($programme) {
            $course->is_attached = $programme->courses->where('id', $course->id)->isNotEmpty();
            return $course;
        });
        
        return Inertia::render('Admin/Programmes/Show', [
            'programme' => $programme,
            'allCourses' => $allCourses
        ]);
    }"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Admin/ProgrammeController.php', 'w') as f:
        f.write(content)
    print("Patched ProgrammeController")
else:
    print("Target not found in ProgrammeController")
