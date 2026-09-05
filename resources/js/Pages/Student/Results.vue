<script setup>
import { Head, Link } from '@inertiajs/vue3';
import StudentLayout from '@/Layouts/StudentLayout.vue';

const props = defineProps({
    resultsBySession: { type: Array, default: () => [] },
    cgpa: Number,
    cumulativeCredits: Number
});

const getGradeColor = (grade) => {
    switch (grade) {
        case 'A': return 'bg-emerald-100 text-emerald-700 border-emerald-200';
        case 'B': return 'bg-blue-100 text-blue-700 border-blue-200';
        case 'C': return 'bg-indigo-100 text-indigo-700 border-indigo-200';
        case 'D': return 'bg-amber-100 text-amber-700 border-amber-200';
        case 'E': return 'bg-orange-100 text-orange-700 border-orange-200';
        case 'F': return 'bg-red-100 text-red-700 border-red-200';
        default: return 'bg-gray-100 text-gray-500 border-gray-200';
    }
};
</script>

<template>
    <Head title="My Results" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Academic Results</h2>
        </template>
        
        <div class="py-8 px-4 sm:px-6 lg:px-8 ">
            
            <div v-if="resultsBySession.length === 0" class="bg-white rounded-3xl p-12 text-center border border-gray-100 shadow-sm max-w-2xl mx-auto">
                <div class="h-24 w-24 rounded-full bg-gray-50 mx-auto flex items-center justify-center mb-6">
                    <svg class="w-10 h-10 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">No Results Found</h3>
                <p class="text-gray-500 mb-6 max-w-md mx-auto">You do not have any academic results yet. Once you complete a semester and grades are published, they will appear here.</p>
                <Link :href="route('student.registration')" class="inline-flex items-center gap-2 px-6 py-3 bg-noun-green text-white font-bold rounded-xl hover:bg-noun-dark transition shadow-md shadow-noun-green/20">
                    Go to Course Registration
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>
                </Link>
            </div>

            <div v-else class="space-y-8">
                
                <!-- CGPA Overview Card -->
                <div class="bg-gradient-to-r from-noun-dark to-noun-green rounded-3xl p-8 shadow-xl text-white relative overflow-hidden">
                    <!-- Decor -->
                    <div class="absolute -right-20 -top-20 opacity-10">
                        <svg class="w-64 h-64" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
                            <path fill="#ffffff" d="M47.7,-57.2C59.6,-47.3,66.6,-30.3,71.2,-12.3C75.8,5.7,78.1,24.8,70.5,39.6C62.9,54.4,45.4,65.1,27.3,70.2C9.2,75.3,-9.6,74.9,-27.1,69C-44.6,63.1,-60.7,51.8,-69.5,35.9C-78.3,20,-79.7,0,-73.4,-17.1C-67,-34.2,-52.8,-48.5,-37.8,-57.4C-22.8,-66.3,-7.1,-69.8,8.2,-68.8C23.6,-67.7,47.3,-62.1,35.8,-67.2Z" transform="translate(100 100)" />
                        </svg>
                    </div>
                    
                    <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
                        <div>
                            <h3 class="text-green-300 font-bold uppercase tracking-widest text-sm mb-1">Cumulative Grade Point Average</h3>
                            <div class="flex items-baseline gap-2">
                                <span class="text-5xl font-black">{{ cgpa.toFixed(2) }}</span>
                                <span class="text-green-100 font-medium">/ 5.00</span>
                            </div>
                        </div>
                        
                        <div class="flex gap-8">
                            <div class="bg-white/10 rounded-2xl p-4 backdrop-blur-sm min-w-[140px]">
                                <p class="text-green-200 text-xs font-bold uppercase tracking-widest mb-1">Total Credits</p>
                                <p class="text-3xl font-bold">{{ cumulativeCredits }}</p>
                            </div>
                            <div class="bg-white/10 rounded-2xl p-4 backdrop-blur-sm min-w-[140px]">
                                <p class="text-green-200 text-xs font-bold uppercase tracking-widest mb-1">Semesters</p>
                                <p class="text-3xl font-bold">{{ resultsBySession.length }}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Session Results List -->
                <div class="space-y-6">
                    <div v-for="(sessionData, index) in resultsBySession" :key="index" class="bg-white rounded-3xl border border-gray-100 shadow-sm overflow-hidden">
                        
                        <div class="bg-gray-50/80 px-6 py-5 border-b border-gray-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                            <div>
                                <h4 class="font-bold text-gray-900 text-lg">{{ sessionData.session.name }}</h4>
                                <p class="text-sm text-gray-500 mt-0.5" v-if="sessionData.has_pending_grades">
                                    <span class="inline-flex items-center gap-1.5 text-amber-600 font-medium">
                                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                        Pending Grades
                                    </span>
                                </p>
                            </div>
                            
                            <div class="flex items-center gap-6">
                                <div>
                                    <p class="text-xs font-bold text-gray-400 uppercase tracking-widest">GPA</p>
                                    <p class="text-lg font-black text-gray-900">{{ sessionData.gpa.toFixed(2) }}</p>
                                </div>
                                <div>
                                    <p class="text-xs font-bold text-gray-400 uppercase tracking-widest">Credits</p>
                                    <p class="text-lg font-black text-gray-900">{{ sessionData.session_credits }}</p>
                                </div>
                            </div>
                        </div>

                        <div class="overflow-x-auto">
                            <table class="min-w-full divide-y divide-gray-100">
                                <thead class="bg-white">
                                    <tr>
                                        <th scope="col" class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase tracking-wider w-1/4">Course Code</th>
                                        <th scope="col" class="px-6 py-4 text-left text-xs font-bold text-gray-400 uppercase tracking-wider w-2/4">Course Title</th>
                                        <th scope="col" class="px-6 py-4 text-center text-xs font-bold text-gray-400 uppercase tracking-wider">Units</th>
                                        <th scope="col" class="px-6 py-4 text-center text-xs font-bold text-gray-400 uppercase tracking-wider">Score</th>
                                        <th scope="col" class="px-6 py-4 text-center text-xs font-bold text-gray-400 uppercase tracking-wider">Grade</th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-50">
                                    <tr v-for="reg in sessionData.registrations" :key="reg.id" class="hover:bg-gray-50/50 transition-colors">
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-noun-dark">
                                            {{ reg.course.code }}
                                        </td>
                                        <td class="px-6 py-4 text-sm text-gray-600 font-medium">
                                            {{ reg.course.title }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center font-medium">
                                            {{ reg.course.units }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-center">
                                            <span v-if="reg.score !== null" class="font-bold text-gray-900">{{ reg.score }}</span>
                                            <span v-else class="text-gray-300">-</span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-center">
                                            <span v-if="reg.grade" class="inline-flex items-center justify-center h-8 w-8 rounded-lg border font-black text-sm" :class="getGradeColor(reg.grade)">
                                                {{ reg.grade }}
                                            </span>
                                            <span v-else class="inline-flex items-center justify-center h-8 px-3 rounded-lg border border-gray-200 bg-gray-50 text-gray-400 font-medium text-xs">
                                                Pending
                                            </span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </StudentLayout>
</template>
