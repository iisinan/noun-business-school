<script setup>
import { ref } from 'vue';
import { Link, router, usePage } from '@inertiajs/vue3';
import Dropdown from '@/Components/Dropdown.vue';
import DropdownLink from '@/Components/DropdownLink.vue';

const page = usePage();
const user = page.props.auth.user;
const sidebarOpen = ref(false);

const navigation = [
    { header: 'MAIN' },
    { name: 'Dashboard', href: route('student.dashboard'), active: route().current('student.dashboard'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
    { header: 'ACADEMICS' },
    { name: 'Course Registration', href: route('student.registration'), active: route().current('student.registration'), icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' },
    { name: 'My Results', href: route('student.results'), active: route().current('student.results'), icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
    { header: 'RECORDS' },
    { name: 'ID Card', href: route('student.idcard'), active: route().current('student.idcard'), icon: 'M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2' },
    { header: 'FINANCE' },
    { name: 'Payment History', href: route('student.payments'), active: route().current('student.payments'), icon: 'M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z' },
];
</script>

<template>
    <div class="min-h-screen bg-gray-50 flex">
        <!-- Mobile Sidebar Overlay -->
        <div v-if="sidebarOpen" class="fixed inset-0 z-40 bg-gray-900/80 backdrop-blur-sm lg:hidden transition-opacity" @click="sidebarOpen = false"></div>

        <!-- Sidebar -->
        <aside :class="[sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0']" class="fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-noun-dark to-[#004d00] text-white transition-transform duration-300 ease-in-out flex flex-col shadow-2xl lg:shadow-none lg:static">
            
            <!-- Branding -->
            <div class="h-20 flex items-center px-6 bg-noun-dark border-b border-white/10 shrink-0">
                <Link :href="route('home')" class="flex items-center gap-3 w-full">
                    <div class="h-10 w-10 bg-white rounded-lg flex items-center justify-center shadow-inner p-1 overflow-hidden shrink-0">
                        <img src="/nbs-logo.png" alt="NOUN" class="h-full w-auto object-contain">
                    </div>
                    <div class="min-w-0">
                        <span class="text-sm font-black text-white tracking-widest block truncate">BUSINESS SCHOOL</span>
                        <span class="text-[10px] text-noun-yellow font-bold uppercase tracking-widest block truncate">Student Portal</span>
                    </div>
                </Link>
                <!-- Mobile Close -->
                <button @click="sidebarOpen = false" class="lg:hidden text-gray-400 hover:text-white p-2 ml-auto shrink-0">
                    <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <div class="flex-1 overflow-y-auto py-6 px-4 space-y-1.5">
                <template v-for="(item, index) in navigation" :key="index">
                    <!-- Section Header -->
                    <div v-if="item.header" class="px-4 pt-4 pb-1 text-[10px] font-black text-gray-400 uppercase tracking-widest">
                        {{ item.header }}
                    </div>
                    
                    <!-- Navigation Link -->
                    <component 
                        :is="item.href === '#' ? 'div' : Link" 
                        v-else 
                        :href="item.href !== '#' ? item.href : undefined"
                        :class="[
                            item.active 
                                ? 'bg-white/10 text-white shadow-sm ring-1 ring-white/20' 
                                : 'text-gray-300 hover:bg-white/5 hover:text-white',
                            item.href === '#' ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer',
                            'group flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all duration-200'
                        ]"
                    >
                        <svg :class="[item.active ? 'text-noun-yellow' : 'text-gray-400 group-hover:text-gray-300', 'h-5 w-5 shrink-0 transition-colors']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                        </svg>
                        <span class="flex-1">{{ item.name }}</span>
                        <!-- Active Indicator -->
                        <div v-if="item.active" class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div>
                    </component>
                </template>
            </div>

            <!-- User Profile (Bottom) -->
            <div class="p-4 border-t border-white/10 shrink-0">
                <div class="flex items-center gap-3 bg-white/5 rounded-xl p-3 border border-white/10">
                    <div v-if="user.passport_url" class="h-10 w-10 rounded-lg flex items-center justify-center shrink-0 border border-white/20 shadow-sm overflow-hidden bg-white/5">
                        <img :src="user.passport_url" class="h-full w-full object-cover" alt="Profile" />
                    </div>
                    <div v-else class="h-10 w-10 rounded-lg bg-noun-green flex items-center justify-center text-white font-bold shrink-0 shadow-inner">
                        {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                    </div>
                    <div class="min-w-0 flex-1">
                        <p class="text-sm font-bold text-white truncate">{{ user.first_name }} {{ user.last_name }}</p>
                        <p class="text-xs text-noun-yellow truncate">{{ user.email }}</p>
                    </div>
                </div>
                <Link :href="route('logout')" method="post" as="button" class="mt-3 w-full flex items-center justify-center gap-2 px-4 py-2 text-sm font-semibold text-red-400 hover:text-red-300 hover:bg-red-400/10 rounded-lg transition-colors">
                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" /></svg>
                    Log Out
                </Link>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1 flex flex-col min-w-0 overflow-hidden bg-gray-50/50">
            <!-- Topbar -->
            <header class="h-20 bg-white border-b border-gray-100 flex items-center justify-between px-4 sm:px-6 lg:px-8 shrink-0 shadow-sm z-10">
                <div class="flex items-center gap-4">
                    <button @click="sidebarOpen = true" class="lg:hidden p-2 text-gray-500 hover:bg-gray-100 rounded-lg">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/></svg>
                    </button>
                    <!-- Header Slot -->
                    <slot name="header"></slot>
                </div>

                <div class="flex items-center gap-4">
                    <Dropdown align="right" width="48">
                        <template #trigger>
                            <button class="flex items-center gap-2 text-sm font-semibold text-gray-600 hover:text-gray-900 p-2 rounded-lg hover:bg-gray-50 transition border border-transparent hover:border-gray-200">
                                <span>{{ user.first_name }}</span>
                                <svg class="h-4 w-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                                </svg>
                            </button>
                        </template>
                        <template #content>
                            <DropdownLink :href="route('profile.edit')">Profile Settings</DropdownLink>
                            <div class="border-t border-gray-100"></div>
                            <DropdownLink :href="route('logout')" method="post" as="button" class="text-red-600">Log Out</DropdownLink>
                        </template>
                    </Dropdown>
                </div>
            </header>

            <!-- Page Content -->
            <div class="flex-1 overflow-y-auto">
                <slot />
            </div>
        </main>
    </div>
</template>
