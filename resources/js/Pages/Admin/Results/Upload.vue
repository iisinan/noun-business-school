<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, usePage } from '@inertiajs/vue3';
import { ref } from 'vue';

const props = defineProps({
    courses: Array,
    sessions: Array
});

const form = useForm({
    upload_mode: 'single',
    course_id: '',
    academic_session_id: props.sessions.length > 0 ? props.sessions[0].id : '',
    file: null
});

const page = usePage();

const submit = () => {
    form.post(route('admin.results.store'), {
        preserveScroll: true,
        onSuccess: () => {
            if (page.props.flash.success) {
                form.reset('file');
            }
        }
    });
};

const handleFile = (e) => {
    form.file = e.target.files[0];
};
</script>

<template>
    <Head title="Upload Results" />
    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">Upload Student Results</h2>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-3xl sm:px-6 lg:px-8">
                
                <div v-if="$page.props.flash.success" class="mb-6 bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-xl relative shadow-sm font-medium">
                    {{ $page.props.flash.success }}
                </div>
                <div v-if="$page.props.flash.error" class="mb-6 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl relative shadow-sm font-medium whitespace-pre-wrap">
                    {{ $page.props.flash.error }}
                </div>

                <form @submit.prevent="submit" class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="p-6 border-b border-gray-100 bg-gray-50 flex items-center justify-between">
                        <h3 class="text-lg font-bold text-gray-900">Upload CSV Results</h3>
                        
                        <div class="flex items-center gap-4 bg-white p-1 rounded-lg border border-gray-200 shadow-sm">
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="form.upload_mode === 'single' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="form.upload_mode" value="single" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Single Course</span>
                            </label>
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="form.upload_mode === 'multiple' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="form.upload_mode" value="multiple" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Multiple Courses</span>
                            </label>
                        </div>
                    </div>

                    <div class="p-6 space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-bold text-gray-700 mb-1">Academic Session</label>
                                <select v-model="form.academic_session_id" required class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="session in sessions" :key="session.id" :value="session.id">{{ session.name }}</option>
                                </select>
                                <p v-if="form.errors.academic_session_id" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.academic_session_id }}</p>
                            </div>
                            
                            <div v-if="form.upload_mode === 'single'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Course</label>
                                <select v-model="form.course_id" required class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option value="" disabled>Select a course</option>
                                    <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                </select>
                                <p v-if="form.errors.course_id" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.course_id }}</p>
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-3">Upload CSV File</label>
                            <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-xl hover:bg-gray-50 transition">
                                <div class="space-y-1 text-center">
                                    <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                                        <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                    <div class="flex text-sm text-gray-600 justify-center">
                                        <label class="relative cursor-pointer bg-white rounded-md font-bold text-noun-green hover:text-green-800 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-noun-green">
                                            <span>Upload a file</span>
                                            <input type="file" @change="handleFile" accept=".csv" required class="sr-only">
                                        </label>
                                        <p class="pl-1">or drag and drop</p>
                                    </div>
                                    <p class="text-xs text-gray-500 font-medium">CSV files only up to 5MB</p>
                                    <p v-if="form.file" class="text-sm text-green-700 font-bold mt-2">{{ form.file.name }} selected</p>
                                </div>
                            </div>
                            <p v-if="form.errors.file" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.file }}</p>
                        </div>
                        
                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-4">
                            <h4 class="text-sm font-bold text-blue-900 mb-2">CSV Template Format</h4>
                            <p class="text-xs text-blue-800 font-mono bg-white px-3 py-2 rounded border border-blue-100 shadow-sm" v-if="form.upload_mode === 'single'">Matric Number, Score<br>NBS/1/0002, 85<br>NBS/1/0014, 62</p>
                            <p class="text-xs text-blue-800 font-mono bg-white px-3 py-2 rounded border border-blue-100 shadow-sm" v-else>Matric Number, Course Code, Score<br>NBS/1/0002, MBA801, 85<br>NBS/1/0002, MBA802, 62<br>NBS/1/0014, MBA801, 74</p>
                        </div>
                    </div>

                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-100 flex items-center justify-end gap-3">
                        <button type="submit" :disabled="form.processing" class="inline-flex items-center gap-2 bg-noun-dark text-white px-6 py-3 rounded-lg text-sm font-bold hover:bg-black transition shadow-md disabled:opacity-50">
                            Upload Results
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </AdminLayout>
</template>
