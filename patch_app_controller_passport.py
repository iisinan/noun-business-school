with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target_validation = """            'employment_info' => 'required|array',
            // Documents are passed as files
            'documents' => 'required|array',
            'documents.*' => 'required|array',
            'documents.*.*' => 'file|max:5120', // 5MB limit
        ]);"""

replacement_validation = """            'employment_info' => 'required|array',
            'passport_photograph' => 'required|image|max:2048', // 2MB passport photo
            // Documents are passed as files
            'documents' => 'required|array',
            'documents.*' => 'required|array',
            'documents.*.*' => 'file|max:5120', // 5MB limit
        ]);"""
content = content.replace(target_validation, replacement_validation)

target_storage = """        // Generate application number
        $applicationNumber = 'APP/' . date('Y') . '/' . str_pad(rand(1, 99999), 5, '0', STR_PAD_LEFT);

        $application = $request->user()->applications()->create(["""

replacement_storage = """        // Handle passport upload
        $personalInfo = $validated['personal_info'];
        if ($request->hasFile('passport_photograph')) {
            $personalInfo['passport_photograph_path'] = $request->file('passport_photograph')->store('applications/passports', 'public');
        }

        // Generate application number
        $applicationNumber = 'APP/' . date('Y') . '/' . str_pad(rand(1, 99999), 5, '0', STR_PAD_LEFT);

        $application = $request->user()->applications()->create(["""
content = content.replace(target_storage, replacement_storage)

target_save = """            'application_number' => $applicationNumber,
            'personal_info' => $validated['personal_info'],
            'academic_background' => $validated['academic_background'],"""

replacement_save = """            'application_number' => $applicationNumber,
            'personal_info' => $personalInfo,
            'academic_background' => $validated['academic_background'],"""
content = content.replace(target_save, replacement_save)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)

