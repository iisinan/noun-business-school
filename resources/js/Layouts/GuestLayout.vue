<script setup>
import { Link } from '@inertiajs/vue3';
</script>

<template>
    <div class="min-h-screen flex bg-gray-50 font-sans antialiased">

        <!-- LEFT PANEL — desktop only -->
        <div class="hidden lg:flex lg:w-[45%] xl:w-1/2 bg-noun-dark relative overflow-hidden flex-col items-center justify-center">
            <!-- Grid pattern -->
            <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff06_1px,transparent_1px),linear-gradient(to_bottom,#ffffff06_1px,transparent_1px)] bg-[size:40px_40px]"></div>
            <!-- Glow blobs -->
            <div class="absolute -top-32 -left-32 w-96 h-96 bg-noun-green/20 rounded-full blur-[120px]"></div>
            <div class="absolute -bottom-24 -right-24 w-80 h-80 bg-noun-yellow/10 rounded-full blur-[100px]"></div>

            <div class="relative z-10 p-12 text-white max-w-md text-center">
                <Link href="/">
                    <img src="/nbs-logo.png" alt="NOUN Business School" class="h-24 w-auto mx-auto mb-8 drop-shadow-2xl hover:opacity-90 transition" />
                </Link>

                <div class="inline-flex items-center gap-2 bg-noun-green/20 border border-noun-green/30 text-noun-yellow text-[10px] font-black uppercase tracking-widest px-3 py-1.5 rounded-full mb-6">
                    <span class="w-1.5 h-1.5 rounded-full bg-noun-yellow animate-pulse"></span>
                    Applicant Portal
                </div>

                <h1 class="text-3xl xl:text-4xl font-black tracking-tight mb-4 leading-tight">
                    NOUN<br/>Business School
                </h1>
                <div class="w-10 h-1 bg-noun-yellow rounded-full mx-auto mb-5"></div>
                <p class="text-sm text-white/60 leading-relaxed">
                    Portal access for applicants, students, and administrators. Empowering future global leaders through flexible, accessible education.
                </p>

                <div class="mt-10 grid grid-cols-3 gap-4 text-center">
                    <div class="bg-white/5 border border-white/10 rounded-2xl px-3 py-4">
                        <div class="text-2xl font-black text-noun-yellow">98%</div>
                        <div class="text-[10px] text-white/50 mt-1 uppercase tracking-wider">Employment</div>
                    </div>
                    <div class="bg-white/5 border border-white/10 rounded-2xl px-3 py-4">
                        <div class="text-2xl font-black text-noun-yellow">50+</div>
                        <div class="text-[10px] text-white/50 mt-1 uppercase tracking-wider">Partners</div>
                    </div>
                    <div class="bg-white/5 border border-white/10 rounded-2xl px-3 py-4">
                        <div class="text-2xl font-black text-noun-yellow">12k+</div>
                        <div class="text-[10px] text-white/50 mt-1 uppercase tracking-wider">Alumni</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RIGHT PANEL — form -->
        <div class="flex-1 flex flex-col min-h-screen">

            <!-- Mobile top bar (hidden on desktop) -->
            <div class="lg:hidden bg-noun-dark px-5 py-4 flex items-center justify-between flex-shrink-0">
                <Link href="/" class="flex items-center gap-2.5">
                    <img src="/nbs-logo.png" alt="NOUN Business School" class="h-9 w-auto drop-shadow" />
                    <div class="leading-tight">
                        <div class="text-white font-bold text-xs">NOUN Business School</div>
                        <div class="text-white/50 text-[10px]">Applicant Portal</div>
                    </div>
                </Link>
                <Link :href="route('home')" class="flex items-center gap-1 text-white/60 hover:text-white text-xs font-semibold transition">
                    <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                    Home
                </Link>
            </div>

            <!-- Desktop back link -->
            <div class="hidden lg:block px-8 pt-8">
                <Link :href="route('home')" class="inline-flex items-center gap-2 text-sm font-semibold text-gray-500 hover:text-gray-900 transition bg-white px-4 py-2 rounded-full shadow-sm border border-gray-200">
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                    Back to Home
                </Link>
            </div>

            <!-- Form area -->
            <div class="flex-1 flex flex-col justify-center items-center px-4 sm:px-6 py-8 lg:py-10">
                <div class="w-full max-w-sm sm:max-w-md">

                    <!-- Card -->
                    <div class="bg-white rounded-2xl shadow-xl shadow-gray-200/60 border border-gray-100 overflow-hidden">
                        <!-- Card top accent bar -->
                        <div class="h-1.5 w-full bg-gradient-to-r from-noun-dark via-noun-green to-noun-yellow"></div>

                        <div class="px-6 sm:px-8 py-8">
                            <slot />
                        </div>
                    </div>

                    <p class="mt-6 text-center text-xs text-gray-400">
                        © 2026 National Open University of Nigeria
                    </p>
                </div>
            </div>
        </div>

    </div>
</template>
