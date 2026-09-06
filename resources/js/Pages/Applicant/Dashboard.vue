<script setup>
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { computed } from 'vue';
import StudentDashboard from '@/Components/StudentDashboard.vue';

const props = defineProps({
    application: Object,
    is_student: Boolean,
    wallet_balance: Number,
    transactions: Array,
    activeSession: Object,
    hasRegisteredSemester: Boolean,
    registeredCourses: Array,
    availableCourses: Array,
});

const currentStep = computed(() => {
    if (!props.application) return 0;
    const status = props.application.status;
    if (status === 'STARTED') return 1;
    if (status === 'DRAFT' || status === 'SUBMITTED') return 2;
    if (['UNDER REVIEW', 'SHORTLISTED', 'SCREENING', 'RECOMMENDED'].includes(status)) return 3;
    if (status === 'ADMITTED') return 4;
    if (status === 'REJECTED') return 4;
    if (status === 'ENROLLED') return 5;
    return 1;
});

const steps = [
    { id: 1, name: 'Application form', description: 'Fill your details' },
    { id: 2, name: 'Application Fee', description: 'Pay N25,000 via Remita' },
    { id: 3, name: 'Under Review', description: 'Screening by admissions' },
    { id: 4, name: 'Decision', description: 'Admission outcome' },
    { id: 5, name: 'Enrollment', description: 'Accept offer & Register' },
];

const payForm = useForm({
    type: 'ACCEPTANCE_FEE'
});
</script>

