<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref, onMounted, onUnmounted } from 'vue';
import { courseDetails } from '../data/courseDetails.js';

const mobileMenuOpen = ref(false);
const scrolled = ref(false);

function handleScroll() { scrolled.value = window.scrollY > 60; }
onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));

const navLinks = [
    { label: 'Home',       href: '/' },
    { label: 'About',      href: route('about') },
    { label: 'Programmes', href: route('programmes') },
    { label: 'Admissions', href: '/#admissions' },
    { label: 'Media',      href: route('media') },
    { label: 'Resources',  href: route('resources') },
    { label: 'Careers',    href: route('career') },
    { label: 'Contact',    href: '/#contact' },
];

const vReveal = {
    mounted: (el, binding) => {
        const delay = binding.value || 0;
        el.classList.add('opacity-0', 'translate-y-8', 'transition-all', 'duration-1000', 'ease-out');
        if (delay) el.style.transitionDelay = `${delay}ms`;
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    el.classList.remove('opacity-0', 'translate-y-8');
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
        
        observer.observe(el);
    }
};

const activeTab = ref('mba');
const selectedCourse = ref(null);
const activeDetailTab = ref('philosophy');

function openCourse(track) {
    selectedCourse.value = courseDetails[track.id] || null;
    activeDetailTab.value = 'philosophy';
}

function closeCourse() {
    selectedCourse.value = null;
}

const programmes = {
    gdp: [],
    mpa: [],
    dpa: [],
    mba: [],
    dba: []
};

Object.values(courseDetails).forEach(course => {
    const track = {
        title: course.shortTitle || course.title,
        code: course.id.toUpperCase(),
        id: course.id
    };
    
    if (course.type === 'GDBA') programmes.gdp.push(track);
    else if (course.type === 'MPA') programmes.mpa.push(track);
    else if (course.type === 'DPA') programmes.dpa.push(track);
    else if (course.type === 'MBA') programmes.mba.push(track);
    else if (course.type === 'DBA') programmes.dba.push(track);
});

// Degree definitions for the sidebar v-for
const degrees = [
    {
        key: 'gdp',
        abbr: 'GDBA',
        label: 'Graduate Diploma',
        icon: 'M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z',
    },
    {
        key: 'mpa',
        abbr: 'MPA',
        label: 'Master of Public Admin.',
        icon: 'M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4',
    },
    {
        key: 'mba',
        abbr: 'MBA',
        label: 'Master of Business Admin.',
        icon: 'M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z',
    },
    {
        key: 'dpa',
        abbr: 'DPA',
        label: 'Doctor of Public Admin.',
        icon: 'M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z',
    },
    {
        key: 'dba',
        abbr: 'DBA',
        label: 'Doctor of Business Admin.',
        icon: 'M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z',
    },
];
</script>


