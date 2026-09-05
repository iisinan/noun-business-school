with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Update script logic
target_script = """const handleFileUpload = (e, reqDesc) => {
    const files = e.target.files;
    if (files.length > 0) {
        form.documents[reqDesc] = Array.from(files);
    } else {
        delete form.documents[reqDesc];
    }
};"""

replacement_script = """const handleFileSelect = (e, reqDesc) => {
    const file = e.target.files[0];
    if (file) {
        if (!form.documents[reqDesc]) {
            form.documents[reqDesc] = [];
        }
        form.documents[reqDesc].push(file);
        // trigger reactivity
        form.documents[reqDesc] = [...form.documents[reqDesc]];
        
        // Reset the input
        e.target.value = '';
    }
};

const removeAttachedFile = (reqDesc, idx) => {
    if (form.documents[reqDesc]) {
        form.documents[reqDesc].splice(idx, 1);
        form.documents[reqDesc] = [...form.documents[reqDesc]];
    }
};"""

content = content.replace(target_script, replacement_script)

# Update validation logic
target_validation = """    for (let req of reqDocs) {
        if (!form.documents[req.description]) {
            validationErrors.value.push(`Please upload the required document: ${req.description}`);"""

replacement_validation = """    for (let req of reqDocs) {
        if (!form.documents[req.description] || form.documents[req.description].length === 0) {
            validationErrors.value.push(`Please upload the required document: ${req.description}`);"""

content = content.replace(target_validation, replacement_validation)

# Update template logic
target_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-4">
                                        <label class="block text-sm font-medium text-gray-700 mb-1">{{ req.description }} <span class="text-red-500">*</span></label>
                                        <p class="text-xs text-gray-500 mb-2">You can select multiple files by holding down CTRL (or CMD) while selecting.</p>
                                        <input type="file" multiple @change="e => handleFileUpload(e, req.description)" :class="errorClass('doc_' + req.id)" class="block w-full rounded-lg border-gray-300 text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-green-50 file:text-noun-green hover:file:bg-green-100 transition-colors">
                                        
                                        <div v-if="form.documents[req.description] && form.documents[req.description].length > 1" class="mt-2 text-xs text-noun-green font-medium">
                                            {{ form.documents[req.description].length }} files selected
                                        </div>
                                    </div>"""

replacement_template = """                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-6 bg-white p-4 rounded-xl border border-gray-100 shadow-sm">
                                        <label class="block text-sm font-medium text-gray-800 mb-3">{{ req.description }} <span class="text-red-500">*</span></label>
                                        
                                        <!-- List of attached files -->
                                        <ul v-if="form.documents[req.description] && form.documents[req.description].length > 0" class="mb-3 space-y-2">
                                            <li v-for="(file, idx) in form.documents[req.description]" :key="idx" class="flex items-center gap-3 bg-gray-50 px-3 py-2.5 rounded-lg text-sm text-gray-700 border border-gray-200">
                                                <svg class="w-5 h-5 text-noun-green flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                                                <span class="flex-1 truncate font-medium">{{ file.name }}</span>
                                                <button type="button" @click="removeAttachedFile(req.description, idx)" class="text-red-500 hover:text-red-700 p-1 bg-red-50 rounded-full hover:bg-red-100 transition" title="Remove Document">
                                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
                                                </button>
                                            </li>
                                        </ul>
                                        
                                        <div v-if="!form.documents[req.description] || form.documents[req.description].length === 0" class="text-xs text-gray-400 italic mb-3">No documents attached yet.</div>

                                        <div class="flex items-center gap-2">
                                            <label :for="'file_' + req.id" class="cursor-pointer inline-flex items-center gap-1.5 text-xs font-bold text-noun-green hover:text-noun-dark bg-green-50 hover:bg-green-100 px-4 py-2 rounded-full transition-colors border border-green-200 shadow-sm" :class="errorClass('doc_' + req.id)">
                                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                                                {{ form.documents[req.description] && form.documents[req.description].length > 0 ? 'Add another document' : 'Attach Document' }}
                                            </label>
                                            <input :id="'file_' + req.id" type="file" class="hidden" @change="e => handleFileSelect(e, req.description)">
                                        </div>
                                    </div>"""

content = content.replace(target_template, replacement_template)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