<template>
    <Head title="Applicant Dashboard" />

    <AuthenticatedLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">
                Admission Tracker
            </h2>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8 space-y-6">

                <div v-if="$page.props.flash && $page.props.flash.success" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg relative">
                    {{ $page.props.flash.success }}
                </div>

                <!-- Welcome Banner -->
                <div class="bg-noun-dark rounded-xl overflow-hidden shadow-sm">
                    <div class="px-8 py-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
                            <div v-if="$page.props.auth.user.passport_url" class="h-16 w-16 sm:h-20 sm:w-20 rounded-full border-2 border-noun-yellow shadow-lg overflow-hidden shrink-0 bg-gray-50">
                                <img :src="$page.props.auth.user.passport_url" class="h-full w-full object-cover" alt="Passport" />
                            </div>
                            <div>
                                <p class="text-noun-yellow text-sm font-medium uppercase tracking-wider mb-1">NOUN Business School</p>
                                <h3 class="text-2xl font-bold text-white">Welcome, {{ $page.props.auth.user.first_name }}!</h3>
                            <p class="mt-2 text-green-300 text-sm max-w-md">
                                Track your admission progress and complete any pending registrations.
                            </p>
                            </div>
                        </div>
                        <a
                            v-if="!application"
                            href="/apply"
                            class="flex-shrink-0 inline-flex items-center gap-2 px-6 py-3 bg-noun-yellow text-noun-dark font-bold rounded-lg hover:bg-yellow-400 transition shadow-md text-sm"
                        >
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            Start Application
                        </a>
                    </div>
                    <div class="h-1 bg-gradient-to-r from-noun-green via-noun-yellow to-noun-green"></div>
                </div>

                <div v-if="application" class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <!-- Tracker Visual -->
                    <div class="lg:col-span-1 bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                        <h3 class="font-bold text-gray-900 mb-6 text-lg border-b pb-3 border-gray-100">Progress Tracker</h3>
                        
                        <div class="relative">
                            <div class="absolute inset-0 left-4 w-0.5 bg-gray-200" aria-hidden="true"></div>
                            <ul role="list" class="space-y-8 relative">
                                <li v-for="step in steps" :key="step.id">
                                    <div class="relative flex items-start group">
                                        <div class="h-9 flex items-center">
                                            <span 
                                                class="relative z-10 w-8 h-8 flex items-center justify-center rounded-full border-2 transition-colors duration-200"
                                                :class="[
                                                    currentStep > step.id ? 'bg-noun-green border-noun-green' : 
                                                    currentStep === step.id ? 'bg-white border-noun-green' : 
                                                    'bg-white border-gray-300'
                                                ]"
                                            >
                                                <!-- Completed -->
                                                <svg v-if="currentStep > step.id" class="w-5 h-5 text-white" viewBox="0 0 20 20" fill="currentColor">
                                                    <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd" />
                                                </svg>
                                                <!-- Current -->
                                                <span v-else-if="currentStep === step.id" class="h-2.5 w-2.5 bg-noun-green rounded-full"></span>
                                            </span>
                                        </div>
                                        <div class="ml-4 min-w-0 flex flex-col">
                                            <span 
                                                class="text-sm font-semibold tracking-wide"
                                                :class="currentStep >= step.id ? 'text-noun-dark' : 'text-gray-500'"
                                            >{{ step.name }}</span>
                                            <span class="text-xs text-gray-500">{{ step.description }}</span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- Action Area -->
                    <div class="lg:col-span-2 space-y-6">
                        <!-- Application Info -->
                        <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
                            <div class="flex items-center justify-between mb-4 pb-4 border-b border-gray-100">
                                <div>
                                    <h3 class="font-bold text-gray-900 text-lg">Application Details</h3>
                                    <p class="text-sm text-gray-500 mt-0.5">{{ application.programme?.name }}</p>
                                </div>
                                <span class="px-3 py-1 inline-flex text-xs leading-5 font-bold rounded-full border uppercase"
                                    :class="[
                                        application.status === 'STARTED' ? 'bg-yellow-50 text-yellow-800 border-yellow-200' : 
                                        application.status === 'ADMITTED' ? 'bg-green-50 text-green-800 border-green-200' :
                                        application.status === 'ENROLLED' ? 'bg-purple-50 text-purple-800 border-purple-200' :
                                        application.status === 'REJECTED' ? 'bg-red-50 text-red-800 border-red-200' :
                                        'bg-blue-50 text-blue-800 border-blue-200'
                                    ]">
                                    {{ application.status }}
                                </span>
                            </div>
                            
                            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                                <div>
                                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">App Number</p>
                                    <p class="font-semibold text-gray-900">{{ application.application_number || 'Pending' }}</p>
                                </div>
                                <div v-if="application.specialisation">
                                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Specialisation</p>
                                    <p class="font-semibold text-gray-900">{{ application.specialisation.name }}</p>
                                </div>
                                <div>
                                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Submitted On</p>
                                    <p class="font-semibold text-gray-900">{{ new Date(application.created_at).toLocaleDateString() }}</p>
                                </div>
                                <div v-if="application.status !== 'STARTED'" class="flex items-end">
                                    <a :href="route('applicant.application.docket')" target="_blank" class="text-noun-green hover:text-green-700 font-semibold text-sm underline flex items-center gap-1 mt-2">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                        Print Form Docket
                                    </a>
                                </div>
                            </div>
                        </div>

                        <!-- Current Action Required -->
                        <div v-if="application.status === 'STARTED'" class="bg-yellow-50 rounded-xl border border-yellow-200 p-6 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-6">
                            <div>
                                <h4 class="font-bold text-yellow-900 text-lg flex items-center gap-2">
                                    <svg class="h-5 w-5 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                    </svg>
                                    Action Required: Pay Application Fee
                                </h4>
                                <p class="text-sm text-yellow-800 mt-2 leading-relaxed">
                                    Your application has been drafted successfully. To officially submit it to the admissions board, you must pay the non-refundable application fee of <strong>NGN 25,000</strong>.
                                </p>
                            </div>
                            <a :href="route('applicant.payment.initiate')" class="inline-flex justify-center items-center gap-2 px-6 py-3 bg-noun-yellow text-noun-dark font-bold rounded-lg hover:bg-yellow-400 transition shadow-sm whitespace-nowrap">
                                Pay via Remita
                            </a>
                        </div>
                        
                        <div v-else-if="currentStep === 3" class="bg-blue-50 border border-blue-200 rounded-xl p-6 shadow-sm">
                            <h4 class="font-bold text-blue-900 text-lg flex items-center gap-2">
                                <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                Application Under Review
                            </h4>
                            <p class="text-sm text-blue-800 mt-2 leading-relaxed">
                                We have successfully received your application fee and documentation. The admissions committee is currently reviewing your file. You will be notified via email once a decision has been made.
                            </p>
                        </div>

                        <div v-else-if="application.status === 'ADMITTED'" class="bg-green-50 border border-green-200 rounded-xl p-6 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-6">
                            <div>
                                <h4 class="font-bold text-green-900 text-lg flex items-center gap-2">
                                    <svg class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                    </svg>
                                    Congratulations! You've been Admitted.
                                </h4>
                                <p class="text-sm text-green-800 mt-2 leading-relaxed">
                                    You have been offered admission into the programme. The next step is to accept the offer and pay your Acceptance Fee of <strong>NGN 50,000</strong> to secure your spot and generate your matriculation number.
                                </p>
                            </div>
                            <div class="flex-shrink-0">
                                <a :href="route('applicant.payment.initiate', {type: 'ACCEPTANCE_FEE'})" class="inline-flex justify-center items-center gap-2 px-6 py-3 bg-noun-green text-white font-bold rounded-lg hover:bg-green-700 transition shadow-sm whitespace-nowrap">
                                    Pay Acceptance Fee
                                </a>
                            </div>
                        </div>

                        <div v-else-if="application.status === 'ENROLLED'" class="space-y-6">
                            <!-- Matric Card -->
                            <div class="rounded-2xl overflow-hidden shadow-sm">
                                <div class="bg-gradient-to-r from-noun-dark to-noun-green px-6 py-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                                    <div>
                                        <p class="text-green-300 text-xs font-semibold uppercase tracking-widest mb-1">Matriculation Number</p>
                                        <p class="text-2xl sm:text-3xl font-black text-white tracking-widest font-mono">NBS/{{ application.academic_session_id }}/{{ String(application.id).padStart(4, '0') }}</p>
                                        <p class="text-green-300 text-xs mt-1">{{ application.programme?.name }}</p>
                                    </div>
                                    <div class="flex flex-col sm:items-end gap-2">
                                        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-noun-yellow text-noun-dark rounded-full text-xs font-black uppercase tracking-wide">
                                            <span class="w-1.5 h-1.5 rounded-full bg-noun-dark animate-pulse"></span>
                                            Enrolled
                                        </span>
                                    </div>
                                </div>
                                <div class="h-1 bg-gradient-to-r from-noun-yellow via-noun-gold to-noun-yellow"></div>
                            </div>

                            <!-- Massive Admission Letter CTA -->
                            <div class="bg-green-50 border border-green-200 rounded-2xl p-6 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-6">
                                <div>
                                    <h4 class="font-bold text-green-900 text-lg flex items-center gap-2">
                                        <svg class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                        </svg>
                                        Official Admission Letter
                                    </h4>
                                    <p class="text-sm text-green-800 mt-2">
                                        Please download and print your official admission letter. You will need a physical copy of this document for your physical clearance and final registration at the study centre.
                                    </p>
                                </div>
                                <a :href="route('applicant.application.letter')" target="_blank" class="flex-shrink-0 inline-flex items-center gap-2 px-6 py-3 bg-noun-green text-white font-bold rounded-xl hover:bg-noun-dark transition shadow-md whitespace-nowrap">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                    Download Letter
                                </a>
                            </div>
                            <!-- Inject the Student Portal -->
                            <StudentDashboard v-if="is_student" v-bind="$props" />
                        </div>

                        <div v-else-if="application.status === 'REJECTED'" class="bg-red-50 border border-red-200 rounded-xl p-6 shadow-sm">
                            <h4 class="font-bold text-red-900 text-lg flex items-center gap-2">
                                <svg class="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                Admission Unsuccessful
                            </h4>
                            <p class="text-sm text-red-800 mt-2 leading-relaxed">
                                We regret to inform you that your application was not successful for this academic session. We encourage you to apply again during the next intake.
                            </p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </AuthenticatedLayout>
</template>
