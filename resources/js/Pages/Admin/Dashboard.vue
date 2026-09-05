<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link } from '@inertiajs/vue3';
import { computed } from 'vue';

const props = defineProps({
    stats: Object,
    recent_applications: Array,
    applications_by_programme: Array
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
</script>

<template>
    <Head title="Admin Dashboard" />

    <AdminLayout>
        <template #header>
            <div class="flex items-center justify-between">
                <h2 class="text-xl font-semibold leading-tight text-gray-800">
                    Admin Dashboard
                </h2>
                <div class="flex gap-3">
                    <Link
                        :href="route('admin.applications.index')"
                        class="inline-flex items-center gap-2 px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-medium hover:bg-noun-dark transition shadow-sm"
                    >
                        Review Applications
                    </Link>
                </div>
            </div>
        </template>

        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8 space-y-6">

                <!-- KPI Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                    <!-- Total Apps -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 relative overflow-hidden group hover:border-blue-300 transition">
                        <div class="absolute right-0 top-0 -mt-4 -mr-4 h-24 w-24 bg-blue-50 rounded-full z-0 group-hover:scale-110 transition-transform"></div>
                        <div class="relative z-10 flex items-center justify-between">
                            <div>
                                <div class="text-sm font-medium text-gray-500 uppercase tracking-wider mb-1">Total Applicants</div>
                                <div class="text-3xl font-bold text-gray-900">{{ stats.total_applications }}</div>
                            </div>
                            <div class="h-12 w-12 rounded-lg bg-blue-100 text-blue-600 flex items-center justify-center">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    <!-- Under Review -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 relative overflow-hidden group hover:border-purple-300 transition">
                        <div class="absolute right-0 top-0 -mt-4 -mr-4 h-24 w-24 bg-purple-50 rounded-full z-0 group-hover:scale-110 transition-transform"></div>
                        <div class="relative z-10 flex items-center justify-between">
                            <div>
                                <div class="text-sm font-medium text-gray-500 uppercase tracking-wider mb-1">Under Review</div>
                                <div class="text-3xl font-bold text-gray-900">{{ stats.under_review }}</div>
                            </div>
                            <div class="h-12 w-12 rounded-lg bg-purple-100 text-purple-600 flex items-center justify-center">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    <!-- Enrolled -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 relative overflow-hidden group hover:border-green-300 transition">
                        <div class="absolute right-0 top-0 -mt-4 -mr-4 h-24 w-24 bg-green-50 rounded-full z-0 group-hover:scale-110 transition-transform"></div>
                        <div class="relative z-10 flex items-center justify-between">
                            <div>
                                <div class="text-sm font-medium text-gray-500 uppercase tracking-wider mb-1">Total Enrolled</div>
                                <div class="text-3xl font-bold text-gray-900">{{ stats.enrolled }}</div>
                            </div>
                            <div class="h-12 w-12 rounded-lg bg-green-100 text-green-600 flex items-center justify-center">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    <!-- Revenue -->
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 relative overflow-hidden group hover:border-amber-300 transition">
                        <div class="absolute right-0 top-0 -mt-4 -mr-4 h-24 w-24 bg-amber-50 rounded-full z-0 group-hover:scale-110 transition-transform"></div>
                        <div class="relative z-10 flex items-center justify-between">
                            <div>
                                <div class="text-sm font-medium text-gray-500 uppercase tracking-wider mb-1">Total Revenue</div>
                                <div class="text-2xl font-bold text-gray-900">₦{{ Number(stats.total_revenue).toLocaleString() }}</div>
                            </div>
                            <div class="h-12 w-12 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center">
                                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    <!-- Recent Applications Table -->
                    <div class="lg:col-span-2 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden flex flex-col">
                        <div class="px-6 py-4 border-b border-gray-100 flex justify-between items-center bg-gray-50">
                            <h3 class="text-base font-bold text-gray-900">Recent Applications</h3>
                            <Link :href="route('admin.applications.index')" class="text-sm text-noun-green hover:underline font-semibold">View All</Link>
                        </div>
                        <div class="overflow-x-auto flex-1">
                            <table class="min-w-full divide-y divide-gray-200">
                                <thead class="bg-white">
                                    <tr>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Applicant</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Programme</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Date</th>
                                        <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                        <th scope="col" class="relative px-6 py-3"></th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-100">
                                    <tr v-for="app in recent_applications" :key="app.id" class="hover:bg-gray-50 transition">
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <div class="flex items-center">
                                                <div class="flex-shrink-0 h-8 w-8 rounded-full bg-noun-dark flex items-center justify-center text-white text-xs font-bold">
                                                    {{ app.user?.first_name?.charAt(0) }}{{ app.user?.last_name?.charAt(0) }}
                                                </div>
                                                <div class="ml-3">
                                                    <div class="text-sm font-semibold text-gray-900">{{ app.user?.first_name }} {{ app.user?.last_name }}</div>
                                                    <div class="text-xs text-gray-500">{{ app.application_number || 'Pending' }}</div>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <div class="text-sm text-gray-900 max-w-[200px] truncate">{{ app.programme?.name }}</div>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                            {{ new Date(app.created_at).toLocaleDateString() }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span class="px-2.5 py-1 inline-flex text-xs leading-5 font-bold rounded-full uppercase tracking-wider" :class="statusColor[app.status] || 'bg-gray-100 text-gray-800'">
                                                {{ app.status }}
                                            </span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                            <Link :href="route('admin.applications.show', app.id)" class="text-noun-green hover:text-green-700 font-semibold bg-green-50 px-3 py-1.5 rounded-lg border border-green-100 hover:bg-green-100 transition">Review</Link>
                                        </td>
                                    </tr>
                                    <tr v-if="recent_applications.length === 0">
                                        <td colspan="5" class="px-6 py-8 text-center text-gray-500 text-sm">No applications found.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Sidebar Stats / Quick Links -->
                    <div class="space-y-6">
                        
                        <!-- Demographics Chart / List -->
                        <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                            <div class="px-6 py-4 border-b border-gray-100 bg-gray-50">
                                <h3 class="text-base font-bold text-gray-900">Applications by Programme</h3>
                            </div>
                            <div class="px-6 py-4">
                                <ul class="space-y-4">
                                    <li v-for="(item, idx) in applications_by_programme" :key="idx">
                                        <div class="flex justify-between items-end mb-1">
                                            <span class="text-sm font-medium text-gray-700 truncate pr-4">{{ item.name }}</span>
                                            <span class="text-sm font-bold text-gray-900">{{ item.total }}</span>
                                        </div>
                                        <div class="w-full bg-gray-100 rounded-full h-2">
                                            <div class="bg-noun-green h-2 rounded-full" :style="{ width: Math.max(5, (item.total / stats.total_applications) * 100) + '%' }"></div>
                                        </div>
                                    </li>
                                    <li v-if="applications_by_programme.length === 0" class="text-sm text-gray-500 italic text-center py-2">
                                        No data available.
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <!-- System Configuration -->
                        <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                            <div class="px-6 py-4 border-b border-gray-100 bg-noun-dark">
                                <h3 class="text-base font-bold text-white">System Settings</h3>
                            </div>
                            <div class="p-4 grid grid-cols-2 gap-3">
                                <Link :href="route('admin.programmes.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Programmes</span>
                                </Link>
                                <Link :href="route('admin.sessions.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Sessions</span>
                                </Link>
                                <Link :href="route('admin.payments.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Payments</span>
                                </Link>
                                <Link :href="route('admin.users.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Users</span>
                                </Link>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </AdminLayout>
</template>
