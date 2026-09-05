import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# 1. Update useForm
target_form = """const form = useForm({
    programme_id: props.preselected_programme || '',
    specialisation_id: props.preselected_specialisation || '',
    personal_info: {"""
replacement_form = """const form = useForm({
    programme_id: props.preselected_programme || '',
    specialisation_id: props.preselected_specialisation || '',
    passport_photograph: null,
    personal_info: {"""
content = content.replace(target_form, replacement_form)


# 2. Add refs and logic
target_refs = """const currentStep = ref(props.preselected_programme ? 2 : 1);
const totalSteps = 4;"""
replacement_refs = """const currentStep = ref(props.preselected_programme ? 2 : 1);
const totalSteps = 4;

const passportPreview = ref(null);
const submitLoader = ref({ active: false, text: '' });

const handlePassportUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
        if (file.size > 2 * 1024 * 1024) {
            alert('Passport photograph must be less than 2MB.');
            e.target.value = '';
            return;
        }
        form.passport_photograph = file;
        passportPreview.value = URL.createObjectURL(file);
    } else {
        form.passport_photograph = null;
        passportPreview.value = null;
    }
};"""
content = content.replace(target_refs, replacement_refs)


# 3. Update Step 2 validation
target_step2 = """        if (p.nationality === 'Other' && !p.nationality_other) { fieldErrors.value.nationality_other = true; hasError = true; }
        if (hasError) validationErrors.value.push('Please fill in all required personal information fields.');
    }"""
replacement_step2 = """        if (p.nationality === 'Other' && !p.nationality_other) { fieldErrors.value.nationality_other = true; hasError = true; }
        if (!form.passport_photograph) { fieldErrors.value.passport_photograph = true; hasError = true; }
        if (hasError) validationErrors.value.push('Please fill in all required personal information fields and upload a passport photograph.');
    }"""
content = content.replace(target_step2, replacement_step2)


# 4. Update submit method
target_submit = """    if (hasError) return;

    form.post(route('applicant.application.store'));
};"""
replacement_submit = """    if (hasError) return;

    submitLoader.value = { active: true, text: 'Analyzing your details...' };
    
    setTimeout(() => {
        submitLoader.value.text = 'Submitting your application...';
        
        form.post(route('applicant.application.store'), {
            onSuccess: () => {
                submitLoader.value.text = 'Submission complete!';
            },
            onError: () => {
                submitLoader.value.active = false;
            }
        });
    }, 1500);
};"""
content = content.replace(target_submit, replacement_submit)


# 5. Template: Add Passport Upload to Step 2
target_step2_html = """                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Identification Type</label>"""
replacement_step2_html = """                                <div class="col-span-1 md:col-span-2 mt-4 bg-white p-5 rounded-xl border border-gray-100 shadow-sm flex flex-col sm:flex-row gap-6 items-center">
                                    <div class="w-28 h-28 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden flex-shrink-0 border border-gray-200">
                                        <img v-if="passportPreview" :src="passportPreview" class="w-full h-full object-cover" />
                                        <svg v-else class="w-10 h-10 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                                    </div>
                                    <div class="flex-1 w-full text-center sm:text-left">
                                        <h4 class="font-bold text-gray-800 text-sm mb-1">Passport Photograph <span class="text-red-500">*</span></h4>
                                        <p class="text-xs text-gray-500 mb-4">Upload a recent, clear passport-sized photograph. Max 2MB (JPG/PNG).</p>
                                        <div class="flex justify-center sm:justify-start">
                                            <label for="passport_upload" class="cursor-pointer inline-flex items-center gap-1.5 text-xs font-bold text-noun-green hover:text-noun-dark bg-green-50 hover:bg-green-100 px-4 py-2 rounded-full transition-colors border border-green-200 shadow-sm" :class="errorClass('passport_photograph')">
                                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
                                                Choose Image
                                            </label>
                                            <input id="passport_upload" type="file" accept="image/jpeg, image/png" @change="handlePassportUpload" class="hidden">
                                        </div>
                                    </div>
                                </div>
                                
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Identification Type</label>"""
content = content.replace(target_step2_html, replacement_step2_html)


# 6. Template: Add Loader Modal
target_loader_html = """    <AuthenticatedLayout>

        <!-- Validation Error Modal -->"""
replacement_loader_html = """    <AuthenticatedLayout>

        <!-- Submit Loader Modal -->
        <div v-if="submitLoader.active" class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-gray-900/60 backdrop-blur-sm transition-opacity">
            <div class="bg-white rounded-2xl shadow-2xl w-full max-w-sm p-8 text-center transform transition-all flex flex-col items-center">
                <div v-if="submitLoader.text !== 'Submission complete!'" class="relative w-16 h-16 mb-6">
                    <div class="absolute inset-0 border-4 border-gray-100 rounded-full"></div>
                    <div class="absolute inset-0 border-4 border-noun-green rounded-full border-t-transparent animate-spin"></div>
                </div>
                <div v-else class="w-16 h-16 mb-6 bg-green-100 rounded-full flex items-center justify-center">
                    <svg class="w-8 h-8 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" /></svg>
                </div>
                <h3 class="text-lg font-bold text-gray-900 mb-2">{{ submitLoader.text }}</h3>
                <p v-if="submitLoader.text !== 'Submission complete!'" class="text-sm text-gray-500">Please do not close or refresh this page.</p>
                <p v-else class="text-sm text-gray-500">Redirecting you to dashboard...</p>
            </div>
        </div>

        <!-- Validation Error Modal -->"""
content = content.replace(target_loader_html, replacement_loader_html)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