<template>
    <Head title="Programmes — NOUN Business School" />
    <div class="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">

        <!-- HEADER -->
        <header
            class="fixed top-0 inset-x-0 z-50 transition-all duration-500"
            :class="scrolled ? 'bg-white/90 backdrop-blur-lg border-b border-gray-200/60 shadow-sm' : 'bg-white border-b border-gray-200'"
        >
            <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-20">
                    <Link :href="route('home')" class="flex items-center gap-3 flex-shrink-0">
                        <img src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-12 w-auto object-contain drop-shadow-sm" />
                        <div class="leading-tight">
                            <div class="font-bold text-sm tracking-tight text-noun-dark">NOUN Business School</div>
                            <div class="text-xs text-gray-500">National Open University</div>
                        </div>
                    </Link>

                    <nav class="hidden lg:flex items-center gap-7">
                        <template v-for="link in navLinks" :key="link.label">
                            <a v-if="link.href.startsWith('#') || link.href.startsWith('/#')" :href="link.href" class="text-sm font-medium text-gray-600 hover:text-noun-green transition-colors">{{ link.label }}</a>
                            <Link v-else :href="link.href" class="text-sm font-medium text-gray-600 hover:text-noun-green transition-colors">{{ link.label }}</Link>
                        </template>
                    </nav>

                    <div class="hidden lg:flex items-center gap-3">
                        <Link v-if="$page.props.auth?.user" :href="route('dashboard')" class="text-sm font-medium text-noun-green hover:text-noun-dark transition-colors">My Dashboard</Link>
                        <template v-else>
                            <Link :href="route('login')" class="text-sm font-medium border border-gray-300 text-noun-dark px-5 py-2.5 rounded-full hover:border-noun-dark hover:bg-gray-50 transition-all">Applicant Login</Link>
                            <Link :href="route('admission.start')" class="text-sm font-bold bg-noun-green text-white px-5 py-2.5 rounded-full hover:bg-noun-dark transition shadow-lg shadow-noun-green/20">Apply Now</Link>
                        </template>
                    </div>

                    <button class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-gray-100" @click="mobileMenuOpen = !mobileMenuOpen" aria-label="Toggle menu">
                        <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
                        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>
            </div>

            <!-- Mobile drawer -->
            <div v-if="mobileMenuOpen" class="lg:hidden bg-white border-t border-gray-100 shadow-xl">
                <div class="px-4 pt-4 pb-6 space-y-1">
                    <template v-for="link in navLinks" :key="link.label">
                        <a v-if="link.href.startsWith('#') || link.href.startsWith('/#')" :href="link.href" class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-lg text-sm font-medium transition-colors" @click="mobileMenuOpen = false">{{ link.label }}</a>
                        <Link v-else :href="link.href" class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-lg text-sm font-medium transition-colors" @click="mobileMenuOpen = false">{{ link.label }}</Link>
                    </template>
                    <div class="pt-4 border-t border-gray-100 space-y-2 mt-4">
                        <Link :href="route('login')" class="block px-3 py-3 text-center text-noun-dark border border-gray-200 rounded-full text-sm font-medium hover:bg-gray-50 transition-colors" @click="mobileMenuOpen = false">Applicant Login</Link>
                        <Link :href="route('admission.start')" class="block px-3 py-3 text-center bg-noun-green text-white rounded-full text-sm font-bold hover:bg-noun-dark transition-colors" @click="mobileMenuOpen = false">Apply Now</Link>
                    </div>
                </div>
            </div>
        </header>

        <!-- MAIN CONTENT -->
        <main class="flex-grow pt-20 bg-white lg:flex lg:flex-col lg:h-screen lg:overflow-hidden">


            <!-- Page Banner -->
            <div class="bg-noun-dark relative overflow-hidden lg:flex-shrink-0">
                <!-- Decorative blobs -->
                <div class="absolute -top-[30%] -right-[5%] w-[600px] h-[600px] bg-noun-green/15 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-0 left-[5%] w-[400px] h-[400px] bg-noun-yellow/5 rounded-full blur-[100px] pointer-events-none"></div>
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff06_1px,transparent_1px),linear-gradient(to_bottom,#ffffff06_1px,transparent_1px)] bg-[size:40px_40px]"></div>

                <div class="relative z-10 w-full mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-14 flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
                    <div class="max-w-2xl">
                        <div class="inline-flex items-center gap-2 bg-noun-green/20 border border-noun-green/30 text-noun-yellow text-xs font-bold uppercase tracking-widest px-3 py-1.5 rounded-full mb-5">
                            <span class="w-1.5 h-1.5 rounded-full bg-noun-yellow animate-pulse"></span>
                            Academic Catalogue
                        </div>
                        <h1 class="text-3xl lg:text-4xl xl:text-5xl font-black text-white leading-tight mb-3">
                            Our Programmes &amp; <span class="text-noun-yellow">Specialisations</span>
                        </h1>
                        <p class="text-white/60 text-base max-w-xl">
                            Over 60 specialisation tracks across 5 degree types — all delivered through Open Distance Learning.
                        </p>
                    </div>
                    <div class="flex gap-4 flex-shrink-0">
                        <div class="bg-white/10 border border-white/10 rounded-2xl px-6 py-5 text-center backdrop-blur-sm">
                            <div class="text-3xl font-black text-noun-yellow">60+</div>
                            <div class="text-white/50 text-xs mt-1 uppercase tracking-wider font-semibold">Specialisations</div>
                        </div>
                        <div class="bg-white/10 border border-white/10 rounded-2xl px-6 py-5 text-center backdrop-blur-sm">
                            <div class="text-3xl font-black text-noun-yellow">5</div>
                            <div class="text-white/50 text-xs mt-1 uppercase tracking-wider font-semibold">Degree Types</div>
                        </div>
                        <div class="hidden sm:block bg-white/10 border border-white/10 rounded-2xl px-6 py-5 text-center backdrop-blur-sm">
                            <div class="text-3xl font-black text-noun-yellow">100%</div>
                            <div class="text-white/50 text-xs mt-1 uppercase tracking-wider font-semibold">Online (ODL)</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Programmes Directory -->
            <section id="programmes-directory" class="py-16 lg:py-0 relative bg-gray-50/80 lg:flex-grow lg:flex lg:flex-col lg:overflow-hidden w-full">
                
                <!-- Decorative Background -->
                <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                    <div class="absolute -top-[30%] -right-[10%] w-[1000px] h-[1000px] bg-noun-green/5 rounded-full blur-[120px]"></div>
                    <div class="absolute top-[40%] -left-[10%] w-[800px] h-[800px] bg-noun-yellow/5 rounded-full blur-[100px]"></div>
                    <div class="absolute -bottom-[20%] right-[20%] w-[600px] h-[600px] bg-noun-green/5 rounded-full blur-[100px]"></div>
                    <div class="absolute inset-0 opacity-[0.4]" style="background-image: radial-gradient(rgba(0, 77, 0, 0.15) 1.5px, transparent 1.5px); background-size: 32px 32px;"></div>
                </div>

                <div class="w-full mx-auto px-2 sm:px-4 lg:px-6 lg:h-full lg:flex lg:flex-col lg:overflow-hidden lg:py-10 relative z-10">
                    
                    <div class="flex flex-col lg:flex-row gap-10 lg:flex-grow lg:overflow-hidden">

                        
                        <!-- Sidebar Navigation -->
                        <div class="w-full lg:w-72 flex-shrink-0 lg:h-full lg:overflow-y-auto lg:pb-10 hide-scrollbar">

                            <!-- Mobile: horizontal pill scroller -->
                            <div class="flex lg:hidden gap-2 overflow-x-auto pb-3 hide-scrollbar mb-6">
                                <button v-for="deg in degrees" :key="deg.key"
                                    @click="activeTab = deg.key"
                                    :class="activeTab === deg.key ? 'bg-noun-green text-white shadow-lg shadow-noun-green/25' : 'bg-white text-gray-600 border border-gray-200'"
                                    class="flex-shrink-0 flex items-center gap-1.5 px-4 py-2 rounded-full text-xs font-bold transition-all duration-200"
                                >
                                    <span>{{ deg.abbr }}</span>
                                    <span :class="activeTab === deg.key ? 'bg-white/30 text-white' : 'bg-gray-100 text-gray-500'" class="text-[10px] font-black px-1.5 py-0.5 rounded-full">{{ programmes[deg.key].length }}</span>
                                </button>
                            </div>

                            <!-- Desktop: full sidebar card -->
                            <div class="hidden lg:block bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100">
                                <!-- Sidebar header -->
                                <div class="relative bg-noun-dark px-6 py-5 overflow-hidden">
                                    <div class="absolute -top-8 -right-8 w-28 h-28 bg-noun-green/20 rounded-full blur-2xl"></div>
                                    <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-noun-green/40 to-transparent"></div>
                                    <p class="text-noun-yellow text-[10px] font-black uppercase tracking-widest mb-1">Academic Catalogue</p>
                                    <h3 class="text-white font-black text-sm leading-tight">Select a Degree Programme</h3>
                                </div>

                                <!-- Degree buttons -->
                                <div class="p-3 flex flex-col gap-1">
                                    <button v-for="deg in degrees" :key="deg.key"
                                        @click="activeTab = deg.key"
                                        :class="activeTab === deg.key ? 'bg-noun-green/10 border-noun-green/25 text-noun-green' : 'border-transparent text-gray-600 hover:bg-gray-50'"
                                        class="w-full flex items-center gap-3 px-4 py-3.5 rounded-2xl text-left transition-all duration-200 border group"
                                    >
                                        <div :class="activeTab === deg.key ? 'bg-noun-green text-white' : 'bg-gray-100 text-gray-400 group-hover:bg-gray-200'"
                                            class="w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 transition-colors">
                                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="deg.icon"/>
                                            </svg>
                                        </div>
                                        <div class="flex-grow min-w-0">
                                            <div class="font-bold text-sm leading-tight truncate">{{ deg.label }}</div>
                                            <div class="text-[11px] mt-0.5 truncate" :class="activeTab === deg.key ? 'text-noun-green/70' : 'text-gray-400'">{{ deg.abbr }}{{ programmes[deg.key].length > 1 ? ' · ' + programmes[deg.key].length + ' tracks' : '' }}</div>
                                        </div>
                                        <span class="text-[11px] font-black px-2 py-1 rounded-lg flex-shrink-0 transition-colors"
                                            :class="activeTab === deg.key ? 'bg-noun-green text-white' : 'bg-gray-100 text-gray-500'">
                                            {{ programmes[deg.key].length }}
                                        </span>
                                    </button>
                                </div>

                                <!-- Apply CTA -->
                                <div class="p-4 border-t border-gray-100 space-y-2">
                                    <Link :href="route('admission.start')" class="w-full flex items-center justify-center gap-2 bg-noun-green text-white font-bold text-sm py-3.5 rounded-2xl hover:bg-noun-dark transition-all duration-300 shadow-md shadow-noun-green/25 hover:shadow-lg hover:-translate-y-0.5">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                                        Apply Now
                                    </Link>
                                    <Link :href="route('resources')" class="w-full flex items-center justify-center gap-2 text-noun-dark font-semibold text-sm py-3 rounded-2xl hover:bg-gray-50 transition-all duration-200 border border-gray-200 hover:border-gray-300">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                        Download Brochure
                                    </Link>
                                </div>
                            </div>
                        </div>


                        <!-- Track Cards Grid -->
                        <div class="flex-grow min-w-0 lg:h-full lg:overflow-y-auto lg:pr-4 lg:pb-20 hide-scrollbar">

                            <!-- Section header -->
                            <div class="flex items-start justify-between mb-8 flex-wrap gap-4">
                                <div>
                                    <div class="flex items-center gap-2 mb-2">
                                        <div class="w-1.5 h-5 bg-noun-green rounded-full"></div>
                                        <span class="text-xs font-black uppercase tracking-widest text-noun-green">
                                            {{ { gdp: 'GDBA', mpa: 'MPA', mba: 'MBA', dpa: 'DPA', dba: 'DBA' }[activeTab] }}
                                        </span>
                                    </div>
                                    <h2 class="text-xl sm:text-2xl font-black text-noun-dark leading-tight">
                                        <span v-if="activeTab === 'gdp'">Graduate Diploma in Business Administration</span>
                                        <span v-if="activeTab === 'mpa'">Master of Public Administration</span>
                                        <span v-if="activeTab === 'mba'">Master of Business Administration</span>
                                        <span v-if="activeTab === 'dpa'">Doctor of Public Administration</span>
                                        <span v-if="activeTab === 'dba'">Doctor of Business Administration</span>
                                    </h2>
                                    <p class="text-gray-400 text-sm mt-1">
                                        <span class="font-bold text-noun-dark">{{ programmes[activeTab].length }}</span>
                                        specialisation{{ programmes[activeTab].length !== 1 ? 's' : '' }} — click any track to explore the full curriculum
                                    </p>
                                </div>
                                <div class="flex items-center gap-2 flex-wrap">
                                    <div class="inline-flex items-center gap-1.5 bg-noun-yellow/10 text-noun-dark text-xs font-bold px-3 py-1.5 rounded-full border border-noun-yellow/20">
                                        <svg class="w-3 h-3 text-noun-yellow" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
                                        NUC Accredited
                                    </div>
                                    <div class="inline-flex items-center gap-1.5 bg-noun-green/10 text-noun-green text-xs font-bold px-3 py-1.5 rounded-full border border-noun-green/20">
                                        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                        100% Online
                                    </div>
                                </div>
                            </div>

                            <!-- Cards Grid -->
                            <div class="grid sm:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-5">
                                <div
                                    v-for="(track, idx) in programmes[activeTab]"
                                    :key="track.code"
                                    @click="openCourse(track)"
                                    class="relative bg-white border border-gray-200 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl hover:shadow-noun-green/10 hover:-translate-y-1 hover:border-noun-green/30 transition-all duration-300 cursor-pointer group flex flex-col"
                                >
                                    <!-- Always-visible top accent bar -->
                                    <div class="h-1.5 w-full bg-gradient-to-r from-noun-dark via-noun-green to-noun-yellow flex-shrink-0"></div>

                                    <!-- Subtle inner glow on hover -->
                                    <div class="absolute inset-0 bg-gradient-to-br from-noun-green/0 to-noun-green/0 group-hover:from-noun-green/[0.03] group-hover:to-transparent transition-all duration-500 pointer-events-none rounded-2xl"></div>

                                    <div class="p-5 flex flex-col flex-grow">
                                        <!-- Header: icon + code badge -->
                                        <div class="flex items-start justify-between mb-4">
                                            <div class="w-11 h-11 rounded-xl bg-noun-green/10 flex items-center justify-center group-hover:bg-noun-green group-hover:scale-105 transition-all duration-300 shadow-sm">
                                                <svg class="w-5 h-5 text-noun-green group-hover:text-white transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
                                                </svg>
                                            </div>
                                            <span class="text-[10px] font-black tracking-widest text-white bg-noun-dark group-hover:bg-noun-green px-2.5 py-1 rounded-lg uppercase transition-colors duration-300">{{ track.code }}</span>
                                        </div>

                                        <!-- Title -->
                                        <h4 class="font-black text-gray-900 text-sm leading-snug mb-4 group-hover:text-noun-green transition-colors duration-300 flex-grow">{{ track.title }}</h4>

                                        <!-- Pills -->
                                        <div class="flex flex-wrap gap-1.5 mb-5">
                                            <span class="inline-flex items-center gap-1 text-[10px] font-semibold text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                                                <svg class="w-2.5 h-2.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
                                                ODL Online
                                            </span>
                                            <span class="inline-flex items-center gap-1 text-[10px] font-semibold text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                                                <svg class="w-2.5 h-2.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                                18–24 Months
                                            </span>
                                        </div>

                                        <!-- CTA Button -->
                                        <div class="mt-auto pt-4 border-t border-gray-100">
                                            <div class="w-full flex items-center justify-center gap-2 bg-gray-50 group-hover:bg-noun-green text-gray-500 group-hover:text-white text-xs font-bold py-2.5 rounded-xl transition-all duration-300">
                                                View Programme
                                                <svg class="w-3.5 h-3.5 transform group-hover:translate-x-0.5 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </section>


            <!-- Course Detail Slide-over Modal -->
            <Transition name="slide-over">
                <div v-if="selectedCourse" class="fixed inset-0 z-[100] flex justify-end" @click.self="closeCourse">
                    <!-- Backdrop -->
                    <div class="absolute inset-0 bg-noun-dark/40 backdrop-blur-sm" @click="closeCourse"></div>

                    <!-- Panel -->
                    <div class="relative w-full max-w-2xl bg-white h-full flex flex-col shadow-[0_0_60px_rgba(0,0,0,0.25)] overflow-hidden">
                        
                        <!-- Panel Header -->
                        <div class="bg-gradient-to-r from-noun-dark to-noun-green px-8 py-7 flex-shrink-0">
                            <div class="flex items-start justify-between gap-4">
                                <div>
                                    <div class="text-noun-yellow text-xs font-bold tracking-widest uppercase mb-2">{{ selectedCourse.type }} Programme</div>
                                    <h2 class="text-white text-xl font-extrabold leading-tight">{{ selectedCourse.title }}</h2>
                                    <p class="text-white/70 text-sm mt-2 leading-relaxed" v-if="selectedCourse.description">{{ selectedCourse.description }}</p>
                                </div>
                                <button @click="closeCourse" class="flex-shrink-0 w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center transition-colors text-white mt-1">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                                </button>
                            </div>

                            <!-- Tab navigation -->
                            <div class="flex gap-1 mt-6 overflow-x-auto pb-1">
                                <button v-for="tab in [
                                    { key: 'philosophy', label: 'Philosophy' },
                                    { key: 'career', label: 'Career Outcomes' },
                                    { key: 'admission', label: 'Admission' },
                                    { key: 'structure', label: 'Programme Structure' },
                                    { key: 'capstone', label: 'Capstone' },
                                    { key: 'graduation', label: 'Graduation' },
                                ]" :key="tab.key"
                                    @click="activeDetailTab = tab.key"
                                    :class="activeDetailTab === tab.key 
                                        ? 'bg-white text-noun-dark' 
                                        : 'text-white/70 hover:text-white hover:bg-white/10'"
                                    class="flex-shrink-0 text-xs font-bold px-4 py-2 rounded-lg transition-all duration-200">
                                    {{ tab.label }}
                                </button>
                            </div>
                        </div>

                        <!-- Panel Body -->
                        <div class="flex-grow overflow-y-auto p-8">
                            
                            <!-- Philosophy & Objectives -->
                            <div v-if="activeDetailTab === 'philosophy'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-noun-green/10 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                                    </div>
                                    Philosophy &amp; Objectives
                                </h3>
                                <ul class="space-y-4">
                                    <li v-for="item in selectedCourse.philosophy" :key="item" class="flex gap-3">
                                        <div class="w-5 h-5 rounded-full bg-noun-green/10 flex items-center justify-center flex-shrink-0 mt-0.5">
                                            <div class="w-1.5 h-1.5 rounded-full bg-noun-green"></div>
                                        </div>
                                        <span class="text-gray-700 text-sm leading-relaxed">{{ item }}</span>
                                    </li>
                                </ul>
                                <p v-if="!selectedCourse.philosophy.length" class="text-gray-500 text-sm">Details available in the full course brochure.</p>
                            </div>

                            <!-- Career Outcomes -->
                            <div v-if="activeDetailTab === 'career'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-noun-yellow/10 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                                    </div>
                                    Career Outcomes
                                </h3>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                    <div v-for="outcome in selectedCourse.careerOutcomes" :key="outcome"
                                        class="flex items-center gap-3 bg-gray-50 border border-gray-100 rounded-xl px-4 py-3">
                                        <svg class="w-4 h-4 text-noun-green flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg>
                                        <span class="text-sm font-semibold text-noun-dark">{{ outcome }}</span>
                                    </div>
                                </div>
                                <p v-if="!selectedCourse.careerOutcomes.length" class="text-gray-500 text-sm">Details available in the full course brochure.</p>
                            </div>

                            <!-- Admission -->
                            <div v-if="activeDetailTab === 'admission'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-blue-50 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                                    </div>
                                    Admission &amp; Entry Requirements
                                </h3>
                                <div class="bg-gray-50 rounded-2xl p-6 border border-gray-100">
                                    <p class="text-gray-700 text-sm leading-relaxed">{{ selectedCourse.admission || 'A Bachelor\'s degree (minimum Second Class Lower) or HND (minimum Lower Credit) from a recognised institution, plus relevant NYSC certificate or exemption letter. GMAT/GRE may be required for select tracks.' }}</p>
                                </div>
                                <div class="mt-4 bg-noun-green/5 border border-noun-green/20 rounded-2xl p-5">
                                    <p class="text-noun-dark text-sm font-semibold mb-1">General Requirements</p>
                                    <p class="text-gray-600 text-sm leading-relaxed">All MBA/MPA candidates must hold a Bachelor's degree (minimum Second Class Lower Division) or HND (minimum Lower Credit) from a recognised institution, plus a minimum of two (2) years post-qualification working experience.</p>
                                </div>
                            </div>

                            <!-- Programme Structure -->
                            <div v-if="activeDetailTab === 'structure'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-purple-50 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                                    </div>
                                    Programme Structure
                                </h3>

                                <div class="space-y-6">
                                    <!-- Semester 1: Foundational Core -->
                                    <div v-if="selectedCourse.type !== 'GDBA'" class="rounded-2xl overflow-hidden border border-gray-200">
                                        <div class="bg-noun-dark px-5 py-3 flex items-center justify-between">
                                            <div>
                                                <p class="text-noun-yellow text-xs font-bold uppercase tracking-wider">Semester 1</p>
                                                <p class="text-white font-bold text-sm mt-0.5">Foundational Core</p>
                                            </div>
                                            <span class="text-white/60 text-xs">All tracks</span>
                                        </div>
                                        <table class="w-full text-sm">
                                            <thead>
                                                <tr class="bg-gray-50 border-b border-gray-100">
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider w-32">Code</th>
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider">Course Title</th>
                                                    <th class="text-center px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider w-16">Units</th>
                                                </tr>
                                            </thead>
                                            <tbody class="divide-y divide-gray-50">
                                                <tr v-for="(row, i) in [
                                                    { code: 'MGT 701', title: 'Management Theory & Practice', units: 3 },
                                                    { code: 'ACC 701', title: 'Financial Accounting for Managers', units: 3 },
                                                    { code: 'QMT 701', title: 'Quantitative Methods for Business', units: 3 },
                                                    { code: 'STR 701', title: 'Strategic Management', units: 3 },
                                                    { code: 'OBH 701', title: 'Organisational Behaviour', units: 3 },
                                                    { code: 'RMS 701', title: 'Research Methods for Business', units: 3 },
                                                ]" :key="row.code" :class="i % 2 === 0 ? 'bg-white' : 'bg-gray-50/50'">
                                                    <td class="px-4 py-3 font-mono text-xs text-noun-green font-bold">{{ row.code }}</td>
                                                    <td class="px-4 py-3 text-gray-700 text-sm">{{ row.title }}</td>
                                                    <td class="px-4 py-3 text-center">
                                                        <span class="text-xs font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full">{{ row.units }}</span>
                                                    </td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-gray-50 border-t border-gray-200">
                                                    <td colspan="2" class="px-4 py-2.5 text-xs font-bold text-gray-500">Total Foundational Credits</td>
                                                    <td class="px-4 py-2.5 text-center"><span class="text-xs font-extrabold text-noun-dark">18</span></td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>

                                    <!-- Semesters 2–3: Specialisation Core (Or All Core for GDBA) -->
                                    <div v-if="selectedCourse.coreCourses && selectedCourse.coreCourses.length" class="rounded-2xl overflow-hidden border border-noun-green/20">
                                        <div class="bg-noun-green px-5 py-3 flex items-center justify-between">
                                            <div>
                                                <p class="text-white/70 text-xs font-bold uppercase tracking-wider">{{ selectedCourse.type === 'GDBA' ? 'Semesters 1-2' : 'Semesters 2–3' }}</p>
                                                <p class="text-white font-bold text-sm mt-0.5">{{ selectedCourse.type === 'GDBA' ? 'All Required Courses' : 'Specialisation Core' }}</p>
                                            </div>
                                            <span class="text-white/70 text-xs">{{ selectedCourse.shortTitle }}</span>
                                        </div>
                                        <table class="w-full text-sm">
                                            <thead>
                                                <tr class="bg-noun-green/5 border-b border-noun-green/10">
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-noun-green/70 uppercase tracking-wider w-36">Code</th>
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-noun-green/70 uppercase tracking-wider">Course Title</th>
                                                    <th class="text-center px-4 py-2.5 text-xs font-bold text-noun-green/70 uppercase tracking-wider w-16">Units</th>
                                                </tr>
                                            </thead>
                                            <tbody class="divide-y divide-gray-50">
                                                <tr v-for="(row, i) in selectedCourse.coreCourses" :key="row.code" :class="i % 2 === 0 ? 'bg-white' : 'bg-noun-green/[0.02]'">
                                                    <td class="px-4 py-3 font-mono text-xs text-noun-green font-bold">{{ row.code }}</td>
                                                    <td class="px-4 py-3 text-gray-700 text-sm">{{ row.title }}</td>
                                                    <td class="px-4 py-3 text-center">
                                                        <span class="text-xs font-bold text-noun-green bg-noun-green/10 px-2 py-0.5 rounded-full">{{ row.units }}</span>
                                                    </td>
                                                </tr>
                                            </tbody>
                                            <tfoot>
                                                <tr class="bg-noun-green/5 border-t border-noun-green/10">
                                                    <td colspan="2" class="px-4 py-2.5 text-xs font-bold text-noun-green/70">{{ selectedCourse.type === 'GDBA' ? 'Total Course Credits' : 'Core Specialisation Credits' }}</td>
                                                    <td class="px-4 py-2.5 text-center">
                                                        <span class="text-xs font-extrabold text-noun-green">{{ selectedCourse.coreCourses.reduce((s, r) => s + r.units, 0) }}</span>
                                                    </td>
                                                </tr>
                                            </tfoot>
                                        </table>
                                    </div>

                                    <!-- Electives -->
                                    <div v-if="selectedCourse.electiveCourses && selectedCourse.electiveCourses.length" class="rounded-2xl overflow-hidden border border-noun-yellow/20">
                                        <div class="bg-noun-yellow/10 px-5 py-3 flex items-center justify-between border-b border-noun-yellow/20">
                                            <div>
                                                <p class="text-noun-yellow text-xs font-bold uppercase tracking-wider">Electives</p>
                                                <p class="text-noun-dark font-bold text-sm mt-0.5">Choose Two of {{ selectedCourse.electiveCourses.length }}</p>
                                            </div>
                                            <span class="text-gray-400 text-xs">6 units</span>
                                        </div>
                                        <table class="w-full text-sm">
                                            <thead>
                                                <tr class="bg-gray-50 border-b border-gray-100">
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider w-36">Code</th>
                                                    <th class="text-left px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider">Course Title</th>
                                                    <th class="text-center px-4 py-2.5 text-xs font-bold text-gray-500 uppercase tracking-wider w-16">Units</th>
                                                </tr>
                                            </thead>
                                            <tbody class="divide-y divide-gray-50">
                                                <tr v-for="(row, i) in selectedCourse.electiveCourses" :key="row.code" :class="i % 2 === 0 ? 'bg-white' : 'bg-yellow-50/30'">
                                                    <td class="px-4 py-3 font-mono text-xs text-amber-600 font-bold">{{ row.code }}</td>
                                                    <td class="px-4 py-3 text-gray-700 text-sm">{{ row.title }}</td>
                                                    <td class="px-4 py-3 text-center">
                                                        <span class="text-xs font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full">{{ row.units }}</span>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>

                                    <!-- Semester 4: Capstone -->
                                    <div v-if="selectedCourse.type !== 'GDBA'" class="rounded-2xl overflow-hidden border border-orange-200">
                                        <div class="bg-orange-50 px-5 py-3 flex items-center justify-between border-b border-orange-100">
                                            <div>
                                                <p class="text-orange-500 text-xs font-bold uppercase tracking-wider">Semester 4</p>
                                                <p class="text-noun-dark font-bold text-sm mt-0.5">Capstone Project</p>
                                            </div>
                                            <span class="text-gray-400 text-xs">6 units</span>
                                        </div>
                                        <table class="w-full text-sm">
                                            <tbody>
                                                <tr class="bg-white">
                                                    <td class="px-4 py-3 font-mono text-xs text-orange-500 font-bold w-36">{{ selectedCourse.type }}-790</td>
                                                    <td class="px-4 py-3 text-gray-700 text-sm">{{ selectedCourse.shortTitle }} Capstone Project</td>
                                                    <td class="px-4 py-3 text-center w-16">
                                                        <span class="text-xs font-bold text-orange-500 bg-orange-50 px-2 py-0.5 rounded-full">6</span>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>

                                    <!-- Total credits summary -->
                                    <div class="flex items-center justify-between bg-noun-dark rounded-xl px-6 py-4 text-white">
                                        <span class="text-sm font-bold">Total Programme Credits</span>
                                        
                                        <div v-if="selectedCourse.type === 'GDBA'" class="flex items-center gap-6 text-center">
                                            <div><div class="text-noun-yellow font-extrabold text-lg">{{ selectedCourse.coreCourses.reduce((s, r) => s + r.units, 0) }}</div><div class="text-white/50 text-[10px]">Courses</div></div>
                                            <div class="text-white/30">=</div>
                                            <div><div class="text-white font-extrabold text-xl">{{ selectedCourse.coreCourses.reduce((s, r) => s + r.units, 0) }}</div><div class="text-white/50 text-[10px]">Total</div></div>
                                        </div>
                                        
                                        <div v-else class="flex items-center gap-6 text-center">
                                            <div><div class="text-noun-yellow font-extrabold text-lg">18</div><div class="text-white/50 text-[10px]">Foundation</div></div>
                                            <div class="text-white/30">+</div>
                                            <div><div class="text-noun-yellow font-extrabold text-lg">{{ selectedCourse.coreCourses ? selectedCourse.coreCourses.reduce((s, r) => s + r.units, 0) : 15 }}</div><div class="text-white/50 text-[10px]">Core</div></div>
                                            <div class="text-white/30">+</div>
                                            <div><div class="text-noun-yellow font-extrabold text-lg">6</div><div class="text-white/50 text-[10px]">Electives</div></div>
                                            <div class="text-white/30">+</div>
                                            <div><div class="text-noun-yellow font-extrabold text-lg">6</div><div class="text-white/50 text-[10px]">Capstone</div></div>
                                            <div class="text-white/30">=</div>
                                            <div><div class="text-white font-extrabold text-xl">{{ 18 + (selectedCourse.coreCourses ? selectedCourse.coreCourses.reduce((s, r) => s + r.units, 0) : 15) + 12 }}</div><div class="text-white/50 text-[10px]">Total</div></div>
                                        </div>
                                    </div>

                                </div>
                            </div>


                            <!-- Capstone Project -->
                            <div v-if="activeDetailTab === 'capstone'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-orange-50 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                                    </div>
                                    Capstone Project
                                </h3>
                                <div class="bg-gradient-to-br from-orange-50 to-white rounded-2xl p-6 border border-orange-100">
                                    <p class="text-gray-700 text-sm leading-relaxed">{{ selectedCourse.capstone || 'A ' + selectedCourse.shortTitle + ' Capstone Project: a live, organisation-based applied consulting project through which candidates demonstrate integrated mastery of the specialisation core, presented and defended before a Faculty/Industry panel.' }}</p>
                                </div>
                                <div class="mt-4 grid grid-cols-3 gap-4">
                                    <div class="bg-gray-50 rounded-xl p-4 text-center border border-gray-100">
                                        <div class="text-noun-green font-extrabold text-xl">6</div>
                                        <div class="text-gray-500 text-xs mt-1">Credit Units</div>
                                    </div>
                                    <div class="bg-gray-50 rounded-xl p-4 text-center border border-gray-100">
                                        <div class="text-noun-green font-extrabold text-xl">1</div>
                                        <div class="text-gray-500 text-xs mt-1">Semester</div>
                                    </div>
                                    <div class="bg-gray-50 rounded-xl p-4 text-center border border-gray-100">
                                        <div class="text-noun-green font-extrabold text-xl">Live</div>
                                        <div class="text-gray-500 text-xs mt-1">Industry Panel</div>
                                    </div>
                                </div>
                            </div>

                            <!-- Graduation Requirements -->
                            <div v-if="activeDetailTab === 'graduation'">
                                <h3 class="text-lg font-extrabold text-noun-dark mb-6 flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-xl bg-noun-green/10 flex items-center justify-center">
                                        <svg class="w-4 h-4 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                                    </div>
                                    Graduation Requirements
                                </h3>
                                <div class="bg-noun-green/5 border border-noun-green/20 rounded-2xl p-5 mb-5">
                                    <p class="text-xs font-bold text-noun-green uppercase tracking-wider mb-3">General MBA Requirements</p>
                                    <ul class="space-y-2 text-sm text-gray-700">
                                        <li class="flex gap-2"><svg class="w-4 h-4 text-noun-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg>Minimum 60 credit units across all four semesters</li>
                                        <li class="flex gap-2"><svg class="w-4 h-4 text-noun-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg>Minimum CGPA of 3.00 on a 5-point scale</li>
                                        <li class="flex gap-2"><svg class="w-4 h-4 text-noun-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg>Successful defence of Capstone Project</li>
                                        <li class="flex gap-2"><svg class="w-4 h-4 text-noun-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4"/></svg>Full clearance of all academic and administrative obligations</li>
                                    </ul>
                                </div>
                                <div v-if="selectedCourse.graduation && selectedCourse.graduation.length" class="bg-gray-50 rounded-2xl p-5 border border-gray-100">
                                    <p class="text-xs font-bold text-noun-dark uppercase tracking-wider mb-3">Track-Specific Notes</p>
                                    <ul class="space-y-2">
                                        <li v-for="req in selectedCourse.graduation" :key="req" class="text-sm text-gray-700 leading-relaxed">{{ req }}</li>
                                    </ul>
                                </div>
                            </div>

                        </div>

                        <!-- Panel Footer -->
                        <div class="flex-shrink-0 border-t border-gray-100 p-6 flex gap-4 bg-white">
                            <Link :href="route('admission.start')" class="flex-1 bg-noun-green text-white text-sm font-bold py-3.5 rounded-xl text-center hover:bg-noun-dark transition-all duration-300 shadow-[0_4px_15px_rgba(0,102,0,0.2)]">
                                Apply for This Programme
                            </Link>
                            <Link :href="route('resources')" class="flex items-center gap-2 border border-gray-200 text-noun-dark text-sm font-semibold px-5 py-3.5 rounded-xl hover:bg-gray-50 transition-all duration-300">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                Brochure
                            </Link>
                        </div>
                    </div>
                </div>
            </Transition>

        </main>


