<script setup>
import { Head, useForm } from '@inertiajs/vue3';

const props = defineProps({
    payment: Object
});

const form = useForm({
    rrr: props.payment.rrr
});

const processPayment = () => {
    form.post(route('remita.pay'));
};
</script>

<template>
    <Head title="Remita Payment Gateway" />

    <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8 font-sans">
        
        <div class="sm:mx-auto sm:w-full sm:max-w-md text-center mb-8">
            <!-- Simulated Remita Logo -->
            <div class="mx-auto h-12 w-32 bg-orange-500 flex items-center justify-center rounded text-white font-black text-xl tracking-wider italic shadow-sm">
                REMITA
            </div>
            <h2 class="mt-6 text-center text-xl font-extrabold text-gray-900">
                Secure Payment Gateway
            </h2>
            <p class="text-sm text-gray-500 mt-2">Test Environment - No real funds will be deducted</p>
        </div>

        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10 border-t-4 border-orange-500">
                
                <div class="mb-8 border-b border-gray-100 pb-6 text-center">
                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Paying To</p>
                    <p class="font-bold text-gray-900 mb-4">NOUN Business School (NBS)</p>
                    
                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Amount Due</p>
                    <p class="text-4xl font-black text-gray-900 tracking-tighter">₦{{ Number(payment.amount).toLocaleString() }}</p>
                </div>

                <div class="space-y-4 mb-8 bg-gray-50 p-4 rounded-lg text-sm">
                    <div class="flex justify-between">
                        <span class="text-gray-500">RRR:</span>
                        <span class="font-bold text-gray-900 font-mono">{{ payment.rrr }}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-500">Payer Name:</span>
                        <span class="font-bold text-gray-900">{{ payment.user.first_name }} {{ payment.user.last_name }}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-500">Payer Email:</span>
                        <span class="font-bold text-gray-900">{{ payment.user.email }}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-500">Description:</span>
                        <span class="font-bold text-gray-900">{{ payment.payment_type.replace('_', ' ') }}</span>
                    </div>
                </div>

                <form @submit.prevent="processPayment" class="space-y-6">
                    
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Card Number</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input type="text" class="focus:ring-orange-500 focus:border-orange-500 block w-full pl-3 pr-12 sm:text-sm border-gray-300 rounded-md py-2.5" placeholder="0000 0000 0000 0000" value="4532 1234 5678 9010" readonly>
                            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                                <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
                                </svg>
                            </div>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Expiry Date</label>
                            <input type="text" class="mt-1 focus:ring-orange-500 focus:border-orange-500 block w-full sm:text-sm border-gray-300 rounded-md py-2.5" placeholder="MM/YY" value="12/25" readonly>
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">CVV</label>
                            <input type="text" class="mt-1 focus:ring-orange-500 focus:border-orange-500 block w-full sm:text-sm border-gray-300 rounded-md py-2.5" placeholder="123" value="123" readonly>
                        </div>
                    </div>

                    <div>
                        <button type="submit" :disabled="form.processing" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-bold text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 transition disabled:opacity-70">
                            <span v-if="form.processing" class="flex items-center gap-2">
                                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                                Processing...
                            </span>
                            <span v-else>Pay ₦{{ Number(payment.amount).toLocaleString() }}</span>
                        </button>
                    </div>
                    
                    <div class="text-center">
                        <a :href="route('dashboard')" class="text-sm text-gray-500 hover:text-gray-900 underline">Cancel Payment</a>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>
