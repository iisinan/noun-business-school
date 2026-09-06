<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link } from '@inertiajs/vue3';

const props = defineProps({
    user: Object,
});

const getInitials = (first, last) => {
    return (first?.charAt(0) || '') + (last?.charAt(0) || '');
};
</script>

<template>
    <Head :title="`${user.first_name} ${user.last_name}`" />

    <AdminLayout>
        <template #header>
            <div class="flex items-center gap-4">
                <Link :href="route('admin.users.index')" class="text-gray-500 hover:text-gray-700">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                </Link>
                <h2 class="text-xl font-semibold leading-tight text-gray-800">
                    User Details: {{ user.first_name }} {{ user.last_name }}
                </h2>
            </div>
        </template>

        <div class="py-8 w-full mx-auto sm:px-6 lg:px-8 space-y-6">
            
            <!-- User Profile Header -->
            <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100 flex flex-col md:flex-row gap-6 items-center">
                <div v-if="user.passport_url" class="h-20 w-20 rounded-full flex items-center justify-center flex-shrink-0 border border-gray-200 shadow-sm overflow-hidden bg-gray-50">
                    <img :src="user.passport_url" class="h-full w-full object-cover" alt="User Passport" />
                </div>
                <div v-else class="h-20 w-20 rounded-full bg-noun-dark flex items-center justify-center text-white text-2xl font-bold flex-shrink-0 shadow-inner">
                    {{ getInitials(user.first_name, user.last_name) }}
                </div>
                <div class="flex-grow text-center md:text-left">
                    <h3 class="text-2xl font-bold text-gray-900">{{ user.first_name }} {{ user.middle_name }} {{ user.last_name }}</h3>
                    <p class="text-gray-500">{{ user.email }} | {{ user.phone || 'No Phone' }}</p>
                    <div class="mt-2 flex gap-2 justify-center md:justify-start">
                        <span 
                            v-for="role in user.roles" 
                            :key="role.id" 
                            class="px-2 py-0.5 text-xs font-semibold rounded-md border"
                            :class="{
                                'bg-blue-50 text-blue-700 border-blue-200': role.name === 'Applicant',
                                'bg-green-50 text-green-700 border-green-200': role.name === 'Student',
                                'bg-purple-50 text-purple-700 border-purple-200': role.name === 'Super Admin' || role.name === 'Admin'
                            }"
                        >
                            {{ role.name }}
                        </span>
                        <span v-if="user.roles.length === 0" class="text-xs italic text-gray-400">No Role</span>
                    </div>
                </div>
                <div class="text-center md:text-right">
                    <p class="text-sm text-gray-500 font-medium">Wallet Balance</p>
                    <p class="text-3xl font-extrabold text-blue-600">NGN {{ user.wallet_balance ? parseFloat(user.wallet_balance).toLocaleString() : '0' }}</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Semester Registrations -->
                <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100">
                    <h3 class="text-lg font-bold mb-4 border-b pb-2">Semester Registrations</h3>
                    <div v-if="user.semester_registrations && user.semester_registrations.length > 0">
                        <ul class="space-y-3">
                            <li v-for="reg in user.semester_registrations" :key="reg.id" class="flex justify-between items-center bg-gray-50 p-3 rounded-lg border border-gray-200">
                                <div>
                                    <p class="font-semibold text-gray-800">{{ reg.academic_session.name }}</p>
                                    <p class="text-xs text-gray-500">{{ new Date(reg.created_at).toLocaleDateString() }}</p>
                                </div>
                                <div class="text-right">
                                    <p class="font-bold text-gray-900">NGN {{ parseFloat(reg.amount).toLocaleString() }}</p>
                                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                                        {{ reg.status.toUpperCase() }}
                                    </span>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div v-else class="text-gray-500 text-sm">
                        No semester registrations found.
                    </div>
                </div>

                <!-- Course Registrations -->
                <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100">
                    <h3 class="text-lg font-bold mb-4 border-b pb-2">Course Registrations</h3>
                    <div v-if="user.course_registrations && user.course_registrations.length > 0" class="overflow-y-auto max-h-80">
                        <ul class="space-y-3">
                            <li v-for="creg in user.course_registrations" :key="creg.id" class="bg-gray-50 p-3 rounded-lg border border-gray-200">
                                <div class="flex justify-between items-start">
                                    <div>
                                        <p class="font-semibold text-gray-800">{{ creg.course.code }}: {{ creg.course.title }}</p>
                                        <p class="text-xs text-gray-500">{{ creg.academic_session.name }} &bull; {{ creg.course.units }} Units</p>
                                    </div>
                                    <div class="text-right flex flex-col items-end gap-1">
                                        <div v-if="creg.grade" class="flex items-center gap-2">
                                            <span class="px-2 py-0.5 rounded text-xs font-bold" :class="creg.grade === 'F' ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'">
                                                {{ creg.score }} ({{ creg.grade }})
                                            </span>
                                            <span class="text-xs text-gray-500 font-bold">{{ creg.grade_points }} GP</span>
                                        </div>
                                        <span v-else class="px-2 py-0.5 rounded text-xs font-bold bg-yellow-100 text-yellow-700">
                                            Pending Result
                                        </span>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div v-else class="text-gray-500 text-sm">
                        No course registrations found.
                    </div>
                </div>

                <!-- Wallet Transactions -->
                <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100 lg:col-span-2">
                    <h3 class="text-lg font-bold mb-4 border-b pb-2">Wallet Transactions</h3>
                    <div v-if="user.wallet_transactions && user.wallet_transactions.length > 0" class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th scope="col" class="px-4 py-2 text-left text-xs font-semibold text-gray-500 uppercase">Date</th>
                                    <th scope="col" class="px-4 py-2 text-left text-xs font-semibold text-gray-500 uppercase">Description</th>
                                    <th scope="col" class="px-4 py-2 text-left text-xs font-semibold text-gray-500 uppercase">Type</th>
                                    <th scope="col" class="px-4 py-2 text-right text-xs font-semibold text-gray-500 uppercase">Amount</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr v-for="tx in user.wallet_transactions" :key="tx.id" class="hover:bg-gray-50">
                                    <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-500">
                                        {{ new Date(tx.created_at).toLocaleString() }}
                                    </td>
                                    <td class="px-4 py-3 text-sm text-gray-900">
                                        {{ tx.description }}
                                    </td>
                                    <td class="px-4 py-3 whitespace-nowrap">
                                        <span class="px-2 py-1 text-xs font-semibold rounded-md border bg-gray-50 text-gray-600 border-gray-200">
                                            {{ tx.type }}
                                        </span>
                                    </td>
                                    <td class="px-4 py-3 whitespace-nowrap text-right text-sm font-bold" :class="tx.amount > 0 ? 'text-green-600' : 'text-red-600'">
                                        {{ tx.amount > 0 ? '+' : '' }}NGN {{ parseFloat(tx.amount).toLocaleString() }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div v-else class="text-gray-500 text-sm">
                        No wallet transactions found.
                    </div>
                </div>
            </div>

        </div>
    </AdminLayout>
</template>
