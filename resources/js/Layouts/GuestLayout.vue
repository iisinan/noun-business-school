<script setup>
import { Link } from '@inertiajs/vue3';
</script>

<template>
    <div class="min-h-screen flex bg-gray-50 font-sans antialiased">
        <!-- Left Banner -->
        <div class="hidden lg:flex lg:w-1/2 bg-noun-dark relative overflow-hidden items-center justify-center">
            <!-- Subtle pattern overlay -->
            <div class="absolute inset-0 opacity-10">
                <div class="absolute top-0 left-0 w-64 h-64 bg-noun-yellow rounded-full -translate-x-1/2 -translate-y-1/2"></div>
                <div class="absolute bottom-0 right-0 w-96 h-96 bg-noun-green rounded-full translate-x-1/3 translate-y-1/3"></div>
            </div>

            <div class="relative z-10 p-12 text-white max-w-lg text-center">
                <Link href="/">
                    <div class="flex items-center justify-center gap-3 mb-8 group cursor-pointer">
                        <img src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-24 w-auto group-hover:opacity-80 transition drop-shadow-lg" />
                    </div>
                </Link>
                <h1 class="text-4xl font-extrabold tracking-tight mb-4">NOUN Business School</h1>
                <div class="w-12 h-1 bg-noun-yellow rounded-full mx-auto mb-4"></div>
                <p class="text-base text-green-200 leading-relaxed">
                    Portal Access for Applicants, Students, and Administrators. Empowering future global leaders through flexible, accessible education.
                </p>

                <div class="mt-10 grid grid-cols-3 gap-4 text-center">
                    <div>
                        <div class="text-3xl font-bold text-noun-yellow">98%</div>
                        <div class="text-xs text-green-300 mt-1">Employment Rate</div>
                    </div>
                    <div>
                        <div class="text-3xl font-bold text-noun-yellow">50+</div>
                        <div class="text-xs text-green-300 mt-1">Global Partners</div>
                    </div>
                    <div>
                        <div class="text-3xl font-bold text-noun-yellow">12k</div>
                        <div class="text-xs text-green-300 mt-1">Alumni</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Right Side (Auth Form) -->
        <div class="flex-1 flex flex-col justify-center items-center py-12 px-4 sm:px-6 lg:px-20 xl:px-24 relative">
            <Link :href="route('home')" class="absolute top-8 left-8 sm:left-12 flex items-center gap-2 text-sm font-semibold text-gray-500 hover:text-gray-900 transition bg-white px-4 py-2 rounded-full shadow-sm border border-gray-200">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" /></svg>
                Back to Home
            </Link>

            <div class="mx-auto w-full max-w-sm lg:w-96">
                <!-- Form Header Logo -->
                <div class="mb-8 flex flex-col items-center">
                    <Link href="/">
                        <img src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-20 w-auto drop-shadow-md" />
                    </Link>
                </div>

                <div class="bg-white px-8 py-8 shadow-lg rounded-2xl border border-gray-100 w-full">
                    <slot />
                </div>

                <p class="mt-6 text-center text-xs text-gray-400">
                    © 2026 National Open University of Nigeria
                </p>
            </div>
        </div>
    </div>
</template>
