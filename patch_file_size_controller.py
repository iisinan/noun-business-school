with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """            'olevel_results' => 'required|array',
            'employment_info' => 'required|array',
            // Documents are passed as files
        ]);"""

replacement = """            'olevel_results' => 'required|array',
            'employment_info' => 'required|array',
            // Documents are passed as files
            'documents' => 'required|array',
            'documents.*' => 'required|array',
            'documents.*.*' => 'file|max:5120', // 5MB limit
        ]);"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
