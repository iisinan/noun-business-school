<script setup>
import { Head, useForm } from '@inertiajs/vue3';
import StudentLayout from '@/Layouts/StudentLayout.vue';
import { ref } from 'vue';

const props = defineProps({
    wallet_balance: Number,
    walletTransactions: { type: Array, default: () => [] },
    gatewayPayments: { type: Array, default: () => [] },
});

const activeTab = ref('wallet');

const topupForm = useForm({ amount: '', type: 'WALLET_TOPUP' });
const submitTopup = () => {
    if (!topupForm.amount || topupForm.amount < 1000) {
        alert('Minimum top-up amount is NGN 1,000.');
        return;
    }
    topupForm.get(route('applicant.payment.initiate'));
};

const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-GB', {
        day: 'numeric', month: 'short', year: 'numeric',
        hour: '2-digit', minute:'2-digit'
    });
};
</script>

<template>
    <Head title="Payment History" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Payment History</h2>
        </template>
        
        <div class="py-8 px-4 sm:px-6 lg:px-8 ">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start">
                
                <!-- ── Main History Area (Left 2 cols) ── -->
                <div class="lg:col-span-2 space-y-6">
                    
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <!-- Tabs -->
                        <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-1 inline-flex w-full sm:w-auto">
                            <button 
                                @click="activeTab = 'wallet'" 
                                class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                                :class="activeTab === 'wallet' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                            >
                                Wallet Ledger
                            </button>
                            <button 
                                @click="activeTab = 'gateway'" 
                                class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                                :class="activeTab === 'gateway' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                            >
                                External Payments
                            </button>
                        </div>
                        
                        <!-- Print Statement Button -->
                        <a v-if="activeTab === 'wallet'" :href="route('student.payments.statement')" target="_blank" class="inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-gray-900 text-white font-bold text-sm rounded-xl hover:bg-black transition shadow-sm">
                            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                            Download Statement
                        </a>
                    </div>

                    <!-- Wallet Ledger View -->
                    <div v-if="activeTab === 'wallet'" class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
                        <div class="px-6 py-5 border-b border-gray-100 flex items-center justify-between">
                            <h3 class="font-bold text-gray-900 text-lg">Wallet Ledger</h3>
                        </div>
                        <div v-if="walletTransactions.length === 0" class="p-8 text-center text-gray-400">
                            <p class="text-sm">No wallet transactions found.</p>
                        </div>
                        <div v-else class="overflow-x-auto">
                            <table class="min-w-full divide-y divide-gray-100">
                                <thead class="bg-gray-50">
                                    <tr>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Date</th>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Description</th>
                                        <th scope="col" class="px-6 py-3.5 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Amount</th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-50">
                                    <tr v-for="tx in walletTransactions" :key="tx.id" class="hover:bg-gray-50/50 transition-colors">
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(tx.created_at) }}</td>
                                        <td class="px-6 py-4 text-sm text-gray-900 font-medium">
                                            <div class="flex items-center gap-3">
                                                <div class="h-8 w-8 rounded-full flex items-center justify-center flex-shrink-0" :class="tx.amount > 0 ? 'bg-emerald-100' : 'bg-red-100'">
                                                    <svg v-if="tx.amount > 0" class="w-4 h-4 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M7 11l5-5m0 0l5 5m-5-5v12" /></svg>
                                                    <svg v-else class="w-4 h-4 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M17 13l-5 5m0 0l-5-5m5 5V6" /></svg>
                                                </div>
                                                <span>{{ tx.description }}</span>
                                            </div>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-bold" :class="tx.amount > 0 ? 'text-emerald-600' : 'text-red-500'">
                                            {{ tx.amount > 0 ? '+' : '' }}₦{{ Math.abs(parseInt(tx.amount)).toLocaleString() }}
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- External Payments View -->
                    <div v-if="activeTab === 'gateway'" class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
                        <div class="px-6 py-5 border-b border-gray-100 flex items-center justify-between">
                            <h3 class="font-bold text-gray-900 text-lg">Gateway Payments</h3>
                        </div>
                        <div v-if="gatewayPayments.length === 0" class="p-8 text-center text-gray-400">
                            <p class="text-sm">No external payments found.</p>
                        </div>
                        <div v-else class="overflow-x-auto">
                            <table class="min-w-full divide-y divide-gray-100">
                                <thead class="bg-gray-50">
                                    <tr>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Date</th>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Reference</th>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>
                                        <th scope="col" class="px-6 py-3.5 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                        <th scope="col" class="px-6 py-3.5 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Amount</th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-50">
                                    <tr v-for="pay in gatewayPayments" :key="pay.id" class="hover:bg-gray-50/50 transition-colors">
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ formatDate(pay.created_at) }}</td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ pay.transaction_reference }}</td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                            {{ pay.payment_type.replace('_', ' ') }}
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap">
                                            <span 
                                                class="px-2.5 py-1 text-xs font-bold rounded-md"
                                                :class="{
                                                    'bg-emerald-100 text-emerald-700': pay.status === 'PAID',
                                                    'bg-amber-100 text-amber-700': pay.status === 'PENDING',
                                                    'bg-red-100 text-red-700': pay.status === 'FAILED' || pay.status === 'CANCELLED'
                                                }"
                                            >
                                                {{ pay.status }}
                                            </span>
                                        </td>
                                        <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-bold text-gray-900">
                                            ₦{{ parseFloat(pay.amount).toLocaleString() }}
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>

                <!-- ── Right Sidebar ── -->
                <div class="space-y-6">
                    <!-- Wallet Balance Card -->
                    <div class="bg-gradient-to-br from-noun-dark to-noun-green rounded-2xl p-6 text-white shadow-noun">
                        <div class="flex items-start justify-between">
                            <div>
                                <p class="text-green-300 text-xs font-semibold uppercase tracking-widest mb-1">Wallet Balance</p>
                                <p class="text-3xl font-black tracking-tight">₦{{ wallet_balance ? parseFloat(wallet_balance).toLocaleString() : '0' }}</p>
                            </div>
                            <div class="h-10 w-10 rounded-xl bg-white/10 flex items-center justify-center">
                                <svg class="w-5 h-5 text-noun-yellow" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" /></svg>
                            </div>
                        </div>
                        <div class="mt-5 pt-5 border-t border-white/10">
                            <p class="text-sm text-green-100 mb-3">Add funds to your wallet via Remita to pay for course registrations and other fees.</p>
                            <form @submit.prevent="submitTopup" class="flex gap-2">
                                <input
                                    type="number"
                                    v-model="topupForm.amount"
                                    placeholder="Amount"
                                    min="1000"
                                    class="flex-1 text-sm rounded-lg border-0 bg-white/15 text-white placeholder-green-300 focus:ring-2 focus:ring-noun-yellow px-3 py-2"
                                />
                                <button type="submit" :disabled="topupForm.processing" class="px-4 py-2 bg-noun-yellow text-noun-dark font-bold text-sm rounded-lg hover:bg-yellow-400 transition disabled:opacity-50 whitespace-nowrap">
                                    Top Up
                                </button>
                            </form>
                        </div>
                    </div>
                    
                    <!-- Support Card -->
                    <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-5">
                        <div class="h-10 w-10 rounded-xl bg-blue-50 flex items-center justify-center mb-3">
                            <svg class="w-5 h-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
                        </div>
                        <h4 class="font-bold text-gray-900 text-sm mb-1">Need help with a payment?</h4>
                        <p class="text-xs text-gray-500 mb-3">If a payment was deducted but is not reflecting in your wallet, please contact bursary.</p>
                        <a href="mailto:bursary@noun.edu.ng" class="text-sm font-bold text-noun-green hover:underline">Contact Bursary</a>
                    </div>
                </div>

            </div>
        </div>
    </StudentLayout>
</template>
