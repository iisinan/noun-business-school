<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';


const props = defineProps({
    payments: Object,
    filters: Object,
    stats: Object
});

const search = ref(props.filters.search || '');
const status = ref(props.filters.status || '');

// Using custom debounce to prevent vite issues if lodash isn't installed
function customDebounce(fn, wait) {
    let timer;
    return function (...args) {
        if (timer) clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), wait);
    };
}

watch([search, status], customDebounce(function ([newSearch, newStatus]) {
    router.get(route('admin.payments.index'), { search: newSearch, status: newStatus }, { preserveState: true, preserveScroll: true, replace: true });
}, 300));
</script>

<template>
    <Head title="Financial Ledger" />
    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">Financial Ledger</h2>
        </template>

        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8 space-y-6">
                
                <!-- Financial Overview Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex items-center gap-4 border-l-4 border-l-noun-green">
                        <div class="h-12 w-12 rounded-full bg-green-50 flex items-center justify-center text-noun-green">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        </div>
                        <div>
                            <div class="text-sm font-medium text-gray-500">Total Revenue Collected</div>
                            <div class="text-2xl font-bold text-gray-900">₦{{ Number(stats.total_revenue).toLocaleString() }}</div>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex items-center gap-4 border-l-4 border-l-blue-500">
                        <div class="h-12 w-12 rounded-full bg-blue-50 flex items-center justify-center text-blue-500">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        </div>
                        <div>
                            <div class="text-sm font-medium text-gray-500">Successful Transactions</div>
                            <div class="text-2xl font-bold text-gray-900">{{ stats.total_transactions }}</div>
                        </div>
                    </div>
                    <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6 flex items-center gap-4 border-l-4 border-l-amber-500">
                        <div class="h-12 w-12 rounded-full bg-amber-50 flex items-center justify-center text-amber-500">
                            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                        </div>
                        <div>
                            <div class="text-sm font-medium text-gray-500">Pending Value (Unpaid)</div>
                            <div class="text-2xl font-bold text-gray-900">₦{{ Number(stats.pending_amount).toLocaleString() }}</div>
                        </div>
                    </div>
                </div>

                <!-- Filters -->
                <div class="bg-white p-4 shadow-sm rounded-xl border border-gray-100 flex flex-col sm:flex-row gap-4 justify-between items-center">
                    <div class="w-full sm:w-1/3 relative">
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                        </div>
                        <input
                            v-model="search"
                            type="text"
                            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg leading-5 bg-white placeholder-gray-500 focus:outline-none focus:ring-noun-green focus:border-noun-green sm:text-sm transition"
                            placeholder="Search RRR, Ref, or Payer Name..."
                        >
                    </div>
                    <div class="w-full sm:w-auto flex items-center gap-3">
                        <span class="text-sm text-gray-500 font-medium">Status:</span>
                        <select v-model="status" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-noun-green focus:border-noun-green sm:text-sm rounded-lg">
                            <option value="">All Payments</option>
                            <option value="PAID">Paid / Successful</option>
                            <option value="PENDING">Pending</option>
                            <option value="FAILED">Failed</option>
                        </select>
                    </div>
                </div>

                <!-- Table -->
                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead>
                                <tr class="bg-gray-50">
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Transaction Ref / RRR</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Payer</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Payment Type</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Amount</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Date</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-100">
                                <tr v-for="payment in payments.data" :key="payment.id" class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="text-sm font-bold text-gray-900">{{ payment.transaction_reference }}</div>
                                        <div class="text-xs text-gray-500 mt-1">RRR: <span class="font-mono text-noun-green">{{ payment.rrr || 'Pending' }}</span></div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="text-sm font-medium text-gray-900">{{ payment.user?.first_name }} {{ payment.user?.last_name }}</div>
                                        <div class="text-xs text-gray-500">{{ payment.user?.email }}</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2 py-1 text-xs font-bold rounded-md bg-gray-100 text-gray-700 border border-gray-200">
                                            {{ payment.payment_type.replace('_', ' ') }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">
                                        ₦{{ Number(payment.amount).toLocaleString() }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 text-xs font-semibold rounded-full"
                                            :class="{
                                                'bg-green-100 text-green-800': payment.status === 'PAID' || payment.status === 'SUCCESSFUL',
                                                'bg-amber-100 text-amber-800': payment.status === 'PENDING',
                                                'bg-red-100 text-red-800': payment.status === 'FAILED'
                                            }">
                                            {{ payment.status }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ new Date(payment.created_at).toLocaleString() }}
                                    </td>
                                </tr>
                                <tr v-if="!payments.data.length">
                                    <td colspan="6" class="px-6 py-12 text-center text-sm text-gray-500">No payment records found.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <!-- Pagination -->
                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-50 flex items-center justify-between">
                        <div class="text-sm text-gray-600">
                            Showing <span class="font-bold">{{ payments.from || 0 }}</span> to <span class="font-bold">{{ payments.to || 0 }}</span> of <span class="font-bold">{{ payments.total }}</span>
                        </div>
                        <div class="flex gap-2">
                            <Link v-if="payments.prev_page_url" :href="payments.prev_page_url" class="px-3 py-1.5 border rounded-lg text-sm bg-white hover:bg-gray-50">Prev</Link>
                            <Link v-if="payments.next_page_url" :href="payments.next_page_url" class="px-3 py-1.5 border rounded-lg text-sm bg-white hover:bg-gray-50">Next</Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AdminLayout>
</template>
