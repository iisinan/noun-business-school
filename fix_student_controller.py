import re

with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

# Add registration method
target = """    public function registerSemester(Request $request)"""

registration_method = """    public function registration(Request $request)
    {
        $user = $request->user();
        $activeSession = AcademicSession::where('is_active', true)->first();

        $hasRegisteredSemester = false;
        $registeredCourses = [];
        $availableCourses = [];

        if ($activeSession) {
            $hasRegisteredSemester = SemesterRegistration::where('user_id', $user->id)
                ->where('academic_session_id', $activeSession->id)
                ->exists();
            
            if ($hasRegisteredSemester) {
                $registeredCourseIds = CourseRegistration::where('user_id', $user->id)
                    ->where('academic_session_id', $activeSession->id)
                    ->pluck('course_id')
                    ->toArray();

                $registeredCourses = Course::whereIn('id', $registeredCourseIds)->get();

                $application = $user->applications()->where('status', 'ENROLLED')->latest()->first();
                if ($application && $application->programme_id) {
                    $availableCourses = $application->programme->courses()
                        ->whereNotIn('courses.id', $registeredCourseIds)
                        ->get();
                } else {
                    $availableCourses = Course::whereNotIn('id', $registeredCourseIds)->get();
                }
            }
        }

        $transactions = WalletTransaction::where('user_id', $user->id)->latest()->take(10)->get();

        return Inertia::render('Student/Registration', [
            'wallet_balance' => (float) $user->wallet_balance,
            'transactions' => $transactions,
            'activeSession' => $activeSession,
            'hasRegisteredSemester' => $hasRegisteredSemester,
            'registeredCourses' => $registeredCourses,
            'availableCourses' => $availableCourses,
        ]);
    }

    public function registerSemester(Request $request)"""

content = content.replace(target, registration_method)

with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
    f.write(content)

