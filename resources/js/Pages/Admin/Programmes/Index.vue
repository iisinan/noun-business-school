<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';

const toggleStatus = (id, currentStatus) => {
    const action = currentStatus ? 'suspend' : 'activate';
    if (confirm(`Are you sure you want to ${action} this programme?`)) {
        router.patch(route('admin.programmes.toggle-status', id), {}, {
            preserveScroll: true
        });
    }
};

defineProps({
    programmes: Array,
});
</script>

<template>
    <Head title="Manage Programmes" />
    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">Curriculum Management</h2>
        </template>

                <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8">
                <!-- Inner Curriculum Tabs -->
                <div class="mb-6 border-b border-gray-200">
                    <nav class="-mb-px flex space-x-8" aria-label="Tabs">
                        <Link 
                            :href="route('admin.programmes.index')" 
                            :class="[route().current('admin.programmes.*') ? 'border-noun-green text-noun-green' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300', 'whitespace-nowrap py-4 px-1 border-b-2 font-bold text-sm transition']"
                        >
                            Programmes
                        </Link>
                        <Link 
                            :href="route('admin.courses.index')" 
                            :class="[route().current('admin.courses.*') ? 'border-noun-green text-noun-green' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300', 'whitespace-nowrap py-4 px-1 border-b-2 font-bold text-sm transition']"
                        >
                            Course Bank
                        </Link>
                    </nav>
                </div>
                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <!-- Header -->
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">All Programmes</h3>
                            <p class="text-sm text-gray-500 mt-0.5">{{ programmes.length }} programme{{ programmes.length !== 1 ? 's' : '' }} listed</p>
                        </div>
                        <Link :href="route('admin.programmes.create')" class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            Add Programme
                        </Link>
                    </div>

                    <table class="min-w-full divide-y divide-gray-100">
                        <thead>
                            <tr class="bg-gray-50">
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Programme Name</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Specialisations</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-50">
                            <template v-for="prog in programmes" :key="prog.id">
                                <!-- Parent Programme Row -->
                                <tr class="bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer group" @click="toggleExpand(prog.id)">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ prog.type }}</span>
                                    </td>
                                    <td class="px-6 py-4">
                                        <div class="flex items-center gap-2">
                                            <svg class="w-4 h-4 text-gray-400 group-hover:text-gray-600 transition-transform duration-200" :class="{ 'rotate-90': expandedProgrammes.includes(prog.id) }" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                            <div class="text-sm font-bold text-gray-900">{{ prog.name }} (Core)</div>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 font-medium">
                                        <span class="bg-white border border-gray-200 px-2.5 py-0.5 rounded-full">{{ prog.specialisations?.length ?? 0 }} Tracks</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                              :class="prog.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                            {{ prog.is_active ? 'Active' : 'Suspended' }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm" @click.stop>
                                        <div class="flex items-center gap-2">
                                            <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1 bg-white border border-gray-300 text-gray-700 font-semibold text-xs rounded hover:bg-gray-50 transition shadow-sm">
                                                Manage Core
                                            </Link>
                                            <button @click="toggleStatus(prog.id, prog.is_active)" class="inline-flex items-center gap-1.5 px-3 py-1 font-semibold text-xs rounded transition shadow-sm border"
                                                    :class="prog.is_active ? 'bg-white border-red-200 text-red-600 hover:bg-red-50' : 'bg-white border-green-200 text-green-600 hover:bg-green-50'">
                                                {{ prog.is_active ? 'Suspend' : 'Activate' }}
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                
                                <!-- Specialisations Rows (Dropdown) -->
                                <tr v-for="spec in prog.specialisations" :key="spec.id" v-show="expandedProgrammes.includes(prog.id)" class="bg-white hover:bg-gray-50 transition-colors border-l-2 border-l-noun-green">
                                    <td class="px-6 py-3 whitespace-nowrap">
                                        <span class="px-2 py-0.5 ml-4 text-[10px] font-semibold rounded bg-gray-100 text-gray-600">Track</span>
                                    </td>
                                    <td class="px-6 py-3">
                                        <div class="text-sm font-medium text-gray-700 pl-4 border-l border-gray-200">{{ spec.name }}</div>
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap text-sm text-gray-400">
                                        Specific Curriculum
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap">
                                        <span class="text-xs text-gray-400">Inherits Status</span>
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap text-sm">
                                        <Link :href="route('admin.specialisations.show', spec.id)" class="inline-flex items-center gap-1.5 px-3 py-1 bg-noun-green text-white font-semibold text-[11px] rounded hover:bg-noun-dark transition shadow-sm">
                                            Manage Track
                                            <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                        </Link>
                                    </td>
                                </tr>
                            </template>
                            <tr v-if="!programmes.length">
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No programmes found.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </AdminLayout>
</template>
