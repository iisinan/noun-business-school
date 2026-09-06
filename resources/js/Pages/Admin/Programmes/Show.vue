<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { ref } from 'vue';
import Modal from '@/Components/Modal.vue';

const props = defineProps({
    programme: Object,
    allCourses: Array
});

const attachCourse = (courseId) => {
    useForm({ course_id: courseId }).post(route('admin.programmes.courses.attach', props.programme.id), { preserveScroll: true });
};

const detachCourse = (courseId) => {
    if (confirm('Are you sure you want to remove this course from the programme?')) {
        useForm({}).delete(route('admin.programmes.courses.detach', [props.programme.id, courseId]));
    }
};
</script>

<template>
    <Head :title="programme.name" />

    <AdminLayout>
        <template #header>
            <div class="flex items-center gap-3">
                <Link :href="route('admin.programmes.index')" class="text-gray-400 hover:text-noun-green transition">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                    </svg>
                </Link>
                <h2 class="text-xl font-semibold leading-tight text-gray-800">
                    {{ programme.name }}
                </h2>
            </div>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8 space-y-6">
                
                <div v-if="$page.props.flash && $page.props.flash.success" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg">
                    {{ $page.props.flash.success }}
                </div>

                <!-- Programme Details Header -->
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden p-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ programme.type }}</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-blue-100 text-blue-800 uppercase">{{ programme.duration }} Semesters</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md uppercase"
                                  :class="programme.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                {{ programme.is_active ? 'Active' : 'Suspended' }}
                            </span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900">{{ programme.name }}</h3>
                        <p class="text-sm text-gray-500 mt-1 max-w-3xl">{{ programme.description || 'No description provided.' }}</p>
                    </div>
                </div>

                <!-- Assigned Courses Section -->
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">Curriculum (Assigned Courses)</h3>
                            <p class="text-sm text-gray-500 mt-0.5">Courses that students in this programme can register for.</p>
                        </div>

                    </div>

                    <table class="min-w-full divide-y divide-gray-100">
                        <thead>
                            <tr class="bg-gray-50">
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Course Code</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Course Title</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Credits</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>
                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Level & Sem</th>
                                <th class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in allCourses" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span v-if="course.type" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-600'">{{ course.type }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-blue-50 text-blue-700 mr-1">{{ course.level }}L</span>
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-green-50 text-green-700">S{{ course.semester }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <div v-if="course.is_attached">
                                        <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                    </div>
                                    <div v-else>
                                        <button @click="attachCourse(course.id)" class="text-noun-green hover:text-noun-dark font-semibold transition">Add to Programme</button>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="!allCourses || allCourses.length === 0">
                                <td colspan="6" class="px-6 py-12 text-center text-sm text-gray-400">No courses available in the system.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>
        </div>

        

    </AdminLayout>
</template>
