<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, usePage } from '@inertiajs/vue3';
import { ref } from 'vue';

const props = defineProps({
    courses: Array,
    sessions: Array
});

const form = useForm({
    upload_mode: 'multiple',
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
    
    window.location.href = route('admin.results.template', {
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

        <div class="py-10">
            <div class="mx-auto max-w-6xl sm:px-6 lg:px-8 space-y-6">
                
                <div v-if="$page.props.flash.success" class="bg-green-50 border border-green-200 text-green-700 px-5 py-4 rounded-xl relative shadow-sm font-medium flex items-center gap-3">
                    <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    {{ $page.props.flash.success }}
                </div>
                <div v-if="$page.props.flash.error" class="bg-red-50 border border-red-200 text-red-700 px-5 py-4 rounded-xl relative shadow-sm font-medium whitespace-pre-wrap flex gap-3">
                    <svg class="w-6 h-6 text-red-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    <div>{{ $page.props.flash.error }}</div>
                </div>

                <div class="bg-white shadow-md rounded-2xl border border-gray-200 overflow-hidden">
                    
                    <!-- Unified Header -->
                    <div class="bg-white px-8 py-6 border-b border-gray-100 flex items-center justify-between">
                        <div>
                            <h3 class="text-xl font-bold text-gray-900 tracking-tight">Results Management</h3>
                            <p class="text-sm text-gray-500 mt-1">Download pre-filled student templates and upload graded results.</p>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-1 lg:grid-cols-12 divide-y lg:divide-y-0 lg:divide-x divide-gray-100">
                        
                        <!-- Left Column: Step 1 Template -->
                        <div class="lg:col-span-5 p-8 bg-gray-50/50 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-6">
                                    <h4 class="text-base font-bold text-gray-900 flex items-center gap-2">
                                        <span class="flex items-center justify-center w-6 h-6 rounded-full bg-noun-green text-white text-xs">1</span>
                                        Download Template
                                    </h4>
                                    
                                    <div class="flex items-center bg-white p-0.5 rounded-lg border border-gray-200 shadow-sm">
                                        <label class="flex items-center gap-2 px-3 py-1 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'single' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                            <input type="radio" v-model="templateForm.mode" value="single" class="sr-only">
                                            <span class="text-xs font-bold tracking-wide">Single</span>
                                        </label>
                                        <label class="flex items-center gap-2 px-3 py-1 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'multiple' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                            <input type="radio" v-model="templateForm.mode" value="multiple" class="sr-only">
                                            <span class="text-xs font-bold tracking-wide">Multiple Courses</span>
                                        </label>
                                    </div>
                                </div>
                                
                                <div class="space-y-5">
                                    <div>
                                        <label class="block text-sm font-bold text-gray-700 mb-1.5">Academic Session</label>
                                        <select v-model="templateForm.academic_session_id" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green text-sm bg-white">
                                            <option v-for="session in sessions" :key="session.id" :value="session.id">{{ session.name }}</option>
                                        </select>
                                    </div>
                                    

                                    
                                    <div v-if="templateForm.mode === 'single'">
                                        <label class="block text-sm font-bold text-gray-700 mb-1.5">Course</label>
                                        <select v-model="templateForm.course_id" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green text-sm bg-white">
                                            <option value="" disabled>Select a course</option>
                                            <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="mt-8 pt-6 border-t border-gray-200">
                                <button @click="downloadTemplate" class="w-full flex justify-center items-center gap-2 bg-white border border-gray-300 text-gray-700 px-6 py-3 rounded-xl text-sm font-bold hover:bg-gray-50 transition shadow-sm hover:border-gray-400">
                                    <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                                    Download Smart Template
                                </button>
                                <p class="text-xs text-gray-500 text-center mt-3 leading-relaxed">
                                    This Excel file is pre-populated with registered students and is password-protected to prevent accidental formatting changes.
                                </p>
                            </div>
                        </div>
                        
                        <!-- Right Column: Step 2 Upload -->
                        <div class="lg:col-span-7 bg-white flex flex-col">
                            <form @submit.prevent="submit" class="p-8 flex flex-col h-full justify-between">
                                <div>
                                    <div class="flex items-center justify-between mb-6">
                                        <h4 class="text-base font-bold text-gray-900 flex items-center gap-2">
                                            <span class="flex items-center justify-center w-6 h-6 rounded-full bg-noun-dark text-white text-xs">2</span>
                                            Upload Graded Results
                                        </h4>
                                        
                                        <div class="flex items-center bg-gray-50 p-0.5 rounded-lg border border-gray-200 shadow-sm">
                                            <label class="flex items-center gap-2 px-3 py-1 cursor-pointer rounded-md transition-colors" :class="form.upload_mode === 'single' ? 'bg-noun-dark text-white' : 'text-gray-600 hover:bg-gray-100'">
                                                <input type="radio" v-model="form.upload_mode" value="single" class="sr-only">
                                                <span class="text-xs font-bold tracking-wide">Single Course</span>
                                            </label>
                                            <label class="flex items-center gap-2 px-3 py-1 cursor-pointer rounded-md transition-colors" :class="form.upload_mode === 'multiple' ? 'bg-noun-dark text-white' : 'text-gray-600 hover:bg-gray-100'">
                                                <input type="radio" v-model="form.upload_mode" value="multiple" class="sr-only">
                                                <span class="text-xs font-bold tracking-wide">Multiple Courses</span>
                                            </label>
                                        </div>
                                    </div>

                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
                                        <div>
                                            <label class="block text-sm font-bold text-gray-700 mb-1.5">Target Session</label>
                                            <select v-model="form.academic_session_id" required class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green text-sm bg-white">
                                                <option v-for="session in sessions" :key="session.id" :value="session.id">{{ session.name }}</option>
                                            </select>
                                            <p v-if="form.errors.academic_session_id" class="text-xs text-red-600 mt-1 font-semibold">{{ form.errors.academic_session_id }}</p>
                                        </div>
                                        
                                        <div v-if="form.upload_mode === 'single'">
                                            <label class="block text-sm font-bold text-gray-700 mb-1.5">Target Course</label>
                                            <select v-model="form.course_id" :required="form.upload_mode === 'single'" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green text-sm bg-white">
                                                <option value="" disabled>Select a course</option>
                                                <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                            </select>
                                            <p v-if="form.errors.course_id" class="text-xs text-red-600 mt-1 font-semibold">{{ form.errors.course_id }}</p>
                                        </div>
                                    </div>

                                    <div>
                                        <label class="block text-sm font-bold text-gray-700 mb-2">Upload Excel / CSV File</label>
                                        <div class="mt-1 flex justify-center px-6 py-10 border-2 border-gray-300 border-dashed rounded-xl hover:bg-green-50/50 hover:border-noun-green transition duration-200 cursor-pointer" @click="$refs.fileInput.click()">
                                            <div class="space-y-2 text-center">
                                                <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                                                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                                </svg>
                                                <div class="flex text-sm text-gray-600 justify-center">
                                                    <span class="relative bg-transparent rounded-md font-bold text-noun-green hover:text-green-800">
                                                        Browse files
                                                    </span>
                                                    <input ref="fileInput" type="file" @change="handleFile" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" required class="sr-only">
                                                    <p class="pl-1">or drag and drop</p>
                                                </div>
                                                <p class="text-xs text-gray-500 font-medium">Supports .xlsx or .csv up to 10MB</p>
                                                <p v-if="form.file" class="text-sm text-green-700 font-bold mt-3 bg-green-100 py-1.5 px-3 rounded-lg inline-block">{{ form.file.name }}</p>
                                            </div>
                                        </div>
                                        <p v-if="form.errors.file" class="text-xs text-red-600 mt-2 font-semibold">{{ form.errors.file }}</p>
                                    </div>
                                </div>

                                <div class="mt-8 pt-6 border-t border-gray-100 flex items-center justify-between">
                                    <div class="text-xs text-gray-500 max-w-[200px]">
                                        Automatically reads Matric Number and Score from the uploaded sheet.
                                    </div>
                                    <button type="submit" :disabled="form.processing || !form.file" class="inline-flex items-center gap-2 bg-noun-dark text-white px-8 py-3.5 rounded-xl text-sm font-bold hover:bg-black transition shadow-md disabled:opacity-50 disabled:cursor-not-allowed">
                                        <svg v-if="form.processing" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                                        Upload & Save Results
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </AdminLayout>
</template>
