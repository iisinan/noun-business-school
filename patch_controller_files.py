with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """    public function store(Request $request)
    {
        \Log::info('STORE PAYLOAD', $request->all());"""
replacement = """    public function store(Request $request)
    {
        $fileErrors = [];
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
        }
        \Log::info('FILE ERRORS', $fileErrors);
        \Log::info('STORE PAYLOAD', $request->all());"""

content = content.replace(target, replacement)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
