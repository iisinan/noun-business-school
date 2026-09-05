import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Update submit function to include fieldErrors for documents
submit_logic = """const submit = () => {
    fieldErrors.value = {};
    validationErrors.value = [];
    let hasError = false;

    // Validate Employment Info (if required)
    const emp = form.employment_info;
    if (!emp.organisation) { fieldErrors.value.emp_organisation = true; hasError = true; }
    if (!emp.job_title) { fieldErrors.value.emp_job_title = true; hasError = true; }
    if (!emp.years_experience) { fieldErrors.value.emp_years = true; hasError = true; }
    if (hasError) validationErrors.value.push('Please fill in your current employment details.');

    // Validate Required Documents
    const reqDocs = programmeRequirements.value.filter(req => req.is_document);
    for (let req of reqDocs) {
        if (!form.documents[req.description]) {
            validationErrors.value.push(`Please upload the required document: ${req.description}`);
            fieldErrors.value['doc_' + req.id] = true;
            hasError = true;
        }
    }

    if (hasError) return;

    form.post(route('applicant.application.store'));
};"""
content = re.sub(r'const submit = \(\) => \{.*?(?=const selectedProgramme = computed\(\(\) => \{)', submit_logic + '\n\n', content, flags=re.DOTALL)

# Update the document file input to use the errorClass
content = content.replace(
    '<input type="file" @change="e => handleFileUpload(e, req.description)" class="block w-full text-sm',
    '<input type="file" @change="e => handleFileUpload(e, req.description)" :class="errorClass(\'doc_\' + req.id)" class="block w-full rounded-lg border-gray-300 text-sm'
)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

