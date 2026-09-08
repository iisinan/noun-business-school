with open('app/Http/Controllers/Admin/ResultController.php', 'r') as f:
    content = f.read()

target = """    public function downloadTemplate(Request $request)
    {
        $request->validate([
            'mode' => 'required|in:single,multiple',
            'course_id' => 'required_if:mode,single|nullable|exists:courses,id',
            'academic_session_id' => 'required|exists:academic_sessions,id',
            'semester' => 'required_if:mode,multiple|nullable|integer|min:1|max:6',
        ]);

        $session = AcademicSession::find($request->academic_session_id);
        
        $query = CourseRegistration::with(['user.applications' => function($q) {
                $q->latest();
            }, 'course'])
            ->where('academic_session_id', $request->academic_session_id)
            ->orderBy('user_id');
            
        if ($request->mode === 'single') {
            $query->where('course_id', $request->course_id);
            $course = Course::find($request->course_id);
            $fileName = "results_template_{$course->code}_{$session->name}.xlsx";
        } else {
            $query->where('semester', $request->semester);
            $fileName = "results_template_sem{$request->semester}_{$session->name}.xlsx";
        }"""

replacement = """    public function downloadTemplate(Request $request)
    {
        $request->validate([
            'mode' => 'required|in:single,multiple',
            'course_id' => 'required_if:mode,single|nullable|exists:courses,id',
            'academic_session_id' => 'required|exists:academic_sessions,id',
        ]);

        $session = AcademicSession::find($request->academic_session_id);
        
        $query = CourseRegistration::with(['user.applications' => function($q) {
                $q->latest();
            }, 'course'])
            ->where('academic_session_id', $request->academic_session_id)
            ->orderBy('user_id');
            
        if ($request->mode === 'single') {
            $query->where('course_id', $request->course_id);
            $course = Course::find($request->course_id);
            $fileName = "results_template_{$course->code}_{$session->name}.xlsx";
        } else {
            $fileName = "results_template_all_courses_{$session->name}.xlsx";
        }"""

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Admin/ResultController.php', 'w') as f:
        f.write(content)
    print("Patched ResultController")
else:
    print("Target not found in ResultController")
