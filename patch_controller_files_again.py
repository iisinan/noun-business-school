with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """        $fileErrors = [];
        if ($request->hasFile('passport_photograph')) {
            $fileErrors['passport'] = $request->file('passport_photograph')->getError();
        }
        if ($request->hasFile('documents')) {
            foreach ($request->file('documents') as $key => $files) {
                if (is_array($files)) {
                    foreach ($files as $i => $file) {
                        $fileErrors["doc_{$key}_{$i}"] = $file->getError();
                    }
                }
            }
        }"""
replacement = """        $fileErrors = [];
        $passport = $request->file('passport_photograph');
        if ($passport) {
            $fileErrors['passport'] = $passport->getError();
        }
        $docs = $request->file('documents');
        if ($docs) {
            foreach ($docs as $key => $files) {
                if (is_array($files)) {
                    foreach ($files as $i => $file) {
                        $fileErrors["doc_{$key}_{$i}"] = $file->getError();
                    }
                }
            }
        }"""
content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
