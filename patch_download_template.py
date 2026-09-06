file_path = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/ResultController.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """    public function downloadTemplate(Request $request)
    {
        $request->validate([
            'academic_session_id' => 'required|exists:academic_sessions,id',
            'semester' => 'required|integer|min:1|max:6',
        ]);

        $session = AcademicSession::find($request->academic_session_id);
        
        $registrations = CourseRegistration::with(['user.applications' => function($q) {
                $q->latest();
            }, 'course'])
            ->where('academic_session_id', $request->academic_session_id)
            ->where('semester', $request->semester)
            ->orderBy('user_id')
            ->get();"""

replace = """    public function downloadTemplate(Request $request)
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
        }
        
        $registrations = $query->get();"""

content = content.replace(search, replace)

search2 = """        $writer = new Xlsx($spreadsheet);
        $fileName = "results_template_sem{$request->semester}_{$session->name}.xlsx";"""

replace2 = """        $writer = new Xlsx($spreadsheet);
        // $fileName is set above"""

content = content.replace(search2, replace2)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched ResultController")
