with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

target = """    public function store(Request $request)
    {
        $validated = $request->validate(["""
replacement = """    public function store(Request $request)
    {
        \Log::info('STORE PAYLOAD', $request->all());
        try {
            $validated = $request->validate(["""

target2 = """            'documents.*.*' => 'file|max:5120', // 5MB limit
        ]);"""
replacement2 = """            'documents.*.*' => 'file|max:5120', // 5MB limit
        ]);
        } catch (\Illuminate\Validation\ValidationException $e) {
            \Log::error('VALIDATION FAILED', $e->errors());
            throw $e;
        }"""

content = content.replace(target, replacement).replace(target2, replacement2)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)
