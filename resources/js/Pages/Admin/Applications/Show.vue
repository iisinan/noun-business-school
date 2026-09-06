<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import Modal from '@/Components/Modal.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { computed, ref } from 'vue';

const viewingDocumentUrl = ref(null);
const isDocumentModalOpen = ref(false);

const openDocument = (url) => {
    viewingDocumentUrl.value = url;
    isDocumentModalOpen.value = true;
};

const closeDocument = () => {
    isDocumentModalOpen.value = false;
    setTimeout(() => { viewingDocumentUrl.value = null; }, 300);
};

const props = defineProps({
    application: Object
});

const admissionRequirements = computed(() => {
    const type = props.application?.programme?.type;
    
    if (type === 'GDBA') {
        return [
            "Bachelor's Degree (minimum Third Class) or HND (minimum Lower Credit).",
            "NYSC Discharge or Exemption Certificate.",
            "O'Level results with 5 credits including English and Mathematics."
        ];
    } else if (type === 'MBA') {
        return [
            "Bachelor's Degree (minimum Second Class Lower) or GDBA.",
            "Minimum of 3 years post-graduation work experience.",
            "NYSC Discharge or Exemption Certificate.",
            "O'Level results with 5 credits including English and Mathematics."
        ];
    } else if (type === 'DBA') {
        return [
            "Master's Degree with a minimum CGPA of 3.5 (or 60% average).",
            "Comprehensive Research Proposal.",
            "Previous Master's Dissertation / Thesis.",
            "NYSC Discharge or Exemption Certificate."
        ];
    } else if (type === 'Certificate') {
        return [
            "Minimum of O'Level results with 5 credits.",
            "Relevant work experience in the subject area."
        ];
    }
    
    return ["Standard University admission requirements apply."];
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

    <AdminLayout>
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
            <div class="mx-auto w-full sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-3 gap-6">

                <!-- Application Details -->
                <div class="lg:col-span-2 space-y-5">
                    
                    <!-- Applicant Header -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                        <div class="px-6 py-4 border-b border-gray-100 flex items-center gap-3 bg-gray-50">
                            <div v-if="application.passport_url" class="h-12 w-12 rounded-full flex items-center justify-center shrink-0 border border-gray-200 shadow-sm overflow-hidden bg-gray-50">
                                <img :src="application.passport_url" class="h-full w-full object-cover" alt="Applicant Passport" />
                            </div>
                            <div v-else class="h-12 w-12 rounded-full bg-noun-dark flex items-center justify-center text-white text-sm font-bold shrink-0 shadow-sm">
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
                        <div class="px-6 py-5 flex flex-col md:flex-row gap-4 md:gap-6 border-b border-gray-100 bg-white">
                            <div class="flex-1">
                                <div class="text-[10px] font-bold text-noun-green uppercase tracking-wider mb-1.5 flex items-center gap-1.5"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14v7"/></svg>Programme</div>
                                <div class="text-sm text-noun-dark font-bold bg-green-50/50 px-4 py-2.5 rounded-xl border border-green-100/50 shadow-sm">{{ application.programme.name }}</div>
                            </div>
                            <div class="flex-1" v-if="application.specialisation">
                                <div class="text-[10px] font-bold text-noun-yellow uppercase tracking-wider mb-1.5 flex items-center gap-1.5"><svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>Specialisation</div>
                                <div class="text-sm text-noun-dark font-bold bg-yellow-50/50 px-4 py-2.5 rounded-xl border border-yellow-100/50 shadow-sm">{{ application.specialisation.name }}</div>
                            </div>
                        </div>
                        
                        <!-- Personal Info -->
                        <div class="px-6 py-6 bg-gray-50/30" v-if="application.personal_info">
                            <h3 class="text-[11px] font-black text-gray-400 mb-5 uppercase tracking-widest flex items-center gap-2">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                Personal Information
                            </h3>
                            <div class="grid grid-cols-2 md:grid-cols-3 gap-y-6 gap-x-4">
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
                        <div class="px-6 py-4 border-b border-gray-100 bg-gray-50/50 flex items-center gap-2">
                            <svg class="w-4 h-4 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l9-5-9-5-9 5 9 5zm0 0v7"></path></svg>
                            <h3 class="text-xs font-bold text-gray-900 uppercase tracking-widest">Academic Background</h3>
                        </div>
                        <div class="px-6 py-5" v-if="application.academic_background">
                            <div v-for="(edu, idx) in application.academic_background" :key="idx" class="mb-5 last:mb-0 bg-white border border-gray-100 rounded-xl overflow-hidden shadow-sm">
                                <div class="px-5 py-3 border-b border-gray-50 bg-gray-50/50 flex items-center gap-2">
                                    <div class="w-6 h-6 rounded bg-noun-green/10 flex items-center justify-center">
                                        <svg class="w-3.5 h-3.5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                                    </div>
                                    <h4 class="font-bold text-gray-900">{{ edu.institution }}</h4>
                                </div>
                                <div class="p-5 grid grid-cols-2 md:grid-cols-4 gap-y-4 gap-x-6">
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Qualification</div>
                                        <div class="text-sm font-medium text-gray-900">{{ edu.qualification }}</div>
                                    </div>
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Course of Study</div>
                                        <div class="text-sm font-medium text-gray-900">{{ edu.course_of_study }}</div>
                                    </div>
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Graduation Year</div>
                                        <div class="text-sm font-medium text-gray-900">{{ edu.graduation_year || 'N/A' }}</div>
                                    </div>
                                    <div>
                                        <div class="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Grade / Class</div>
                                        <div class="text-sm font-medium text-gray-900">{{ edu.grade }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- OLevel -->
                        <div class="px-6 py-5 border-t border-gray-100 bg-gray-50/30" v-if="application.olevel_results && application.olevel_results.length > 0">
                            <h3 class="text-[11px] font-black text-gray-400 mb-4 uppercase tracking-widest flex items-center gap-2">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                                O'Level Results
                            </h3>
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
                        <div class="px-6 py-4 border-b border-gray-100 bg-gray-50/50 flex items-center gap-2">
                            <svg class="w-4 h-4 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                            <h3 class="text-xs font-bold text-gray-900 uppercase tracking-widest">Employment & Documents</h3>
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
                                <div v-if="application.document_urls && Object.keys(application.document_urls).length > 0" class="space-y-2">
                                    <div v-for="(urlOrUrls, desc) in application.document_urls" :key="desc" class="flex flex-col gap-1 text-sm border-b border-gray-50 pb-2 last:border-0">
                                        <div class="text-gray-600 truncate font-semibold capitalize">{{ desc.replace(/_/g, ' ') }}</div>
                                        
                                        <!-- If multiple documents under same key -->
                                        <template v-if="Array.isArray(urlOrUrls)">
                                            <button v-for="(url, idx) in urlOrUrls" :key="idx" @click.prevent="openDocument(url)" type="button" class="text-noun-green hover:underline font-medium text-xs flex items-center gap-1 pl-2">
                                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                                View Document {{ idx + 1 }}
                                            </button>
                                        </template>
                                        
                                        <!-- Single document -->
                                        <button v-else @click.prevent="openDocument(urlOrUrls)" type="button" class="text-noun-green hover:underline font-medium text-xs flex items-center gap-1 pl-2">
                                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                            View Document
                                        </button>
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
                            <div v-if="application.status === 'STARTED'" class="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                                <div class="flex gap-2">
                                    <svg class="h-5 w-5 text-yellow-600 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                    <div>
                                        <h4 class="text-xs font-bold text-yellow-800 uppercase tracking-wider mb-1">Fee Pending</h4>
                                        <p class="text-xs text-yellow-700">This applicant has not paid the application fee yet. You cannot review or make an admissions decision until payment is complete.</p>
                                    </div>
                                </div>
                            </div>
                            <form v-else @submit.prevent="updateStatus">
                                <div class="mb-4">
                                    <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">Update Status</label>
                                    <select v-model="statusForm.status" @change="updateStatus" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green text-sm">
                                        <option value="UNDER REVIEW">Under Review</option>
                                        <option value="ADMITTED">Admitted</option>
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

                    <!-- Admission Requirements Smart Card -->
                    <div class="bg-indigo-50 border border-indigo-100 rounded-xl shadow-sm overflow-hidden">
                        <div class="px-6 py-4 border-b border-indigo-200 bg-indigo-100 flex items-center gap-2">
                            <svg class="h-5 w-5 text-indigo-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <h3 class="text-sm font-bold text-indigo-900">Smart Requirements Match</h3>
                        </div>
                        <div class="px-6 py-5">
                            <p class="text-xs font-medium text-indigo-800 mb-3 uppercase tracking-wider">For {{ application.programme.type }} Programmes:</p>
                            <ul class="space-y-2">
                                <li v-for="(req, idx) in admissionRequirements" :key="idx" class="flex items-start gap-2 text-sm text-indigo-900">
                                    <svg class="h-5 w-5 text-indigo-500 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    <span class="leading-tight">{{ req }}</span>
                                </li>
                            </ul>
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

        <!-- Document Viewer Modal -->
        <Modal :show="isDocumentModalOpen" @close="closeDocument" maxWidth="4xl">
            <div class="bg-white rounded-lg overflow-hidden flex flex-col h-[85vh]">
                <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between bg-gray-50 shrink-0">
                    <h3 class="text-lg font-bold text-gray-900">Document Viewer</h3>
                    <div class="flex items-center gap-3">
                        <a v-if="viewingDocumentUrl" :href="viewingDocumentUrl" target="_blank" class="text-sm font-semibold text-noun-green hover:underline">Open in new tab</a>
                        <button @click="closeDocument" class="text-gray-400 hover:text-gray-600 transition">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                        </button>
                    </div>
                </div>
                <div class="flex-1 bg-gray-100 p-4 overflow-hidden flex items-center justify-center">
                    <iframe v-if="viewingDocumentUrl" :src="viewingDocumentUrl" class="w-full h-full bg-white rounded shadow-sm border border-gray-200" title="Document Viewer"></iframe>
                </div>
            </div>
        </Modal>

    </AdminLayout>
</template>
