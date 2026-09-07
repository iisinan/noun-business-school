<script setup>
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';
import { Head, useForm, usePage } from '@inertiajs/vue3';
import { ref, computed } from 'vue';

const props = defineProps({
    programmes: Array,
    active_session: Object,
    preselected_programme: [String, Number],
    preselected_specialisation: [String, Number]
});

const page = usePage();
const user = page.props.auth.user;

const currentStep = ref(props.preselected_programme ? 2 : 1);
const totalSteps = 4;

const passportPreview = ref(null);
const submitLoader = ref({ active: false, text: '' });
const fileError = ref(null);

const handlePassportUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
        if (file.size > 500 * 1024) {
            fileError.value = 'Passport photograph must be less than 500KB.';
            e.target.value = '';
            return;
        }
        form.passport_photograph = file;
        passportPreview.value = URL.createObjectURL(file);
    } else {
        form.passport_photograph = null;
        passportPreview.value = null;
    }
};



const form = useForm({
    programme_id: props.preselected_programme || '',
    specialisation_id: props.preselected_specialisation || '',
    passport_photograph: null,
    passport_photograph: null,
    personal_info: {
        title: '',
        full_name: `${user.first_name} ${user.last_name || ''}`.trim(),
        gender: '',
        marital_status: '',
        dob: '',
        nationality: '',
        nationality_other: '',
        state_of_origin: '',
        lga: '',
        address: '',
        phone: user.phone || '',
        whatsapp_number: '',
        email: user.email || '',
        identification_type: '',
    },
    academic_background: [{
        institution: '',
        qualification: '',
        course_of_study: '',
        graduation_year: '',
        grade: '',
    }],
    olevel_results: [
        { exam_type: '', exam_year: '', exam_number: '', sitting: 1, subjects: [{name: 'English Language', grade: ''}, {name: 'Mathematics', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}] }
    ],
    employment_info: {
        status: '',
        organisation: '',
        job_title: '',
        years_experience: '',
    },
    documents: {}
});


const validationErrors = ref([]);
const fieldErrors = ref({});

const errorClass = (field) => {
    return fieldErrors.value[field] ? 'border-red-500 ring-1 ring-red-500' : 'border-gray-300';
};

const nextStep = () => {
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
        if (!form.passport_photograph) { fieldErrors.value.passport_photograph = true; hasError = true; }
        if (hasError) validationErrors.value.push('Please fill in all required personal information fields and upload a passport photograph.');
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
                
                olevel.subjects.forEach((sub, subIdx) => {
                    // Only validate if they filled either subject or grade, meaning they started it
                    if (sub.name || sub.grade) {
                        if (!sub.name) { fieldErrors.value['olevel_sub_name_'+i+'_'+subIdx] = true; hasError = true; }
                        if (!sub.grade) { fieldErrors.value['olevel_sub_grade_'+i+'_'+subIdx] = true; hasError = true; }
                    } else if (subIdx < 5) {
                        // Let's enforce at least 5 subjects strictly
                        fieldErrors.value['olevel_sub_name_'+i+'_'+subIdx] = true; 
                        fieldErrors.value['olevel_sub_grade_'+i+'_'+subIdx] = true;
                        hasError = true;
                    }
                });
            });
        }
        if (hasError) validationErrors.value.push('Please complete all required Academic and O\'Level details (at least 5 subjects required per sitting).');
    }

    if (hasError) return;

    if (currentStep.value < totalSteps) currentStep.value++;
};

const prevStep = () => {
    if (currentStep.value > 1) currentStep.value--;
};

const nigerianStates = [
    'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'FCT - Abuja', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara'
];

const qualifications = ['BSc', 'BA', 'HND', 'OND', 'NCE', 'PGD', 'MSc', 'MA', 'MBA', 'PhD', 'Other'];
const degreeGrades = ['First Class', 'Second Class Upper (2:1)', 'Second Class Lower (2:2)', 'Third Class', 'Pass', 'Distinction', 'Upper Credit', 'Lower Credit', 'Merit'];
const examTypes = ['WAEC', 'NECO', 'NABTEB', 'GCE'];
const olevelGrades = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9', 'AR'];
const olevelSubjects = ['Mathematics', 'English Language', 'Physics', 'Chemistry', 'Biology', 'Agricultural Science', 'Economics', 'Government', 'Civic Education', 'Literature in English', 'Accounting', 'Commerce', 'Geography', 'Further Mathematics', 'History', 'CRK', 'IRK', 'Hausa', 'Igbo', 'Yoruba'];