<!-- FOOTER -->
        <footer id="contact" class="bg-[#001a00] border-t border-white/5">
            <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8">
                    <div class="lg:col-span-1 lg:pr-8">
                        <div class="flex items-center gap-3 mb-6">
                            <img src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-14 w-auto object-contain drop-shadow-lg" />
                            <div>
                                <div class="font-bold text-white text-sm tracking-wide">NOUN Business School</div>
                                <div class="text-noun-yellow text-[10px] uppercase tracking-widest mt-0.5">National Open University</div>
                            </div>
                        </div>
                        <p class="text-white/60 text-sm leading-relaxed mb-8">
                            Delivering flexible, rigorous and practice-relevant graduate business education through Open Distance Learning — for professionals across Nigeria and Africa.
                        </p>
                    </div>

                    <div>
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Quick Links</h4>
                        <ul class="space-y-3">
                            <li v-for="link in navLinks.filter(l => !['Home', 'Contact', 'Programmes', 'Admissions'].includes(l.label))" :key="link.label">
                                <Link :href="link.href" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ link.label }}</Link>
                            </li>
                            <li><a href="/#programmes" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">Our Programmes</a></li>
                            <li><a href="/#admissions" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">Admissions</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Programmes</h4>
                        <ul class="space-y-3 text-sm text-white/60">
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">Graduate Diploma (GDBA)</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">MBA — 28 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">MPA — 2 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">DBA — 28 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">DPA — 2 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">Executive Certificates</a></li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Contact</h4>
                        <ul class="space-y-4 text-sm text-white/60">
                            <li class="flex items-start gap-3">
                                <svg class="w-4 h-4 text-noun-yellow flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                                <span>NOUN Headquarters, University Village, Jabi, Abuja, Nigeria</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-4 h-4 text-noun-yellow flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
                                <a href="https://www.noun.edu.ng" target="_blank" class="hover:text-noun-yellow transition-colors">www.noun.edu.ng</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </footer>
    </div>
</template>

<style scoped>
:global(html) {
    scroll-behavior: smooth;
}

.hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
.hide-scrollbar::-webkit-scrollbar {
    display: none;
}

.slide-over-enter-active,
.slide-over-leave-active {
    transition: opacity 0.3s ease;
}
.slide-over-enter-active .relative.w-full,
.slide-over-leave-active .relative.w-full {
    transition: transform 0.35s cubic-bezier(0.32, 0.72, 0, 1);
}
.slide-over-enter-from,
.slide-over-leave-to {
    opacity: 0;
}
.slide-over-enter-from .relative.w-full {
    transform: translateX(100%);
}
.slide-over-leave-to .relative.w-full {
    transform: translateX(100%);
}
</style>
