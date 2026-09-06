<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';

const deleteUser = (user) => {
    if (confirm(`Are you absolutely sure you want to COMPLETELY delete ${user.first_name} ${user.last_name}?\n\nThis will permanently destroy their application, payments, wallet balance, and results. This action CANNOT be undone.`)) {
        router.delete(route('admin.users.destroy', user.id), {
            preserveScroll: true
        });
    }
};
import { ref, watch } from 'vue';

function debounce(fn, wait) {
    let timer;
    return function (...args) {
        if (timer) clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), wait);
    };
}


const props = defineProps({
    users: Object,
    filters: Object
});

const search = ref(props.filters.search || '');
const role = ref(props.filters.role || '');

watch([search, role], debounce(function ([newSearch, newRole]) {
    router.get(route('admin.users.index'), { search: newSearch, role: newRole }, { preserveState: true, preserveScroll: true, replace: true });
}, 300));
</script>

<template>
    <Head title="User Management" />

    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">
                User Management
            </h2>
        </template>

        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8">
                
                <!-- Filters -->
                <div class="bg-white p-4 shadow-sm rounded-xl border border-gray-100 mb-6 flex flex-col sm:flex-row gap-4 justify-between items-center">
                    <div class="w-full sm:w-1/3">
                        <label class="sr-only">Search</label>
                        <div class="relative">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <svg class="h-5 w-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                                </svg>
                            </div>
                            <input
                                v-model="search"
                                type="text"
                                class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-noun-green focus:border-noun-green sm:text-sm transition"
                                placeholder="Search users by name or email..."
                            >
                        </div>
                    </div>
                    <div class="w-full sm:w-auto flex items-center gap-3">
                        <span class="text-sm text-gray-500 font-medium">Filter by Role:</span>
                        <select v-model="role" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-noun-green focus:border-noun-green sm:text-sm rounded-lg">
                            <option value="">All Roles</option>
                            <option value="Applicant">Applicant</option>
                            <option value="Student">Student</option>
                            <option value="Admin">Admin</option>
                            <option value="Super Admin">Super Admin</option>
                        </select>
                    </div>
                </div>

                <!-- Table -->
                <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead>
                                <tr class="bg-gray-50">
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">User</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Contact</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">System Role</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Wallet</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Joined</th>
                                    <th scope="col" class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Actions</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-100">
                                <tr v-for="user in users.data" :key="user.id" class="hover:bg-gray-50 transition-colors">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex items-center gap-3">
                                            <div class="h-9 w-9 rounded-full bg-noun-dark flex items-center justify-center text-white text-xs font-bold flex-shrink-0 shadow-inner">
                                                {{ user.first_name?.charAt(0) }}{{ user.last_name?.charAt(0) }}
                                            </div>
                                            <div>
                                                <Link :href="route('admin.users.show', user.id)" class="text-sm font-bold text-noun-green hover:underline">
                                                    {{ user.first_name }} {{ user.last_name }}
                                                </Link>
                                                <div class="text-xs text-gray-500 flex items-center gap-1 mt-0.5">
                                                    <span v-if="user.email_verified_at" class="text-green-500" title="Email Verified">
                                                        <svg class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor">
                                                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                                                        </svg>
                                                    </span>
                                                    <span v-else class="text-amber-500" title="Unverified Email">
                                                        <svg class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor">
                                                            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                                                        </svg>
                                                    </span>
                                                    ID: {{ user.id }}
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="text-sm text-gray-900 font-medium">{{ user.email }}</div>
                                        <div class="text-xs text-gray-500 mt-0.5">{{ user.phone || 'No phone' }}</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex gap-1 flex-wrap">
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
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700 font-medium">
                                        NGN {{ user.wallet_balance ? parseFloat(user.wallet_balance).toLocaleString() : '0' }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ new Date(user.created_at).toLocaleDateString() }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <Link :href="route('admin.users.show', user.id)" class="text-noun-green hover:text-noun-dark transition font-semibold mr-3">View</Link>
                                        <button @click="deleteUser(user)" class="text-red-500 hover:text-red-700 transition font-semibold">Delete</button>
                                    </td>
                                </tr>
                                <tr v-if="users.data.length === 0">
                                    <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-500">
                                        No users found matching your filters.
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Pagination -->
                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-50 flex flex-col sm:flex-row items-center justify-between gap-4">
                        <div class="text-sm text-gray-600">
                            Showing <span class="font-bold">{{ users.from || 0 }}</span> to <span class="font-bold">{{ users.to || 0 }}</span> of <span class="font-bold">{{ users.total }}</span> users
                        </div>
                        <div class="flex items-center gap-2">
                            <Link
                                v-if="users.prev_page_url"
                                :href="users.prev_page_url"
                                class="inline-flex items-center gap-1 px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium bg-white text-gray-700 hover:bg-gray-50 transition shadow-sm"
                            >
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                                </svg>
                                Previous
                            </Link>
                            <Link
                                v-if="users.next_page_url"
                                :href="users.next_page_url"
                                class="inline-flex items-center gap-1 px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium bg-white text-gray-700 hover:bg-gray-50 transition shadow-sm"
                            >
                                Next
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                </svg>
                            </Link>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </AdminLayout>
</template>
