with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target_script = """const handleFileSelect = (e, reqDesc) => {
    const file = e.target.files[0];
    if (file) {
        if (!form.documents[reqDesc]) {
            form.documents[reqDesc] = [];
        }"""

replacement_script = """const handleFileSelect = (e, reqDesc) => {
    const file = e.target.files[0];
    if (file) {
        // 5MB limit
        if (file.size > 5 * 1024 * 1024) {
            alert(`The file "${file.name}" is too large. Please select a file smaller than 5MB.`);
            e.target.value = '';
            return;
        }

        if (!form.documents[reqDesc]) {
            form.documents[reqDesc] = [];
        }"""

content = content.replace(target_script, replacement_script)

target_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-6 bg-white p-4 rounded-xl border border-gray-100 shadow-sm">
                                        <label class="block text-sm font-medium text-gray-800 mb-3">{{ req.description }} <span class="text-red-500">*</span></label>
                                        
                                        <!-- List of attached files -->"""

replacement_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-6 bg-white p-4 rounded-xl border border-gray-100 shadow-sm">
                                        <div class="flex justify-between items-start mb-3">
                                            <label class="block text-sm font-medium text-gray-800">{{ req.description }} <span class="text-red-500">*</span></label>
                                            <span class="text-[10px] uppercase font-bold text-gray-400 bg-gray-100 px-2 py-1 rounded">Max 5MB</span>
                                        </div>
                                        
                                        <!-- List of attached files -->"""

content = content.replace(target_template, replacement_template)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
