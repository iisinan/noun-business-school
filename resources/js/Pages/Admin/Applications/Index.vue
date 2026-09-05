<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';

const props = defineProps({
    applications: Object,
    programmes: Array,
    filters: Object,
});

const search = ref(props.filters?.search || '');
const status = ref(props.filters?.status || '');
const programme_id = ref(props.filters?.programme_id || '');

let timeout = null;
watch([search, status, programme_id], ([newSearch, newStatus, newProgramme]) => {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => {
        router.get(
            route('admin.applications.index'),
            { search: newSearch, status: newStatus, programme_id: newProgramme },
            { preserveState: true, preserveScroll: true, replace: true }
        );
    }, 300);
});
</script>

<template>
    <Head title="Manage Applications" />

    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">
                Manage Applications
            </h2>
        </template>

        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8">
                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">All Applications</h3>
                            <span class="text-sm text-gray-500">{{ applications.total }} total</span>
                        </div>
                        <div class="flex flex-col sm:flex-row items-center gap-3">
                            <input
                                v-model="search"
                                type="text"
                                placeholder="Search applicant..."
                                class="w-full sm:w-48 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green"
                            />
                            <select v-model="status" class="w-full sm:w-40 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green">
                                <option value="">All Statuses</option>
                                <option value="DRAFT">Draft</option>
                                <option value="SUBMITTED">Submitted</option>
                                <option value="UNDER REVIEW">Under Review</option>
                                <option value="SHORTLISTED">Shortlisted</option>
                                <option value="SCREENING">Screening</option>
                                <option value="RECOMMENDED">Recommended</option>
                                <option value="ADMITTED">Admitted</option>
                                <option value="REJECTED">Rejected</option>
                                <option value="ENROLLED">Enrolled</option>
                            </select>
                            <select v-model="programme_id" class="w-full sm:w-48 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green">
                                <option value="">All Programmes</option>
                                <option v-for="prog in programmes" :key="prog.id" :value="prog.id">{{ prog.name }}</option>
                            </select>
                            <a :href="route('admin.applications.export')" class="shrink-0 inline-flex items-center gap-2 bg-white border border-gray-300 text-gray-700 px-4 py-2 rounded-lg text-sm font-semibold hover:bg-gray-50 transition shadow-sm">
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                                Export CSV
                            </a>
                        </div>
                    </div>

                    <table class="min-w-full divide-y divide-gray-100">
                        <thead>
                            <tr class="bg-gray-50">
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Application No</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Applicant</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Programme</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="app in applications.data" :key="app.id" class="hover:bg-gray-50 transition-colors">
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="inline-flex items-center px-2.5 py-1 rounded-md bg-gray-100 border border-gray-200 text-xs font-mono font-bold text-gray-700">
                                        {{ app.application_number || '—' }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="flex items-center gap-3">
                                        <div class="h-8 w-8 rounded-full bg-noun-dark flex items-center justify-center text-white text-xs font-bold flex-shrink-0">
                                            {{ app.user?.first_name?.charAt(0) }}{{ app.user?.last_name?.charAt(0) }}
                                        </div>
                                        <div>
                                            <div class="text-sm font-medium text-gray-900">{{ app.user?.first_name }} {{ app.user?.last_name }}</div>
                                            <div class="text-xs text-gray-500">{{ app.user?.email }}</div>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-600">{{ app.programme?.name }}</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                          :class="{
                                              'bg-amber-100 text-amber-800': app.status === 'UNDER REVIEW',
                                              'bg-blue-100 text-blue-800': app.status === 'SHORTLISTED',
                                              'bg-green-100 text-noun-dark': app.status === 'ADMITTED',
                                              'bg-gray-100 text-gray-700': app.status === 'STARTED',
                                              'bg-red-100 text-red-800': app.status === 'REJECTED',
                                              'bg-purple-100 text-purple-800': app.status === 'SCREENING',
                                              'bg-emerald-100 text-emerald-800': app.status === 'ENROLLED',
                                          }">
                                        {{ app.status }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                                    <Link
                                        :href="route('admin.applications.show', app.id)"
                                        class="inline-flex items-center justify-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm"
                                    >
                                        Review
                                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </Link>
                                </td>
                            </tr>
                            <tr v-if="applications.data.length === 0">
                                <td colspan="5" class="px-6 py-12 text-center">
                                    <div class="flex flex-col items-center gap-2 text-gray-400">
                                        <svg class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                        </svg>
                                        <span class="text-sm">No applications found.</span>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- Pagination -->
                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-50 flex items-center justify-between">
                        <div class="text-sm text-gray-600">
                            Showing <span class="font-medium">{{ applications.from || 0 }}</span> to <span class="font-medium">{{ applications.to || 0 }}</span> of <span class="font-medium">{{ applications.total }}</span> results
                        </div>
                        <div class="flex items-center gap-2">
                            <Link
                                v-if="applications.prev_page_url"
                                :href="applications.prev_page_url"
                                class="inline-flex items-center gap-1 px-3 py-1.5 border border-gray-300 rounded-lg text-sm bg-white text-gray-600 hover:bg-gray-50 transition"
                            >
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                                </svg>
                                Previous
                            </Link>
                            <Link
                                v-if="applications.next_page_url"
                                :href="applications.next_page_url"
                                class="inline-flex items-center gap-1 px-3 py-1.5 border border-gray-300 rounded-lg text-sm bg-white text-gray-600 hover:bg-gray-50 transition"
                            >
                                Next
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                </svg>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AdminLayout>
</template>
