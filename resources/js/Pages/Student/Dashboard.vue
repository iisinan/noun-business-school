<script setup>
import StudentLayout from '@/Layouts/StudentLayout.vue';
import { Head } from '@inertiajs/vue3';

import { usePage } from '@inertiajs/vue3';

const props = defineProps({
    wallet_balance: Number,
    transactions: Array,
    activeSession: Object,
    hasRegisteredSemester: Boolean,
    registeredCourses: Array,
    availableCourses: Array,
    application: Object
});

const page = usePage();
const user = page.props.auth.user;

</script>

<template>
    <Head title="Student Portal" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Student Portal</h2>
        </template>

        <div class="py-12 bg-gray-50/50 min-h-screen">
            <div class=" sm:px-6 lg:px-8">
                
                <div class="space-y-6">
                    <!-- Matric Card -->
                    <div class="rounded-2xl overflow-hidden shadow-sm">
                        <div class="bg-gradient-to-r from-noun-dark to-noun-green px-6 py-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                            <div>
                                <p class="text-green-300 text-xs font-semibold uppercase tracking-widest mb-1">Matriculation Number</p>
                                <p class="text-2xl sm:text-3xl font-black text-white tracking-widest font-mono">NBS/{{ application?.academic_session_id || activeSession?.id || '...' }}/{{ String(application?.id || user.id).padStart(4, '0') }}</p>
                                <p class="text-green-300 text-xs mt-1">{{ application?.programme?.name || 'Admitted Student' }}</p>
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

                    
                    

                    <!-- Quick Links -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                        <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
                            <h3 class="font-bold text-gray-800 text-lg mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                                Academics
                            </h3>
                            <p class="text-sm text-gray-500 mb-4">Register for your semester courses or check your latest examination results.</p>
                            <a :href="route('student.registration')" class="text-sm font-bold text-noun-green hover:text-noun-dark">Go to Course Registration &rarr;</a>
                        </div>
                        
                        <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
                            <h3 class="font-bold text-gray-800 text-lg mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                                Finances
                            </h3>
                            <p class="text-sm text-gray-500 mb-4">View your wallet transactions and payment history for the academic year.</p>
                            <Link :href="route('student.payments')" class="text-sm font-bold text-noun-green hover:underline">View Payment History &rarr;</Link>
                        </div>
                    </div>

                </div>

            </div>
        </div>
    </StudentLayout>
</template>
