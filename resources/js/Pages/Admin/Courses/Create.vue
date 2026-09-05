<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

const form = useForm({
    code: '',
    title: '',
    type: 'Core',
    credits: 3,
    semester: 1,
    level: 700,
    description: ''
});

const submit = () => {
    form.post(route('admin.courses.store'));
};
</script>

<template>
    <Head title="Create Course" />
    <AdminLayout>
        <template #header>
            <div class="flex items-center gap-3">
                <Link :href="route('admin.courses.index')" class="text-gray-500 hover:text-noun-green">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                </Link>
                <h2 class="text-xl font-semibold leading-tight text-gray-800">Add New Course</h2>
            </div>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-3xl sm:px-6 lg:px-8">
                <form @submit.prevent="submit" class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="p-6 border-b border-gray-100 bg-gray-50">
                        <h3 class="text-lg font-bold text-gray-900">Course Details</h3>
                    </div>

                    <div class="p-6 space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Course Code</label>
                                <input v-model="form.code" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="e.g. MBA801">
                                <p v-if="form.errors.code" class="text-sm text-red-600 mt-1">{{ form.errors.code }}</p>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Course Title</label>
                                <input v-model="form.title" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="e.g. Production Management">
                                <p v-if="form.errors.title" class="text-sm text-red-600 mt-1">{{ form.errors.title }}</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Credit Units</label>
                                <input v-model="form.credits" type="number" min="1" max="10" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                <p v-if="form.errors.credits" class="text-sm text-red-600 mt-1">{{ form.errors.credits }}</p>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Course Type</label>
                                <select v-model="form.type" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                    <option value="Core">Core</option>
                                    <option value="Elective">Elective</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Semester</label>
                                <select v-model="form.semester" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                    <option value="1">First Semester</option>
                                    <option value="2">Second Semester</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Level</label>
                                <select v-model="form.level" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                    <option value="700">700 Level (PGD)</option>
                                    <option value="800">800 Level (Master's)</option>
                                    <option value="900">900 Level (PhD)</option>
                                </select>
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-semibold text-gray-700 mb-1">Description (Optional)</label>
                            <textarea v-model="form.description" rows="3" class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm"></textarea>
                        </div>
                    </div>

                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-100 flex items-center justify-end gap-3">
                        <Link :href="route('admin.courses.index')" class="px-4 py-2 text-sm font-semibold text-gray-700 hover:text-gray-900">Cancel</Link>
                        <button type="submit" :disabled="form.processing" class="inline-flex items-center gap-2 bg-noun-green text-white px-5 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-md disabled:opacity-50">
                            Save Course
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </AdminLayout>
</template>