const submit = () => {
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
    const reqDocs = programmeRequirements.value.filter(req => req.is_document == 1 || req.is_document === true || req.is_document === '1');
    for (let req of reqDocs) {
        if (!form.documents[req.description] || form.documents[req.description].length === 0) {
            validationErrors.value.push(`Please upload the required document: ${req.description}`);
            fieldErrors.value['doc_' + req.id] = true;
            hasError = true;
        }
    }

    if (hasError) return;

    submitLoader.value = { active: true, text: 'Analyzing your details...' };
    
    setTimeout(() => {
        submitLoader.value.text = 'Submitting your application...';
        
        form.post(route('applicant.application.store'), {
            onSuccess: () => {
                submitLoader.value.text = 'Submission complete!';
            },
            onError: (errors) => {
                const serverErrors = Object.values(errors).flat();
                if (serverErrors.length > 0) {
                    validationErrors.value = serverErrors;
                    setTimeout(() => { validationErrors.value = []; }, 8000);
                }
            },
            onFinish: () => {
                submitLoader.value.active = false;
            }
        });
    }, 1500);
};

const selectedProgramme = computed(() => {
    return props.programmes.find(p => p.id === form.programme_id);
});

const programmeRequirements = computed(() => {
    if(!selectedProgramme.value) return [];
    return selectedProgramme.value.admission_requirements || [];
});

const addAcademic = () => {
    form.academic_background.push({ institution: '', qualification: '', course_of_study: '', graduation_year: '', grade: '' });
};

const removeAcademic = (index) => {
    form.academic_background.splice(index, 1);
};

const addOlevel = () => {
    if(form.olevel_results.length < 2) {
        form.olevel_results.push({ exam_type: '', exam_year: '', exam_number: '', sitting: 2, subjects: [{name: 'English Language', grade: ''}, {name: 'Mathematics', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}] });
    }
};

const removeOlevel = (index) => {
    form.olevel_results.splice(index, 1);
};

const isExecutiveCert = computed(() => {
    return selectedProgramme.value?.type === 'Certificate';
});

const isDBA = computed(() => {
    return selectedProgramme.value?.type === 'DBA' || selectedProgramme.value?.type === 'DPA';
});

