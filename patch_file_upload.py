with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Update handleFileUpload
target_script = """const handleFileUpload = (e, reqDesc) => {
    const file = e.target.files[0];
    if (file) {
        form.documents[reqDesc] = file;
    }
};"""

replacement_script = """const handleFileUpload = (e, reqDesc) => {
    const files = e.target.files;
    if (files.length > 0) {
        form.documents[reqDesc] = Array.from(files);
    } else {
        delete form.documents[reqDesc];
    }
};"""

content = content.replace(target_script, replacement_script)

# Add multiple attribute and update instruction text
target_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-4">
                                        <label class="block text-sm font-medium text-gray-700 mb-1">{{ req.description }} <span class="text-red-500">*</span></label>
                                        <input type="file" @change="e => handleFileUpload(e, req.description)" :class="errorClass('doc_' + req.id)" class="block w-full rounded-lg border-gray-300 text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-green-50 file:text-noun-green hover:file:bg-green-100 transition-colors">
                                    </div>"""

replacement_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-4">
                                        <label class="block text-sm font-medium text-gray-700 mb-1">{{ req.description }} <span class="text-red-500">*</span></label>
                                        <p class="text-xs text-gray-500 mb-2">You can select multiple files by holding down CTRL (or CMD) while selecting.</p>
                                        <input type="file" multiple @change="e => handleFileUpload(e, req.description)" :class="errorClass('doc_' + req.id)" class="block w-full rounded-lg border-gray-300 text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-green-50 file:text-noun-green hover:file:bg-green-100 transition-colors">
                                        
                                        <div v-if="form.documents[req.description] && form.documents[req.description].length > 1" class="mt-2 text-xs text-noun-green font-medium">
                                            {{ form.documents[req.description].length }} files selected
                                        </div>
                                    </div>"""

content = content.replace(target_template, replacement_template)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
