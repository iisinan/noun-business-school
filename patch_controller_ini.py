with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """        \Log::info('FILE ERRORS', $fileErrors);"""
replacement = """        \Log::info('FILE ERRORS', $fileErrors);
        \Log::info('UPLOAD_MAX_FILESIZE', ['size' => ini_get('upload_max_filesize')]);"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
