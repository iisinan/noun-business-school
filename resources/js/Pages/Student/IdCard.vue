<script setup>
import { Head } from '@inertiajs/vue3';
import { onMounted } from 'vue';

const props = defineProps({
    user: Object,
    application: Object,
});

onMounted(() => {
    // We do not auto-print here so the student can preview first.
});
</script>

<template>
    <Head title="Student ID Card" />

    <div class="min-h-screen bg-gray-50 flex flex-col items-center py-10 print:py-0 print:bg-white relative">
        <!-- Action Buttons (Hidden in print) -->
        <div class="fixed top-6 right-6 flex gap-3 print:hidden z-50">
            <button @click="window.history.back()" class="px-4 py-2 bg-white border border-gray-300 text-gray-700 rounded-lg text-sm font-semibold shadow-sm hover:bg-gray-50 transition">
                Back
            </button>
            <button @click="window.print()" class="px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-semibold shadow-sm hover:bg-noun-dark transition inline-flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                Print ID Card
            </button>
        </div>

        <div class="mb-6 text-center print:hidden">
            <h1 class="text-2xl font-bold text-gray-900">Student Identity Card</h1>
            <p class="text-gray-500 text-sm mt-1">Please print this page in color on standard card stock.</p>
        </div>

        <!-- ID Card Front -->
        <div class="w-[210mm] h-[297mm] flex flex-col items-center print:w-auto print:h-auto print:block relative overflow-hidden bg-white shadow-sm print:shadow-none mx-auto print:mx-0 p-8">
            
            <!-- Card Container -->
            <div class="relative w-[54mm] h-[86mm] bg-white border-2 border-noun-green rounded-xl overflow-hidden shadow-2xl print:shadow-none shrink-0 print:m-0 mb-10 mx-auto" style="print-color-adjust: exact; -webkit-print-color-adjust: exact;">
                
                <!-- Background Pattern/Color -->
                <div class="absolute inset-0 z-0">
                    <div class="absolute inset-x-0 top-0 h-[40%] bg-gradient-to-b from-noun-dark to-noun-green"></div>
                    <!-- Watermark -->
                    <div class="absolute inset-0 flex items-center justify-center opacity-10 pt-20">
                        <img src="/nbs-logo.png" alt="Watermark" class="w-24">
                    </div>
                </div>

                <!-- Card Content -->
                <div class="relative z-10 flex flex-col h-full">
                    <!-- Header -->
                    <div class="text-center pt-3 pb-1.5 px-2 flex flex-col items-center">
                        <img src="/nbs-logo.png" alt="NOUN Logo" class="h-9 w-auto mb-1 bg-white p-1 rounded-full shadow-sm">
                        <h2 class="text-[11px] font-black text-white leading-tight uppercase tracking-widest">NOUN Business School</h2>
                        <h3 class="text-[6px] font-medium text-white/90 leading-tight uppercase tracking-wider mt-0.5">National Open University of Nigeria</h3>
                        <div class="bg-noun-yellow text-noun-dark text-[7px] font-bold px-2 py-0.5 rounded-full mt-1.5 uppercase tracking-widest shadow-sm">
                            Student ID Card
                        </div>
                    </div>

                    <!-- Photo -->
                    <div class="flex justify-center mt-2 mb-2">
                        <div class="w-20 h-24 bg-white p-0.5 rounded-lg shadow-md border-2 border-white overflow-hidden z-20">
                            <img v-if="$page.props.auth.user.passport_url" :src="$page.props.auth.user.passport_url" class="h-full w-full object-cover rounded-md" alt="Student Passport">
                            <div v-else class="h-full w-full bg-gray-100 flex items-center justify-center text-[10px] text-gray-400 text-center rounded-md">No Photo</div>
                        </div>
                    </div>

                    <!-- Details -->
                    <div class="flex-1 flex flex-col items-center text-center px-3">
                        <h3 class="text-xs font-bold text-gray-900 uppercase leading-tight mt-1">{{ user.first_name }} {{ user.last_name }}</h3>
                        
                        <div class="w-full mt-3 space-y-1.5">
                            <div class="flex flex-col">
                                <span class="text-[7px] font-bold text-noun-green uppercase tracking-wider">Matriculation No</span>
                                <span class="text-[10px] font-bold text-gray-800 font-mono leading-none">NBS/{{ application.academic_session_id }}/{{ String(application.id).padStart(4, '0') }}</span>
                            </div>
                            
                            <div class="flex flex-col">
                                <span class="text-[7px] font-bold text-noun-green uppercase tracking-wider">Programme</span>
                                <span class="text-[9px] font-bold text-gray-800 leading-tight">{{ application.programme?.name || 'N/A' }}</span>
                            </div>
                            
                            <div class="flex flex-col mt-1">
                                <span class="text-[7px] font-bold text-noun-green uppercase tracking-wider">Validity</span>
                                <span class="text-[8px] font-bold text-gray-800 leading-tight">2026 - 2028</span>
                            </div>
                        </div>
                    </div>

                    <!-- Footer Bar -->
                    <div class="h-4 bg-noun-dark w-full mt-auto"></div>
                </div>
            </div>
            
            <!-- Card Back -->
            <div class="relative w-[54mm] h-[86mm] bg-white border border-gray-300 rounded-xl overflow-hidden shadow-2xl print:shadow-none shrink-0 print:m-0 mx-auto" style="print-color-adjust: exact; -webkit-print-color-adjust: exact;">
                <div class="p-3 text-[8px] text-gray-800 leading-snug flex flex-col h-full justify-between">
                    <div>
                        <h4 class="font-bold text-noun-green text-[9px] uppercase border-b border-noun-green pb-1 mb-2">Conditions of Use</h4>
                        <ol class="list-decimal pl-3 space-y-1">
                            <li>This card remains the property of the National Open University of Nigeria (NOUN).</li>
                            <li>It is non-transferable and must be presented upon request by authorized university personnel.</li>
                            <li>Loss or damage must be reported immediately to the Registry.</li>
                            <li>If found, please return to the nearest NOUN Study Centre or Police Station.</li>
                        </ol>
                    </div>
                    
                    <div class="text-center mt-4">
                        <img :src="'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=NBS/' + application.academic_session_id + '/' + String(application.id).padStart(4, '0')" alt="QR Code" class="w-16 h-16 mx-auto mb-2 opacity-90">
                        <p class="text-[7px] text-gray-500">Scan to verify authenticity</p>
                    </div>
                    
                    <div class="text-center mt-2 border-t border-gray-200 pt-1">
                        <p class="font-bold text-noun-dark">Business School (NBS)</p>
                        <p class="text-[7px]">Plot 91, Cadastral Zone, Nnamdi Azikiwe Expressway, Jabi, Abuja, Nigeria.</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
