<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { ref } from 'vue';
import Modal from '@/Components/Modal.vue';

const props = defineProps({
    programme: Object,
    allCourses: Array
});

const isAttachModalOpen = ref(false);

const attachForm = useForm({
    course_id: ''
});

const submitAttach = () => {
    attachForm.post(route('admin.programmes.courses.attach', props.programme.id), {
        onSuccess: () => {
            isAttachModalOpen.value = false;
            attachForm.reset();
        }
    });
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
                        <button @click="isAttachModalOpen = true" class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                            Attach Course
                        </button>
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
                            <tr v-for="course in programme.courses" :key="course.id" class="hover:bg-gray-50">
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
                                    <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                </td>
                            </tr>
                            <tr v-if="!programme.courses || programme.courses.length === 0">
                                <td colspan="6" class="px-6 py-12 text-center text-sm text-gray-400">No courses attached to this programme yet.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </div>
        </div>

        <!-- Attach Course Modal -->
        <Modal :show="isAttachModalOpen" @close="isAttachModalOpen = false" maxWidth="md">
            <div class="p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-4">Attach Course to Programme</h3>
                <form @submit.prevent="submitAttach">
                    <div class="mb-5">
                        <label class="block text-sm font-semibold text-gray-700 mb-1.5">Select Course</label>
                        <select v-model="attachForm.course_id" required class="block w-full rounded-lg border-gray-300 focus:border-noun-green focus:ring-noun-green sm:text-sm">
                            <option value="" disabled>Choose a course...</option>
                            <option v-for="c in allCourses" :key="c.id" :value="c.id">
                                {{ c.code }} - {{ c.title }}
                            </option>
                        </select>
                        <p v-if="attachForm.errors.course_id" class="mt-1 text-sm text-red-600">{{ attachForm.errors.course_id }}</p>
                    </div>
                    
                    <div class="flex items-center justify-end gap-3 mt-6">
                        <button type="button" @click="isAttachModalOpen = false" class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg text-sm font-semibold hover:bg-gray-200 transition">Cancel</button>
                        <button type="submit" :disabled="attachForm.processing" class="px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-semibold hover:bg-noun-dark transition disabled:opacity-50">Attach Course</button>
                    </div>
                </form>
            </div>
        </Modal>

    </AdminLayout>
</template>
