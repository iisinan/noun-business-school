with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

content = content.replace("store('applications/documents', 'public')", "store('applications/documents', 's3')")
content = content.replace("store('applications/passports', 'public')", "store('applications/passports', 's3')")

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
