with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """        \Log::info('UPLOAD_MAX_FILESIZE', ['size' => ini_get('upload_max_filesize')]);"""
replacement = """        \Log::info('UPLOAD_MAX_FILESIZE', ['size' => ini_get('upload_max_filesize')]);
        \Log::info('POST_MAX_SIZE', ['size' => ini_get('post_max_size')]);
        \Log::info('UPLOAD_TMP_DIR', ['dir' => ini_get('upload_tmp_dir') ?: sys_get_temp_dir()]);"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
