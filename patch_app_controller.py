with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """        return Inertia::render('Applicant/ApplicationForm', [
            'programmes' => $programmes,
            'active_session' => \App\Models\AcademicSession::where('is_active', true)->first(),
        ]);"""

replacement = """        $preselectedProgramme = $request->query('programme_id') ?? session('preselected_programme');
        $preselectedSpecialisation = $request->query('specialisation_id') ?? session('preselected_specialisation');

        return Inertia::render('Applicant/ApplicationForm', [
            'programmes' => $programmes,
            'active_session' => \App\Models\AcademicSession::where('is_active', true)->first(),
            'preselected_programme' => $preselectedProgramme ? (int)$preselectedProgramme : null,
            'preselected_specialisation' => $preselectedSpecialisation ? (int)$preselectedSpecialisation : null,
        ]);"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
