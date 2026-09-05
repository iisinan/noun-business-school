import re

vue_content = """<script setup>
import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { computed } from 'vue';

const props = defineProps({
    application: Object
});

const statusColor = {
    'STARTED': 'bg-yellow-100 text-yellow-800',
    'SUBMITTED': 'bg-blue-100 text-blue-800',
    'UNDER REVIEW': 'bg-purple-100 text-purple-800',
    'SHORTLISTED': 'bg-indigo-100 text-indigo-800',
    'SCREENING': 'bg-teal-100 text-teal-800',
    'RECOMMENDED': 'bg-green-100 text-green-700',
    'ADMITTED': 'bg-green-100 text-green-800',
    'ENROLLED': 'bg-emerald-100 text-emerald-800',
    'REJECTED': 'bg-red-100 text-red-800'
};

const statusForm = useForm({
    status: props.application.status
});

const updateStatus = () => {
    statusForm.post(route('admin.applications.updateStatus', props.application.id), {
        preserveScroll: true
    });
};
</script>

<template>
    <Head :title="'Application - ' + (application.application_number || 'Pending')" />

    <AuthenticatedLayout>
        <template #header>
            <div class="flex items-center gap-3">
                <Link :href="route('admin.applications.index')" class="text-gray-400 hover:text-noun-green transition">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                    </svg>
                </Link>
                <div>
                    <h2 class="text-xl font-semibold leading-tight text-gray-800">
                        Application: <span class="font-mono text-noun-green">{{ application.application_number || 'Pending' }}</span>
                    </h2>
                </div>
            </div>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-3 gap-6">

                <!-- Application Details -->
                <div class="lg:col-span-2 space-y-5">
                    
                    <!-- Applicant Header -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100 flex items-center gap-3 bg-gray-50">
                            <div class="h-10 w-10 rounded-full bg-noun-dark flex items-center justify-center text-white text-sm font-bold">
                                {{ application.user.first_name?.charAt(0) }}{{ application.user.last_name?.charAt(0) }}
                            </div>
                            <div>
                                <h3 class="text-base font-semibold text-gray-900">{{ application.user.first_name }} {{ application.user.last_name }}</h3>
                                <p class="text-sm text-gray-500">{{ application.user.email }}</p>
                            </div>
                            <span class="ml-auto px-2.5 py-1 text-xs font-bold rounded-full uppercase tracking-wider" :class="statusColor[application.status] || 'bg-gray-100 text-gray-700'">
                                {{ application.status }}
                            </span>
                        </div>
                        <div class="px-6 py-4 grid grid-cols-2 sm:grid-cols-3 gap-4 border-b border-gray-100">
                            <div>
                                <div class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Programme</div>
                                <div class="mt-1 text-sm text-gray-800 font-medium">{{ application.programme.name }}</div>
                            </div>
                            <div v-if="application.specialisation">
                                <div class="text-xs font-semibold text-gray-400 uppercase tracking-wider">Specialisation</div>
                                <div class="mt-1 text-sm text-gray-800">{{ application.specialisation.name }}</div>
                            </div>
                        </div>
                        
                        <!-- Personal Info -->
                        <div class="px-6 py-4" v-if="application.personal_info">
                            <h3 class="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wider border-b pb-2">Personal Information</h3>
                            <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                                <div>
                                    <div class="text-xs text-gray-500">Gender</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.gender === 'M' ? 'Male' : (application.personal_info.gender === 'F' ? 'Female' : application.personal_info.gender) }}</div>
                                </div>
                                <div>
                                    <div class="text-xs text-gray-500">Marital Status</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.marital_status }}</div>
                                </div>
                                <div>
                                    <div class="text-xs text-gray-500">Date of Birth</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.dob }}</div>
                                </div>
                                <div>
                                    <div class="text-xs text-gray-500">Phone</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.phone }}</div>
                                </div>
                                <div>
                                    <div class="text-xs text-gray-500">Nationality</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.nationality === 'Other' ? application.personal_info.nationality_other : application.personal_info.nationality }}</div>
                                </div>
                                <div>
                                    <div class="text-xs text-gray-500">State of Origin</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.state_of_origin }}</div>
                                </div>
                                <div class="col-span-2 md:col-span-3">
                                    <div class="text-xs text-gray-500">Address</div>
                                    <div class="text-sm font-medium">{{ application.personal_info.address }}</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Academic & OLevel -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100">
                            <h3 class="text-sm font-bold text-gray-900 uppercase tracking-wider">Academic Background</h3>
                        </div>
                        <div class="px-6 py-4" v-if="application.academic_background">
                            <div v-for="(edu, idx) in application.academic_background" :key="idx" class="mb-4 last:mb-0 bg-gray-50 p-4 rounded-lg border border-gray-100">
                                <h4 class="font-bold text-gray-900 mb-2">{{ edu.institution }}</h4>
                                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                                    <div>
                                        <div class="text-xs text-gray-500">Qualification</div>
                                        <div class="text-sm font-medium">{{ edu.qualification }}</div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-gray-500">Course of Study</div>
                                        <div class="text-sm font-medium">{{ edu.course_of_study }}</div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-gray-500">Graduation Year</div>
                                        <div class="text-sm font-medium">{{ edu.graduation_year || 'N/A' }}</div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-gray-500">Grade / Class</div>
                                        <div class="text-sm font-medium">{{ edu.grade }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- OLevel -->
                        <div class="px-6 py-4 border-t border-gray-100" v-if="application.olevel_results && application.olevel_results.length > 0">
                            <h3 class="text-sm font-bold text-gray-900 uppercase tracking-wider mb-3">O'Level Results</h3>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div v-for="(olevel, idx) in application.olevel_results" :key="idx" class="bg-gray-50 p-4 rounded-lg border border-gray-100">
                                    <div class="flex justify-between items-center mb-3 pb-2 border-b border-gray-200">
                                        <span class="font-bold text-gray-800">{{ olevel.exam_type }} ({{ olevel.exam_year }})</span>
                                        <span class="text-xs text-gray-500 font-mono">No: {{ olevel.exam_number }}</span>
                                    </div>
                                    <table class="w-full text-sm">
                                        <tbody>
                                            <tr v-for="(sub, sIdx) in olevel.subjects" :key="sIdx">
                                                <td v-if="sub.name && sub.grade" class="py-1 text-gray-600">{{ sub.name }}</td>
                                                <td v-if="sub.name && sub.grade" class="py-1 text-right font-bold text-gray-900">{{ sub.grade }}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Employment & Documents -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100">
                            <h3 class="text-sm font-bold text-gray-900 uppercase tracking-wider">Employment & Documents</h3>
                        </div>
                        <div class="px-6 py-4 grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- Employment -->
                            <div>
                                <h4 class="text-sm font-bold text-gray-700 mb-3 border-b pb-1">Current Employment</h4>
                                <div v-if="application.employment_info" class="space-y-3">
                                    <div>
                                        <div class="text-xs text-gray-500">Organisation</div>
                                        <div class="text-sm font-medium">{{ application.employment_info.organisation || 'N/A' }}</div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-gray-500">Job Title</div>
                                        <div class="text-sm font-medium">{{ application.employment_info.job_title || 'N/A' }}</div>
                                    </div>
                                    <div>
                                        <div class="text-xs text-gray-500">Years of Experience</div>
                                        <div class="text-sm font-medium">{{ application.employment_info.years_experience || 'N/A' }}</div>
                                    </div>
                                </div>
                            </div>

                            <!-- Documents -->
                            <div>
                                <h4 class="text-sm font-bold text-gray-700 mb-3 border-b pb-1">Uploaded Documents</h4>
                                <div v-if="application.documents" class="space-y-2">
                                    <div v-for="(path, desc) in application.documents" :key="desc" class="flex items-center justify-between text-sm">
                                        <span class="text-gray-600 truncate max-w-[200px]" :title="desc">{{ desc }}</span>
                                        <a :href="'/storage/' + path" target="_blank" class="text-noun-green hover:underline font-medium text-xs flex items-center gap-1">
                                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                            View
                                        </a>
                                    </div>
                                </div>
                                <div v-else class="text-sm text-gray-400 italic">No documents uploaded.</div>
                            </div>
                        </div>
                    </div>
                    
                </div>

                <!-- Admin Controls -->
                <div class="space-y-5">
                    <!-- Admissions Decision -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100 bg-noun-dark">
                            <h3 class="text-sm font-semibold text-white">Admissions Decision</h3>
                        </div>
                        <div class="px-6 py-5">
                            <form @submit.prevent="updateStatus">
                                <div class="mb-4">
                                    <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">Update Status</label>
                                    <select v-model="statusForm.status" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green text-sm">
                                        <option value="STARTED">Started (Incomplete)</option>
                                        <option value="SUBMITTED">Submitted (Fee Paid)</option>
                                        <option value="UNDER REVIEW">Under Review</option>
                                        <option value="SHORTLISTED">Shortlisted</option>
                                        <option value="SCREENING">Screening/Interview</option>
                                        <option value="RECOMMENDED">Recommended</option>
                                        <option value="ADMITTED">Admitted</option>
                                        <option value="ENROLLED">Enrolled</option>
                                        <option value="REJECTED">Rejected</option>
                                    </select>
                                </div>

                                <button
                                    type="submit"
                                    :disabled="statusForm.processing"
                                    class="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg text-sm font-semibold text-white bg-noun-green hover:bg-noun-dark transition disabled:opacity-50 shadow-md"
                                >
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    Update Status
                                </button>
                            </form>
                        </div>
                    </div>

                    <!-- Payment Status -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100">
                            <h3 class="text-sm font-semibold text-gray-700">Payment Records</h3>
                        </div>
                        <div class="px-6 py-4">
                            <div v-if="application.payments.length > 0" class="space-y-3">
                                <div v-for="payment in application.payments" :key="payment.id" class="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                                    <div>
                                        <div class="text-sm font-medium text-gray-800">{{ payment.payment_type }}</div>
                                        <div class="text-xs text-gray-500">NGN {{ payment.amount }}</div>
                                    </div>
                                    <span class="text-xs font-semibold px-2 py-0.5 rounded-full"
                                          :class="payment.status === 'PAID' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'">
                                        {{ payment.status }}
                                    </span>
                                </div>
                            </div>
                            <div v-else class="py-4 text-center text-sm text-gray-400">
                                No payment records found.
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </AuthenticatedLayout>
</template>
"""

with open("resources/js/Pages/Admin/Applications/Show.vue", "w") as f:
    f.write(vue_content)