const handleFileSelect = (e, reqDesc) => {
    const file = e.target.files[0];
    if (file) {
        // 500KB limit
        if (file.size > 500 * 1024) {
            fileError.value = `The file "${file.name}" is too large. Please select a file smaller than 500KB.`;
            e.target.value = '';
            return;
        }

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
};
</script>

<template>
    <Head title="Application Form" />

    <AuthenticatedLayout>

        <!-- Submit Loader Modal -->
        <Transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
        >
            <div v-if="submitLoader.active" class="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-gray-900/70 backdrop-blur-md">
                <div class="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-10 text-center transform transition-all flex flex-col items-center">
                    
                    <div class="relative w-20 h-20 mb-6">
                        <Transition
                            enter-active-class="transition duration-500 ease-out absolute inset-0"
                            enter-from-class="opacity-0 scale-50 rotate-90"
                            enter-to-class="opacity-100 scale-100 rotate-0"
                            leave-active-class="transition duration-300 ease-in absolute inset-0"
                            leave-from-class="opacity-100 scale-100 rotate-0"
                            leave-to-class="opacity-0 scale-50 -rotate-90"
                        >
                            <div v-if="submitLoader.text !== 'Submission complete!'" class="absolute inset-0">
                                <!-- Pulsing logo inside -->
                                <div class="absolute inset-0 flex items-center justify-center animate-pulse">
                                    <img src="/nbs-logo.png" class="w-10 h-10 object-contain opacity-80" />
                                </div>
                                <!-- Spinning ring -->
                                <div class="absolute inset-0 border-[4px] border-gray-100 rounded-full"></div>
                                <div class="absolute inset-0 border-[4px] border-noun-green rounded-full border-t-transparent border-r-transparent animate-spin" style="animation-duration: 1s;"></div>
                            </div>
                            <div v-else class="absolute inset-0 bg-green-100 rounded-full flex items-center justify-center shadow-inner">
                                <svg class="w-10 h-10 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3.5" d="M5 13l4 4L19 7" /></svg>
                            </div>
                        </Transition>
                    </div>

                    <h3 class="text-xl font-black text-gray-900 mb-2 tracking-tight">{{ submitLoader.text }}</h3>
                    <p v-if="submitLoader.text !== 'Submission complete!'" class="text-sm text-gray-500 font-medium">Please do not close or refresh this page.</p>
                    <p v-else class="text-sm text-gray-500 font-medium">Redirecting you to dashboard...</p>
                    
                    <!-- Upload Progress -->
                    <div v-if="form.progress" class="w-full mt-5">
                        <div class="w-full bg-gray-100 rounded-full h-2 overflow-hidden relative">
                            <div class="bg-noun-green h-full rounded-full transition-all duration-300" :style="{ width: form.progress.percentage + '%' }"></div>
                        </div>
                        <p class="text-xs text-gray-500 mt-2 font-bold">{{ form.progress.percentage }}% Uploaded</p>
                    </div>
                </div>
            </div>
        </Transition>

        <!-- File Error Modal -->
        <Transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="opacity-0 scale-95"
            enter-to-class="opacity-100 scale-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="opacity-100 scale-100"
            leave-to-class="opacity-0 scale-95"
        >
            <div v-if="fileError" class="fixed inset-0 z-[80] flex items-center justify-center p-4 bg-gray-900/60 backdrop-blur-sm">
                <div class="bg-white rounded-3xl shadow-2xl w-full max-w-sm overflow-hidden transform transition-all border border-red-100">
                    <div class="bg-red-50 px-6 py-6 border-b border-red-100 flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mb-4 shadow-sm border border-red-200">
                            <svg class="h-8 w-8 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                            </svg>
                        </div>
                        <h3 class="text-xl font-black text-red-800 tracking-tight">File Too Large</h3>
                    </div>
                    <div class="p-6 text-center">
                        <p class="text-sm text-gray-600 font-medium leading-relaxed">{{ fileError }}</p>
                        <div class="mt-8">
                            <button @click="fileError = null" class="w-full px-5 py-3 bg-red-600 hover:bg-red-700 text-white text-sm font-bold rounded-xl transition-colors shadow-md focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                                Try Again
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </Transition>

        <!-- Validation Error Modal -->
        <div v-if="validationErrors.length > 0" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-900/50 backdrop-blur-sm">
            <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden transform transition-all">
                <div class="bg-red-50 px-6 py-4 border-b border-red-100 flex items-center gap-3">
                    <svg class="h-6 w-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                    <h3 class="text-lg font-bold text-red-800">Missing Information</h3>
                </div>
                <div class="p-6">
                    <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
                        <li v-for="(err, i) in validationErrors" :key="i">{{ err }}</li>
                    </ul>
                    <div class="mt-6 flex justify-end">
                        <button @click="validationErrors = []" class="px-5 py-2 bg-red-600 hover:bg-red-700 text-white text-sm font-semibold rounded-lg transition-colors shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            Got it
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">
                Application for Admission {{ active_session?.name }}
            </h2>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-4xl sm:px-6 lg:px-8">
                <div class="bg-white shadow-sm sm:rounded-xl border border-gray-100 p-8 relative overflow-hidden">
                    <!-- Subtle top accent -->
                    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-noun-green via-noun-yellow to-noun-green"></div>

                    <!-- Progress Bar -->
                    <div class="mb-10">
                        <div class="flex justify-between text-xs sm:text-sm font-medium text-gray-400 mb-3">
                            <span :class="{'text-noun-green font-bold': currentStep >= 1}">1. Programme</span>
                            <span :class="{'text-noun-green font-bold': currentStep >= 2}">2. Personal Info</span>
                            <span :class="{'text-noun-green font-bold': currentStep >= 3}">3. Academics</span>
                            <span :class="{'text-noun-green font-bold': currentStep >= 4}">4. Experience</span>
                        </div>
                        <div class="w-full bg-gray-100 rounded-full h-2">
                            <div class="bg-noun-green h-2 rounded-full transition-all duration-500 ease-out" :style="`width: ${(currentStep / totalSteps) * 100}%`"></div>
                        </div>
                    </div>

                    <form @submit.prevent="submit" class="space-y-6">
                        
                        <!-- STEP 1: Programme Selection -->
                        <div v-show="currentStep === 1" class="space-y-6">
                            <div>
                                <h3 class="text-xl font-bold text-gray-900">Select Programme</h3>
                                <p class="text-sm text-gray-500 mt-1">Choose the programme and specialisation you wish to apply for.</p>
                            </div>
                            
                            <div class="space-y-5">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Programme <span class="text-red-500">*</span></label>
                                    <select v-model="form.programme_id" :disabled="preselected_programme" :class="errorClass('programme_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5 disabled:bg-gray-100 disabled:text-gray-500">
                                        <option value="">Select a programme...</option>
                                        <option v-for="prog in programmes" :key="prog.id" :value="prog.id">
                                            {{ prog.name }}
                                        </option>
                                    </select>
                                    <p v-if="preselected_programme" class="mt-2 text-xs text-noun-green font-medium flex items-center gap-1">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                                        Locked from your initial selection
                                    </p>
                                </div>
                                
                                <div v-if="selectedProgramme && selectedProgramme.specialisations.length > 0">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Specialisation <span class="text-red-500">*</span></label>
                                    <select v-model="form.specialisation_id" :disabled="preselected_specialisation" :class="errorClass('specialisation_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5 disabled:bg-gray-100 disabled:text-gray-500">
                                        <option value="">Select a specialisation...</option>
                                        <option v-for="spec in selectedProgramme.specialisations" :key="spec.id" :value="spec.id">
                                            {{ spec.name }}
                                        </option>
                                    </select>
                                    <p v-if="preselected_specialisation" class="mt-2 text-xs text-noun-green font-medium flex items-center gap-1">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                                        Locked from your initial selection
                                    </p>
                                </div>
                            </div>

                            <div v-if="selectedProgramme" class="bg-noun-light border border-noun-green/20 p-5 rounded-xl mt-6">
                                <h4 class="text-sm font-bold text-noun-dark flex items-center gap-2">
                                    <svg class="h-4 w-4 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                    Admission Requirements
                                </h4>
                                <ul class="list-disc list-outside ml-5 mt-3 space-y-2">
                                    <li v-for="req in programmeRequirements" :key="req.id" class="text-sm text-gray-700 leading-relaxed pl-1">
                                        {{ req.description }}
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <!-- STEP 2: Personal Information -->
                        <div v-show="currentStep === 2" class="space-y-6">
                            <div>
                                <h3 class="text-xl font-bold text-gray-900">Personal Information</h3>
                                <p class="text-sm text-gray-500 mt-1">Please provide your basic contact and background details. (<span class="text-red-500">*</span> Required fields)</p>
                            </div>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Full Name <span class="text-red-500">*</span></label>
                                    <input type="text" v-model="form.personal_info.full_name" readonly :class="errorClass('full_name')" class="block w-full rounded-lg bg-gray-100 text-gray-600 shadow-sm sm:text-sm cursor-not-allowed">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Gender <span class="text-red-500">*</span></label>
                                    <select v-model="form.personal_info.gender" :class="errorClass('gender')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2">
                                        <option value="M">Male</option>
                                        <option value="F">Female</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Marital Status <span class="text-red-500">*</span></label>
                                    <select v-model="form.personal_info.marital_status" :class="errorClass('marital_status')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2">
                                        <option value="Single">Single</option>
                                        <option value="Married">Married</option>
                                        <option value="Divorced">Divorced</option>
                                        <option value="Widowed">Widowed</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Date of Birth <span class="text-red-500">*</span></label>
                                    <input type="date" v-model="form.personal_info.dob" :class="errorClass('dob')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Nationality <span class="text-red-500">*</span></label>
                                    <select v-model="form.personal_info.nationality" :class="errorClass('nationality')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2 mb-2">
                                        <option value="Nigerian">Nigerian</option>
                                        <option value="Other">Other</option>
                                    </select>
                                    <input v-if="form.personal_info.nationality === 'Other'" type="text" placeholder="Specify Nationality" v-model="form.personal_info.nationality_other" :class="errorClass('nationality_other')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">State of Origin <span class="text-red-500">*</span></label>
                                    <select v-if="form.personal_info.nationality === 'Nigerian'" v-model="form.personal_info.state_of_origin" :class="errorClass('state_of_origin')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2">
                                        <option value="">Select State...</option>
                                        <option v-for="state in nigerianStates" :key="state" :value="state">{{ state }}</option>
                                    </select>
                                    <input v-else type="text" placeholder="State/Province" v-model="form.personal_info.state_of_origin" :class="errorClass('state_of_origin')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Phone Number <span class="text-red-500">*</span></label>
                                    <input type="tel" v-model="form.personal_info.phone" readonly :class="errorClass('phone')" class="block w-full rounded-lg bg-gray-100 text-gray-600 shadow-sm sm:text-sm cursor-not-allowed">
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">WhatsApp Number</label>
                                    <input type="tel" v-model="form.personal_info.whatsapp_number" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                <div class="md:col-span-2">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Email Address <span class="text-red-500">*</span></label>
                                    <input type="email" v-model="form.personal_info.email" readonly :class="errorClass('email')" class="block w-full rounded-lg bg-gray-100 text-gray-600 shadow-sm sm:text-sm cursor-not-allowed">
                                </div>
                                <div class="md:col-span-2">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Residential Address <span class="text-red-500">*</span></label>
                                    <input type="text" v-model="form.personal_info.address" :class="errorClass('address')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                
                                <div class="col-span-1 md:col-span-2 mt-4 bg-white p-5 rounded-xl border border-gray-100 shadow-sm flex flex-col sm:flex-row gap-6 items-center">
                                    <div class="w-28 h-28 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden flex-shrink-0 border border-gray-200">
                                        <img v-if="passportPreview" :src="passportPreview" class="w-full h-full object-cover" />
                                        <svg v-else class="w-10 h-10 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                                    </div>
                                    <div class="flex-1 w-full text-center sm:text-left">
                                        <h4 class="font-bold text-gray-800 text-sm mb-1">Passport Photograph <span class="text-red-500">*</span></h4>
                                        <p class="text-xs text-gray-500 mb-4">Upload a recent, clear passport-sized photograph. Max 500KB (JPG/PNG).</p>
                                        <div class="flex justify-center sm:justify-start">
                                            <label for="passport_upload" class="cursor-pointer inline-flex items-center gap-1.5 text-xs font-bold text-noun-green hover:text-noun-dark bg-green-50 hover:bg-green-100 px-4 py-2 rounded-full transition-colors border border-green-200 shadow-sm" :class="errorClass('passport_photograph')">
                                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
                                                Choose Image
                                            </label>
                                            <input id="passport_upload" type="file" accept="image/jpeg, image/png" @change="handlePassportUpload" class="hidden">
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>

                        <!-- STEP 3: Academics -->
                        <div v-show="currentStep === 3" class="space-y-6">
                            <div v-if="isExecutiveCert">
                                <h3 class="text-xl font-bold text-gray-900">Academic Background (Optional)</h3>
                                <p class="text-sm text-gray-500 mt-1">Executive Certificates only require relevant work experience, but you may provide academic history.</p>
                            </div>
                            <div v-else>
                                <h3 class="text-xl font-bold text-gray-900">Academic Background & O'Level</h3>
                                <p class="text-sm text-gray-500 mt-1">List your higher education qualifications and secondary school results.</p>
                            </div>

                            <div v-for="(edu, index) in form.academic_background" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl">
                                <div class="flex justify-between items-center mb-4">
                                    <h4 class="font-semibold text-gray-900">Qualification #{{ index + 1 }}</h4>
                                    <button v-if="index > 0" type="button" @click="removeAcademic(index)" class="text-xs text-red-500 hover:text-red-700 font-bold flex items-center gap-1 transition">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                        Remove Qualification
                                    </button>
                                </div>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-xs font-medium text-gray-700 mb-1">Institution <span class="text-red-500">*</span></label>
                                        <input type="text" v-model="edu.institution" :class="errorClass('edu_institution_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-medium text-gray-700 mb-1">Qualification <span class="text-red-500">*</span></label>
                                        <select v-model="edu.qualification" :class="errorClass('edu_qualification_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green py-2">
                                            <option value="">Select Qualification...</option>
                                            <option v-for="q in qualifications" :key="q" :value="q">{{ q }}</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-xs font-medium text-gray-700 mb-1">Course of Study <span class="text-red-500">*</span></label>
                                        <input type="text" v-model="edu.course_of_study" :class="errorClass('edu_course_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-medium text-gray-700 mb-1">Grade / Classification <span class="text-red-500">*</span></label>
                                        <select v-model="edu.grade" :class="errorClass('edu_grade_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green py-2">
                                            <option value="">Select Grade...</option>
                                            <option v-for="g in degreeGrades" :key="g" :value="g">{{ g }}</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <button type="button" @click="addAcademic" class="text-sm font-semibold text-noun-green hover:text-noun-dark transition">+ Add another qualification</button>

                            <div v-if="!isExecutiveCert && !isDBA">
                                <hr class="my-8 border-gray-200">
                                <h4 class="font-semibold text-gray-900 mb-4">O'Level Results</h4>
                                <div v-for="(olevel, index) in form.olevel_results" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl mb-4 relative">
                                    <div class="flex items-center justify-between mb-4">
                                        <h4 class="font-medium text-gray-800">Sitting #{{ olevel.sitting }}</h4>
                                        <button v-if="index > 0" type="button" @click="removeOlevel(index)" class="text-xs text-red-500 hover:text-red-700 font-bold flex items-center gap-1 transition">
                                            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                            Remove Sitting
                                        </button>
                                    </div>
                                    <div class="grid grid-cols-3 gap-4 mb-5">
                                        <div>
                                            <label class="block text-xs font-medium text-gray-700 mb-1">Exam Type <span class="text-red-500">*</span></label>
                                            <select v-model="olevel.exam_type" :class="errorClass('olevel_type_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green py-2">
                                                <option value="">Select...</option>
                                                <option v-for="type in examTypes" :key="type" :value="type">{{ type }}</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label class="block text-xs font-medium text-gray-700 mb-1">Exam Year <span class="text-red-500">*</span></label>
                                            <input type="number" min="1980" max="2030" v-model="olevel.exam_year" :class="errorClass('olevel_year_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green">
                                        </div>
                                        <div>
                                            <label class="block text-xs font-medium text-gray-700 mb-1">Exam Number <span class="text-red-500">*</span></label>
                                            <input type="text" v-model="olevel.exam_number" :class="errorClass('olevel_number_'+index)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green">
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-3" v-for="(sub, subIdx) in olevel.subjects" :key="subIdx">
                                        <select v-model="sub.name" :disabled="subIdx === 0 || subIdx === 1" :class="[errorClass('olevel_sub_name_'+index+'_'+subIdx), subIdx === 0 || subIdx === 1 ? 'bg-gray-100 cursor-not-allowed text-gray-600' : '']" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green py-2">
                                            <option value="">Select Subject...</option>
                                            <option v-for="subject in olevelSubjects" :key="subject" :value="subject">{{ subject }}</option>
                                            <option value="Other">Other...</option>
                                        </select>
                                        <select v-model="sub.grade" :class="errorClass('olevel_sub_grade_'+index+'_'+subIdx)" class="block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green py-2">
                                            <option value="">Select Grade...</option>
                                            <option v-for="grade in olevelGrades" :key="grade" :value="grade">{{ grade }}</option>
                                        </select>
                                    </div>
                                </div>
                                <button type="button" v-if="form.olevel_results.length < 2" @click="addOlevel" class="text-sm font-semibold text-noun-green hover:text-noun-dark transition">+ Add second sitting</button>
                            </div>
                        </div>
                        
                        <!-- STEP 4: Experience & Documents -->
                        <div v-show="currentStep === 4" class="space-y-6">
                            <div>
                                <h3 class="text-xl font-bold text-gray-900">Employment & Documents</h3>
                                <p class="text-sm text-gray-500 mt-1">Provide your current employment details and upload required documents.</p>
                            </div>
                            
                            <div class="bg-gray-50 p-5 rounded-xl border border-gray-200">
                                <h4 class="font-semibold text-gray-900 mb-4">Current Employment (<span class="text-red-500">*</span> Required)</h4>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1.5">Organisation <span class="text-red-500">*</span></label>
                                        <input type="text" v-model="form.employment_info.organisation" :class="errorClass('emp_organisation')" class="block w-full rounded-lg shadow-sm focus:border-noun-green sm:text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1.5">Job Title <span class="text-red-500">*</span></label>
                                        <input type="text" v-model="form.employment_info.job_title" :class="errorClass('emp_job_title')" class="block w-full rounded-lg shadow-sm focus:border-noun-green sm:text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1.5">Years of Experience <span class="text-red-500">*</span></label>
                                        <input type="number" v-model="form.employment_info.years_experience" :class="errorClass('emp_years')" class="block w-full rounded-lg shadow-sm focus:border-noun-green sm:text-sm">
                                    </div>
                                </div>
                            </div>

                            <div>
                                <h4 class="font-semibold text-gray-900 mb-4">Required Documents</h4>
                                <div v-for="req in programmeRequirements" :key="req.id">
                                    <div v-if="req.is_document == 1 || req.is_document === true || req.is_document === '1'" class="mb-6 bg-white p-4 rounded-xl border border-gray-100 shadow-sm">
                                        <div class="flex justify-between items-start mb-3">
                                            <label class="block text-sm font-medium text-gray-800">{{ req.description }} <span class="text-red-500">*</span></label>
                                            <span class="text-[10px] uppercase font-bold text-gray-400 bg-gray-100 px-2 py-1 rounded">Max 500KB</span>
                                        </div>
                                        
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
                                        
                                        <div v-if="!form.documents[req.description] || form.documents[req.description].length === 0" class="text-xs text-gray-400 italic mb-3">No documents attached yet. (Max 500KB. Formats: PDF, JPG, PNG)</div>

                                        <div class="flex items-center gap-2">
                                            <label :for="'file_' + req.id" class="cursor-pointer inline-flex items-center gap-1.5 text-xs font-bold text-noun-green hover:text-noun-dark bg-green-50 hover:bg-green-100 px-4 py-2 rounded-full transition-colors border border-green-200 shadow-sm" :class="errorClass('doc_' + req.id)">
                                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                                                {{ form.documents[req.description] && form.documents[req.description].length > 0 ? 'Add another document' : 'Attach Document' }}
                                            </label>
                                            <input :id="'file_' + req.id" type="file" accept=".pdf,.jpg,.jpeg,.png" class="hidden" @change="e => handleFileSelect(e, req.description)">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Navigation Buttons -->
                        <div class="mt-8 pt-6 border-t border-gray-200 flex justify-between items-center">
                            <button type="button" :class="[currentStep === 1 ? 'invisible' : '']" @click="prevStep" class="px-5 py-2.5 bg-white border border-gray-300 text-gray-700 text-sm font-semibold rounded-lg hover:bg-gray-50 transition shadow-sm">
                                Back
                            </button>

                            <button type="button" v-if="currentStep < totalSteps" @click="nextStep" class="px-6 py-2.5 bg-noun-green text-white text-sm font-semibold rounded-lg hover:bg-noun-dark transition shadow-sm">
                                Continue Step {{ currentStep + 1 }}
                            </button>
                            
                            <button type="submit" v-if="currentStep === totalSteps" class="px-8 py-2.5 bg-noun-yellow text-noun-dark text-sm font-bold rounded-lg hover:bg-yellow-400 transition shadow-sm" :disabled="form.processing">
                                Submit Application
                            </button>
                        </div>
                    </form>

                </div>
            </div>
        </div>
    </AuthenticatedLayout>
</template>
