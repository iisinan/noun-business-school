<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, usePage } from '@inertiajs/vue3';
import { ref } from 'vue';

const props = defineProps({
    courses: Array,
    sessions: Array
});

const form = useForm({
    upload_mode: 'multiple', // default to multiple since template supports it
    course_id: '',
    academic_session_id: props.sessions.length > 0 ? props.sessions[0].id : '',
    file: null
});

const templateForm = useForm({
    mode: 'single',
    course_id: '',
    academic_session_id: props.sessions.length > 0 ? props.sessions[0].id : '',
    semester: 1
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

const downloadTemplate = () => {
    if (templateForm.mode === 'single' && !templateForm.course_id) {
        alert('Please select a course first.');
        return;
    }
    
    window.location.href = route('results.template', {
        mode: templateForm.mode,
        course_id: templateForm.course_id,
        academic_session_id: templateForm.academic_session_id,
        semester: templateForm.semester
    });
};
</script>

<template>
    <Head title="Upload Results" />
    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">Upload Student Results</h2>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-3xl sm:px-6 lg:px-8 space-y-6">
                
                <div v-if="$page.props.flash.success" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-xl relative shadow-sm font-medium">
                    {{ $page.props.flash.success }}
                </div>
                <div v-if="$page.props.flash.error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl relative shadow-sm font-medium whitespace-pre-wrap">
                    {{ $page.props.flash.error }}
                </div>

                <!-- Step 1: Download Template -->
                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="p-6 border-b border-gray-100 bg-gray-50 flex items-center justify-between">
                        <div>
                            <h3 class="text-lg font-bold text-gray-900">Step 1: Download Smart Excel Template</h3>
                            <p class="text-sm text-gray-500 mt-1">Generate a pre-filled Excel file with registered students.</p>
                        </div>
                        
                        <div class="flex items-center gap-4 bg-white p-1 rounded-lg border border-gray-200 shadow-sm">
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'single' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="templateForm.mode" value="single" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Single Course</span>
                            </label>
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'multiple' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="templateForm.mode" value="multiple" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Entire Semester</span>
                            </label>
                        </div>
                    </div>

                    <div class="p-6 space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-bold text-gray-700 mb-1">Academic Session</label>
                                <select v-model="templateForm.academic_session_id" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="session in sessions" :key="session.id" :value="session.id">{{ session.name }}</option>
                                </select>
                            </div>
                            
                            <div v-if="templateForm.mode === 'multiple'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Semester</label>
                                <select v-model="templateForm.semester" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="i in 6" :key="i" :value="i">Semester {{ i }}</option>
                                </select>
                            </div>
                            
                            <div v-if="templateForm.mode === 'single'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Course</label>
                                <select v-model="templateForm.course_id" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option value="" disabled>Select a course</option>
                                    <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-100 flex items-center justify-end">
                        <button @click="downloadTemplate" class="inline-flex items-center gap-2 bg-noun-green text-white px-6 py-3 rounded-lg text-sm font-bold hover:bg-noun-dark transition shadow-md">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                            Download Template (.xlsx)
                        </button>
                    </div>
                </div>

                <!-- Step 2: Upload Results -->
                <form @submit.prevent="submit" class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="p-6 border-b border-gray-100 bg-gray-50 flex items-center justify-between">
                        <h3 class="text-lg font-bold text-gray-900">Step 2: Upload Results</h3>
                        
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
                                <label class="block text-sm font-bold text-gray-700 mb-1">Target Academic Session</label>
                                <select v-model="form.academic_session_id" required class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="session in sessions" :key="session.id" :value="session.id">{{ session.name }}</option>
                                </select>
                                <p v-if="form.errors.academic_session_id" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.academic_session_id }}</p>
                            </div>
                            
                            <div v-if="form.upload_mode === 'single'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Target Course</label>
                                <select v-model="form.course_id" :required="form.upload_mode === 'single'" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option value="" disabled>Select a course</option>
                                    <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                </select>
                                <p v-if="form.errors.course_id" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.course_id }}</p>
                            </div>
                        </div>

                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-3">Upload File</label>
                            <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-xl hover:bg-gray-50 transition">
                                <div class="space-y-1 text-center">
                                    <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                                        <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                    </svg>
                                    <div class="flex text-sm text-gray-600 justify-center">
                                        <label class="relative cursor-pointer bg-white rounded-md font-bold text-noun-green hover:text-green-800 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-noun-green">
                                            <span>Upload a file</span>
                                            <input type="file" @change="handleFile" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" required class="sr-only">
                                        </label>
                                        <p class="pl-1">or drag and drop</p>
                                    </div>
                                    <p class="text-xs text-gray-500 font-medium">Excel (.xlsx) or CSV files up to 10MB</p>
                                    <p v-if="form.file" class="text-sm text-green-700 font-bold mt-2">{{ form.file.name }} selected</p>
                                </div>
                            </div>
                            <p v-if="form.errors.file" class="text-sm text-red-600 mt-1 font-semibold">{{ form.errors.file }}</p>
                        </div>
                        
                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-4">
                            <h4 class="text-sm font-bold text-blue-900 mb-2">Supported Formats</h4>
                            <ul class="list-disc pl-5 text-sm text-blue-800 space-y-1">
                                <li><strong>Smart Excel Template (.xlsx):</strong> Downloaded from Step 1. Simply fill the Score column and upload. The system automatically reads Matric Number from Column B and Score from Column F.</li>
                                <li><strong>Legacy CSV:</strong> Requires headers (<code>Matric Number</code>, <code>Score</code>, and optionally <code>Course Code</code>).</li>
                            </ul>
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
