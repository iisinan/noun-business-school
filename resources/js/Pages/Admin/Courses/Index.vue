<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';

const props = defineProps({
    courses: Object,
    filters: Object
});

const search = ref(props.filters.search || '');
let timeout = null;

watch(search, (val) => {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => {
        router.get(route('admin.courses.index'), { search: val }, { preserveState: true, replace: true });
    }, 300);
});
</script>

<template>
    <Head title="Manage Courses" />
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
                
                <div class="bg-white p-4 shadow-sm rounded-xl border border-gray-100 mb-6 flex flex-col md:flex-row justify-between items-center gap-4">
                    <div class="w-full md:w-2/3 flex flex-col sm:flex-row gap-3">
                        <input
                            v-model="search"
                            type="text"
                            class="block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg bg-white sm:text-sm focus:ring-noun-green focus:border-noun-green"
                            placeholder="Search by course code or title..."
                        >
                        <select v-model="programme_id" class="block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg bg-white sm:text-sm focus:ring-noun-green focus:border-noun-green">
                            <option value="">All Programmes</option>
                            <option v-for="prog in programmes" :key="prog.id" :value="prog.id">{{ prog.name }}</option>
                        </select>
                    </div>
                    <Link :href="route('admin.courses.create')" class="shrink-0 bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                        + Add Course
                    </Link>
                </div>

                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <table class="min-w-full divide-y divide-gray-100">
                        <thead>
                            <tr class="bg-gray-50">
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Course Code</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Course Title</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Credits</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Level & Semester</th>
                                <th class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in courses.data" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span v-if="course.type" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-600'">{{ course.type }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-blue-50 text-blue-700 mr-2">{{ course.level }} Level</span>
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-green-50 text-green-700">Sem {{ course.semester }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <button class="text-noun-green hover:text-noun-dark font-semibold">Edit</button>
                                </td>
                            </tr>
                            <tr v-if="!courses.data.length">
                                <td colspan="6" class="px-6 py-8 text-center text-gray-400 text-sm">No courses found.</td>
                            </tr>
                        </tbody>
                    </table>
                    
                    <!-- Pagination -->
                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-50 flex items-center justify-between">
                        <div class="text-sm text-gray-600">
                            Showing {{ courses.from || 0 }} to {{ courses.to || 0 }} of {{ courses.total }}
                        </div>
                        <div class="flex gap-2">
                            <Link v-if="courses.prev_page_url" :href="courses.prev_page_url" class="px-3 py-1.5 border rounded-lg text-sm bg-white hover:bg-gray-50">Prev</Link>
                            <Link v-if="courses.next_page_url" :href="courses.next_page_url" class="px-3 py-1.5 border rounded-lg text-sm bg-white hover:bg-gray-50">Next</Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AdminLayout>
</template>
