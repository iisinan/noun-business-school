<script setup>
import { Head } from '@inertiajs/vue3';
import { onMounted } from 'vue';

const props = defineProps({
    user: Object,
    application: Object,
    session: Object,
    registeredCourses: Array,
});

const calculateTotalUnits = () => {
    return props.registeredCourses.reduce((sum, item) => sum + (item.course?.units || 0), 0);
};

onMounted(() => {
    // Automatically trigger print dialog when component is loaded in a new tab
    setTimeout(() => {
        window.print();
    }, 500);
});
</script>

<template>
    <Head title="Course Registration Slip" />

    <div class="min-h-screen bg-gray-50 flex justify-center py-10 print:py-0 print:bg-white">
        <!-- Action Buttons (Hidden in print) -->
        <div class="fixed top-6 right-6 flex gap-3 print:hidden">
            <button @click="window.close()" class="px-4 py-2 bg-white border border-gray-300 text-gray-700 rounded-lg text-sm font-semibold shadow-sm hover:bg-gray-50 transition">
                Close
            </button>
            <button @click="window.print()" class="px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-semibold shadow-sm hover:bg-noun-dark transition inline-flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                Print Document
            </button>
        </div>

        <!-- Document Container -->
        <div class="w-[210mm] min-h-[297mm] bg-white shadow-xl print:shadow-none mx-auto print:mx-0 p-12 relative overflow-hidden">
            
            <!-- Watermark -->
            <div class="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none select-none">
                <img src="/nbs-logo.png" alt="Watermark" class="w-[500px]">
            </div>

            <!-- Header -->
            <div class="flex items-start justify-between border-b-2 border-noun-green pb-6 mb-8 relative z-10">
                <div class="flex items-center gap-5">
                    <img src="/nbs-logo.png" alt="NOUN Logo" class="h-24 w-auto">
                    <div>
                        <h1 class="text-2xl font-black text-noun-green tracking-tight uppercase">National Open University of Nigeria</h1>
                        <h2 class="text-lg font-bold text-gray-800 tracking-wide mt-1">Business School (NBS)</h2>
                        <p class="text-sm text-gray-500 font-medium mt-0.5">Course Registration E-Slip</p>
                    </div>
                </div>
            </div>

            <!-- Student Biodata Card -->
            <div class="border border-gray-200 rounded-xl overflow-hidden mb-8 relative z-10">
                <div class="bg-gray-100 px-5 py-3 border-b border-gray-200">
                    <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest">Student Information</h3>
                </div>
                <div class="p-6 grid grid-cols-2 gap-y-4 gap-x-8">
                    <div>
                        <p class="text-xs text-gray-500 uppercase font-semibold">Full Name</p>
                        <p class="font-bold text-gray-900 mt-0.5">{{ user.first_name }} {{ user.last_name }}</p>
                    </div>
                    <div>
                        <p class="text-xs text-gray-500 uppercase font-semibold">Matriculation Number</p>
                        <p class="font-bold text-noun-green font-mono mt-0.5 text-lg leading-none">
                            NBS/{{ application.academic_session_id }}/{{ String(application.id).padStart(4, '0') }}
                        </p>
                    </div>
                    <div>
                        <p class="text-xs text-gray-500 uppercase font-semibold">Programme of Study</p>
                        <p class="font-bold text-gray-900 mt-0.5">{{ application.programme?.name || 'N/A' }}</p>
                    </div>
                    <div>
                        <p class="text-xs text-gray-500 uppercase font-semibold">Academic Session & Semester</p>
                        <p class="font-bold text-gray-900 mt-0.5">{{ session.name }} &mdash; Semester {{ $page.props.studentSemester || 1 }}</p>
                    </div>
                </div>
            </div>

            <!-- Course Table -->
            <div class="mb-8 relative z-10">
                <h3 class="text-sm font-bold text-gray-800 uppercase tracking-widest mb-4">Registered Courses</h3>
                
                <table class="w-full border-collapse">
                    <thead>
                        <tr class="bg-noun-green text-white">
                            <th class="py-2.5 px-4 text-left text-xs font-bold uppercase tracking-wider border border-noun-green w-16">S/N</th>
                            <th class="py-2.5 px-4 text-left text-xs font-bold uppercase tracking-wider border border-noun-green w-32">Course Code</th>
                            <th class="py-2.5 px-4 text-left text-xs font-bold uppercase tracking-wider border border-noun-green">Course Title</th>
                            <th class="py-2.5 px-4 text-center text-xs font-bold uppercase tracking-wider border border-noun-green w-24">Units</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(reg, index) in registeredCourses" :key="reg.id" class="border-b border-gray-200">
                            <td class="py-3 px-4 border border-gray-200 text-sm font-medium text-gray-500 text-center">{{ index + 1 }}</td>
                            <td class="py-3 px-4 border border-gray-200 text-sm font-bold text-gray-900">{{ reg.course?.code }}</td>
                            <td class="py-3 px-4 border border-gray-200 text-sm text-gray-800">{{ reg.course?.title }}</td>
                            <td class="py-3 px-4 border border-gray-200 text-sm font-bold text-gray-900 text-center">{{ reg.course?.units }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr class="bg-gray-100">
                            <td colspan="3" class="py-3 px-4 border border-gray-300 text-right text-sm font-bold text-gray-900 uppercase">Total Registered Units</td>
                            <td class="py-3 px-4 border border-gray-300 text-center text-sm font-black text-noun-green">{{ calculateTotalUnits() }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>



            <div class="mt-12 text-center relative z-10">
                <p class="text-xs text-gray-400 italic">This document is electronically generated and is valid for the specified academic session.</p>
                <p class="text-xs text-gray-400 font-mono mt-1">Generated: {{ new Date().toLocaleString() }}</p>
            </div>
        </div>
    </div>
</template>
