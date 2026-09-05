import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Add script setup variables
script_addition = """
const validationErrors = ref([]);
const fieldErrors = ref({});

const errorClass = (field) => {
    return fieldErrors.value[field] ? 'border-red-500 ring-1 ring-red-500' : 'border-gray-300';
};
"""
content = content.replace("const nextStep = () => {", script_addition + "\nconst nextStep = () => {")

# Rewrite nextStep to use validationErrors and fieldErrors
next_step_logic = """const nextStep = () => {
    fieldErrors.value = {};
    validationErrors.value = [];
    let hasError = false;

    // Step 1 Validation
    if (currentStep.value === 1) {
        if (!form.programme_id) { fieldErrors.value.programme_id = true; hasError = true; }
        if (selectedProgramme.value?.specialisations.length > 0 && !form.specialisation_id) { fieldErrors.value.specialisation_id = true; hasError = true; }
        if (hasError) validationErrors.value.push('Please select a programme and specialisation.');
    }
    
    // Step 2 Validation
    if (currentStep.value === 2) {
        const p = form.personal_info;
        const requiredFields = ['full_name', 'gender', 'marital_status', 'dob', 'nationality', 'state_of_origin', 'phone', 'email', 'address'];
        requiredFields.forEach(f => {
            if (!p[f]) { fieldErrors.value[f] = true; hasError = true; }
        });
        if (p.nationality === 'Other' && !p.nationality_other) { fieldErrors.value.nationality_other = true; hasError = true; }
        if (hasError) validationErrors.value.push('Please fill in all required personal information fields.');
    }

    // Step 3 Validation
    if (currentStep.value === 3) {
        // Academic Background
        form.academic_background.forEach((edu, i) => {
            if (!edu.institution) { fieldErrors.value['edu_institution_'+i] = true; hasError = true; }
            if (!edu.qualification) { fieldErrors.value['edu_qualification_'+i] = true; hasError = true; }
            if (!edu.course_of_study) { fieldErrors.value['edu_course_'+i] = true; hasError = true; }
            if (!edu.grade) { fieldErrors.value['edu_grade_'+i] = true; hasError = true; }
        });
        
        // OLevel
        if (!isExecutiveCert.value && !isDBA.value) {
            form.olevel_results.forEach((olevel, i) => {
                if (!olevel.exam_type) { fieldErrors.value['olevel_type_'+i] = true; hasError = true; }
                if (!olevel.exam_year) { fieldErrors.value['olevel_year_'+i] = true; hasError = true; }
                if (!olevel.exam_number) { fieldErrors.value['olevel_number_'+i] = true; hasError = true; }
            });
        }
        if (hasError) validationErrors.value.push('Please complete all required Academic and O\\'Level details.');
    }

    if (hasError) return;

    if (currentStep.value < totalSteps) currentStep.value++;
};"""

content = re.sub(r'const nextStep = \(\) => \{.*?(?=const prevStep = \(\) => \{)', next_step_logic + '\n\n', content, flags=re.DOTALL)

# Rewrite submit
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
            hasError = true;
        }
    }

    if (hasError) return;

    form.post(route('applicant.application.store'));
};"""
content = re.sub(r'const submit = \(\) => \{.*?(?=const selectedProgramme = computed\(\(\) => \{)', submit_logic + '\n\n', content, flags=re.DOTALL)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

