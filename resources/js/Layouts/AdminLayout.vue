<script setup>
import { ref } from 'vue';
import { Link, usePage } from '@inertiajs/vue3';
import Dropdown from '@/Components/Dropdown.vue';
import DropdownLink from '@/Components/DropdownLink.vue';

const showingNavigationDropdown = ref(false);

const navigation = [
    { name: 'Dashboard', href: route('admin.dashboard'), active: route().current('admin.dashboard'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
    { name: 'Applications', href: route('admin.applications.index'), active: route().current('admin.applications.*'), icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
    { name: 'Curriculum', href: route('admin.programmes.index'), active: route().current('admin.programmes.*') || route().current('admin.courses.*'), icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' },
    { name: 'Sessions', href: route('admin.sessions.index'), active: route().current('admin.sessions.*'), icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z' },
    { name: 'Upload Results', href: route('admin.results.upload'), active: route().current('admin.results.*'), icon: 'M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12' },
    { name: 'Payments', href: route('admin.payments.index'), active: route().current('admin.payments.*'), icon: 'M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z' },
    { name: 'Users', href: route('admin.users.index'), active: route().current('admin.users.*'), icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },
];
</script>

<template>
    <div class="min-h-screen bg-gray-50 flex">
        
        <!-- Sidebar Navigation (Desktop) -->
        <aside class="hidden md:flex md:w-64 md:flex-col fixed inset-y-0 left-0 z-20 bg-noun-dark shadow-xl transition-all duration-300">
            <div class="flex-1 flex flex-col min-h-0 overflow-y-auto">
                <!-- Branding -->
                <div class="h-20 flex items-center px-6 bg-[#002810] border-b border-[#004d1f] shrink-0">
                    <Link :href="route('admin.dashboard')" class="flex items-center gap-3 w-full">
                        <div class="h-10 w-10 bg-white rounded-lg flex items-center justify-center shadow-inner p-1 overflow-hidden shrink-0">
                            <img src="/nbs-logo.png" alt="NOUN" class="h-full w-auto object-contain">
                        </div>
                        <div class="min-w-0 flex flex-col justify-center">
                            <span class="text-[13px] font-black text-white tracking-widest block truncate leading-tight">BUSINESS SCHOOL</span>
                            <span class="text-[10px] text-noun-yellow font-bold uppercase tracking-widest block truncate leading-tight mt-0.5">Admin Portal</span>
                        </div>
                    </Link>
                </div>

                <nav class="flex-1 px-4 py-6 space-y-1.5">
                    <Link
                        v-for="item in navigation"
                        :key="item.name"
                        :href="item.href"
                        :class="[
                            item.active 
                                ? 'bg-white/10 text-white shadow-sm ring-1 ring-white/20' 
                                : 'text-gray-300 hover:bg-white/5 hover:text-white',
                            'group flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all duration-200'
                        ]"
                    >
                        <svg :class="[item.active ? 'text-noun-yellow' : 'text-gray-400 group-hover:text-gray-300', 'h-5 w-5 flex-shrink-0 transition-colors']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                        </svg>
                        <span class="flex-1">{{ item.name }}</span>
                        <!-- Active Indicator -->
                        <div v-if="item.active" class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div>
                    </Link>
                </nav>

                <div class="p-4 border-t border-white/10 shrink-0">
                    <Link 
                        :href="route('logout')" 
                        method="post" 
                        as="button" 
                        class="w-full flex items-center justify-center gap-2 px-4 py-2 text-sm font-semibold text-red-400 hover:text-red-300 hover:bg-red-400/10 rounded-lg transition-colors"
                    >
                        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" /></svg>
                        Sign Out
                    </Link>
                </div>
            </div>
        </aside>

        <!-- Main Content Area -->
        <div class="flex-1 md:ml-64 flex flex-col min-w-0 transition-all duration-300">
            
            <!-- Top Navbar (Mobile / Quick Actions) -->
            <header class="bg-white shadow-sm h-16 flex items-center justify-between px-4 sm:px-6 lg:px-8 border-b border-gray-200 z-10 sticky top-0">
                <div class="flex items-center md:hidden">
                    <button @click="showingNavigationDropdown = !showingNavigationDropdown" class="text-gray-500 hover:text-gray-900 focus:outline-none">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                    <span class="ml-4 font-bold text-noun-dark">NBS Admin</span>
                </div>
                
                <div class="hidden md:flex items-center text-sm font-medium text-gray-500">
                    <span id="header-date">{{ new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) }}</span>
                </div>

                <div class="flex items-center gap-4">
                    <!-- Notifications -->
                    <button class="text-gray-400 hover:text-noun-green relative">
                        <span class="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-500 ring-2 ring-white"></span>
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                        </svg>
                    </button>

                    <!-- Profile Dropdown -->
                    <Dropdown align="right" width="48">
                        <template #trigger>
                            <button type="button" class="flex items-center gap-2 focus:outline-none">
                                <div class="h-8 w-8 rounded-full bg-noun-green text-white flex items-center justify-center font-bold text-xs ring-2 ring-transparent hover:ring-noun-yellow transition">
                                    {{ $page.props.auth.user.first_name?.charAt(0) || $page.props.auth.user.name?.charAt(0) }}
                                </div>
                            </button>
                        </template>

                        <template #content>
                            <DropdownLink :href="route('profile.edit')">Settings</DropdownLink>
                            <div class="border-t border-gray-100"></div>
                            <DropdownLink :href="route('logout')" method="post" as="button">Sign Out</DropdownLink>
                        </template>
                    </Dropdown>
                </div>
            </header>

            <!-- Mobile menu -->
            <div v-show="showingNavigationDropdown" class="md:hidden bg-noun-dark z-20 absolute top-16 inset-x-0 shadow-lg border-b border-[#004d1f]">
                <div class="pt-2 pb-3 space-y-1">
                    <Link v-for="item in navigation" :key="item.name" :href="item.href"
                        :class="[
                            item.active ? 'bg-noun-green text-white border-l-4 border-noun-yellow' : 'text-gray-300 hover:bg-[#004d1f] hover:text-white',
                            'block pl-3 pr-4 py-3 text-base font-medium transition-colors'
                        ]">
                        {{ item.name }}
                    </Link>
                </div>
            </div>

            <!-- Page Header -->
            <div class="bg-white border-b border-gray-200" v-if="$slots.header">
                <div class="px-4 sm:px-6 lg:px-8 py-5">
                    <slot name="header" />
                </div>
            </div>

            <!-- Page Content -->
            <main class="flex-1 overflow-y-auto bg-gray-50">
                <slot />
            </main>
            
        </div>
    </div>
</template>
