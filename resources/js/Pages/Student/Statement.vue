<script setup>
import { Head } from '@inertiajs/vue3';
import { onMounted } from 'vue';

const props = defineProps({
    user: Object,
    application: Object,
    walletTransactions: { type: Array, default: () => [] },
    wallet_balance: Number
});

const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-GB', {
        day: 'numeric', month: 'short', year: 'numeric',
        hour: '2-digit', minute:'2-digit'
    });
};

onMounted(() => {
    // Automatically trigger print dialog when component is mounted
    setTimeout(() => {
        window.print();
    }, 500);
});
</script>

<template>
    <Head title="Wallet Statement" />
    
    <div class="min-h-screen bg-gray-100 p-8 print:bg-white print:p-0">
        <!-- A4 Page Container -->
        <div class="max-w-[210mm] min-h-[297mm] mx-auto bg-white shadow-2xl print:shadow-none p-12 relative overflow-hidden">
            
            <!-- Watermark -->
            <div class="absolute inset-0 z-0 flex items-center justify-center opacity-[0.03] pointer-events-none">
                <img src="/nbs-logo.png" alt="" class="w-[500px] h-[500px] object-contain grayscale">
            </div>

            <!-- Print Header -->
            <div class="relative z-10 text-center border-b-2 border-noun-dark pb-6 mb-8 flex items-center justify-between">
                <img src="/nbs-logo.png" alt="NOUN Logo" class="h-24 w-auto object-contain">
                <div class="text-right">
                    <h1 class="text-2xl font-black text-noun-dark tracking-wide uppercase">NOUN Business School</h1>
                    <p class="text-gray-600 font-semibold mt-1">Wallet Financial Statement</p>
                    <p class="text-gray-500 text-sm mt-1">Generated: {{ new Date().toLocaleDateString('en-GB') }}</p>
                </div>
            </div>

            <!-- Student Info Grid -->
            <div class="relative z-10 grid grid-cols-2 gap-8 mb-8 border border-gray-200 rounded-lg p-5">
                <div>
                    <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Student Details</p>
                    <p class="text-lg font-bold text-gray-900">{{ user.last_name }}, {{ user.first_name }} {{ user.middle_name || '' }}</p>
                    <p class="text-sm font-semibold text-gray-600">{{ user.email }}</p>
                    <p class="text-sm font-bold text-noun-green mt-1">{{ application?.matric_number || application?.application_number }}</p>
                </div>
                <div class="text-right">
                    <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Current Balance</p>
                    <p class="text-2xl font-black text-gray-900">₦{{ wallet_balance.toLocaleString() }}</p>
                    <p class="text-sm text-gray-500 mt-1 font-medium">Programme: {{ application?.programme?.name }}</p>
                </div>
            </div>

            <!-- Transactions Table -->
            <div class="relative z-10 mb-12">
                <h3 class="text-lg font-bold text-gray-900 mb-4 border-b pb-2">Transaction History</h3>
                <table class="w-full text-left text-sm border-collapse">
                    <thead>
                        <tr class="bg-gray-100 border-y border-gray-300">
                            <th class="py-3 px-4 font-bold text-gray-700 w-1/4">Date</th>
                            <th class="py-3 px-4 font-bold text-gray-700 w-1/2">Description</th>
                            <th class="py-3 px-4 font-bold text-gray-700 text-right w-1/4">Amount</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-200">
                        <tr v-for="tx in walletTransactions" :key="tx.id">
                            <td class="py-3 px-4 text-gray-600">{{ formatDate(tx.created_at) }}</td>
                            <td class="py-3 px-4 font-medium text-gray-800">{{ tx.description }}</td>
                            <td class="py-3 px-4 text-right font-bold" :class="tx.amount > 0 ? 'text-emerald-700' : 'text-red-700'">
                                {{ tx.amount > 0 ? '+' : '' }}₦{{ Math.abs(parseInt(tx.amount)).toLocaleString() }}
                            </td>
                        </tr>
                        <tr v-if="walletTransactions.length === 0">
                            <td colspan="3" class="py-8 text-center text-gray-500 italic">No transactions recorded.</td>
                        </tr>
                    </tbody>
                    <tfoot v-if="walletTransactions.length > 0">
                        <tr class="bg-gray-50 border-y border-gray-300">
                            <td colspan="2" class="py-4 px-4 text-right font-bold text-gray-700">Final Wallet Balance:</td>
                            <td class="py-4 px-4 text-right font-black text-gray-900 text-lg border-t-2 border-gray-800">
                                ₦{{ wallet_balance.toLocaleString() }}
                            </td>
                        </tr>
                    </tfoot>
                </table>
            </div>



            <!-- Action buttons (hidden in print) -->
            <div class="fixed top-8 right-8 print:hidden flex gap-4">
                <button @click="window.print()" class="px-6 py-3 bg-noun-green text-white font-bold rounded-xl shadow-lg hover:bg-noun-dark transition flex items-center gap-2">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
                    Print Statement
                </button>
                <a :href="route('student.payments')" class="px-6 py-3 bg-white text-gray-700 font-bold rounded-xl shadow-lg hover:bg-gray-50 transition border border-gray-200">
                    Back to Portal
                </a>
            </div>
        </div>
    </div>
</template>
