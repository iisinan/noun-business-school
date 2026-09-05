<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ProgrammeController.php';
$content = file_get_contents($file);

$additions = <<<PHP

    public function show(Programme \$programme)
    {
        \$programme->load('courses', 'specialisations');
        \$allCourses = \App\Models\Course::orderBy('code')->get();
        
        return Inertia::render('Admin/Programmes/Show', [
            'programme' => \$programme,
            'allCourses' => \$allCourses
        ]);
    }

    public function attachCourse(Request \$request, Programme \$programme)
    {
        \$request->validate([
            'course_id' => 'required|exists:courses,id'
        ]);

        \$programme->courses()->syncWithoutDetaching([\$request->course_id]);

        return back()->with('success', 'Course attached to programme successfully.');
    }

    public function detachCourse(Programme \$programme, \App\Models\Course \$course)
    {
        \$programme->courses()->detach(\$course->id);
        return back()->with('success', 'Course removed from programme.');
    }
}
PHP;

$content = preg_replace('/\}\s*$/', $additions, $content);
file_put_contents($file, $content);
echo "Patched ProgrammeController\n";
