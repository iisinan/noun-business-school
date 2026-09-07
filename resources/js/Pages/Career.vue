<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref, onMounted, onUnmounted } from 'vue';

defineProps({
    canLogin: { type: Boolean },
});

// ── Reveal directive ──────────────────────────────────────────────────────────
const vReveal = {
    mounted: (el, binding) => {
        const delay = binding.value || 0;
        el.classList.add('opacity-0', 'translate-y-8', 'transition-all', 'duration-700', 'ease-out');
        if (delay) el.style.transitionDelay = `${delay}ms`;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    el.classList.remove('opacity-0', 'translate-y-8');
                    el.classList.add('opacity-100', 'translate-y-0');
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.1 });
        observer.observe(el);
    }
};

const mobileMenuOpen = ref(false);
const scrolled = ref(false);
const activeTab = ref('vacancies');
const openRole = ref(null);

const tabs = [
    { key: 'vacancies',   label: 'Current Vacancies',      count: 2 },
    { key: 'faculty',     label: 'Faculty Opportunities',   count: 1 },
    { key: 'internships', label: 'Internships',             count: 0 },
    { key: 'volunteering',label: 'Volunteering',            count: 0 },
];

const vacancies = {
    vacancies: [
        {
            id: 1,
            title: 'Lecturer / Course Developer — Business Analytics',
            dept: 'Academic & Faculty',
            type: 'Full-Time',
            location: 'Abuja (Hybrid)',
            badge: 'Hot Role',
            description: 'We are seeking an experienced educator to develop and deliver postgraduate-level courses in Business Analytics and Quantitative Methods for our MBA and DBA programmes.',
            responsibilities: [
                'Develop and maintain course materials for online delivery via the LMS.',
                'Facilitate live virtual tutorials and evaluate student performance.',
                'Conduct academic research and publish in peer-reviewed journals.',
                'Participate in curriculum review and programme quality assurance.',
            ],
            requirements: [
                'PhD in Business Analytics, Statistics, or a closely related field.',
                'Minimum 3 years of postgraduate teaching experience.',
                'Familiarity with Open Distance Learning (ODL) principles.',
                'Strong record of academic research or senior industry practice.',
            ],
        },
        {
            id: 2,
            title: 'Student Services & Admissions Officer',
            dept: 'Student Affairs',
            type: 'Full-Time',
            location: 'Abuja',
            badge: null,
            description: 'This role manages the admissions pipeline and ensures an excellent student experience from first inquiry through to enrolment.',
            responsibilities: [
                'Manage and respond to admissions inquiries via email and the student portal.',
                'Review, verify, and process student applications.',
                'Coordinate orientation programmes for new cohorts.',
                'Maintain accurate student records across all systems.',
            ],
            requirements: [
                'Bachelor\'s degree in any discipline.',
                'Minimum 2 years of experience in university administration.',
                'Excellent written and verbal communication skills.',
                'Proficiency in MS Office and student information systems.',
            ],
        },
    ],
    faculty: [
        {
            id: 3,
            title: 'Visiting Lecturer — Strategic Management',
            dept: 'Faculty',
            type: 'Part-Time / Contract',
            location: 'Remote-first',
            badge: null,
            description: 'We welcome experienced practitioners and academics to join our faculty as visiting lecturers for one or two modules per academic session.',
            responsibilities: [
                'Deliver one or two specialist modules per session.',
                'Review and grade student assessments.',
                'Contribute to faculty discussions on curriculum relevance.',
            ],
            requirements: [
                'PhD or equivalent professional qualifications (e.g. FCCA, FCA, FCIB).',
                'At least 5 years of senior professional or academic experience.',
                'Strong communication and digital presentation skills.',
            ],
        },
    ],
    internships: [],
    volunteering: [],
};

const perks = [
    { icon: 'M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z', label: 'Free Postgraduate Study', text: 'Free study for staff and dependants across all NBS programmes.' },
    { icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6', label: 'Remote-First Culture', text: 'Hybrid and fully-remote roles across most departments.' },
    { icon: 'M13 10V3L4 14h7v7l9-11h-7z', label: 'Career Pathways', text: 'Structured development tracks and transparent promotion criteria.' },
    { icon: 'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z', label: 'Health & Wellbeing', text: 'Comprehensive health insurance for staff and immediate family.' },
    { icon: 'M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9', label: 'Pan-African Impact', text: 'Work at the frontier of business education across the continent.' },
    { icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z', label: 'Collaborative Team', text: 'Work alongside leading academics and industry practitioners.' },
];

const form = ref({ name: '', email: '', expertise: '', years: '', availability: '', linkedin: '' });
const formSubmitted = ref(false);
function submitFacultyForm() { formSubmitted.value = true; }

function handleScroll() { scrolled.value = window.scrollY > 60; }
onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));

const navLinks = [
    { label: 'Home',       href: route('home') },
    { label: 'About',      href: route('about') },
    { label: 'Programmes', href: route('programmes') },
    { label: 'Admissions', href: '/#admissions' },
    { label: 'Media',      href: route('media') },
    { label: 'Resources',  href: route('resources') },
    { label: 'Contact',    href: '#contact' },
];
</script>

<template>
    <Head title="Careers — NOUN Business School" />
    <div class="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">

        <!-- ── HEADER ── -->
        <header
            class="fixed top-0 inset-x-0 z-50 transition-all duration-500"
            :class="scrolled ? 'bg-white/90 backdrop-blur-lg border-b border-gray-200/60 shadow-sm' : 'bg-white border-b border-gray-200'"
        >
            <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-20">
                    <Link :href="route('home')" class="flex items-center gap-3 flex-shrink-0">
                        <img src="/nbs-logo.png" alt="NOUN Business School" class="h-12 w-auto object-contain" />
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
                        <Link v-if="canLogin" :href="route('login')" class="ml-2 inline-flex items-center gap-2 bg-noun-green text-white px-5 py-2.5 rounded-full text-sm font-bold hover:bg-noun-dark transition shadow-lg shadow-noun-green/20">
                            Student Portal
                        </Link>
                    </nav>

                    <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-gray-100">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                        </svg>
                    </button>
                </div>

                <div v-if="mobileMenuOpen" class="lg:hidden pb-4 border-t border-gray-100 mt-2 pt-4 space-y-1">
                    <template v-for="link in navLinks" :key="link.label">
                        <a v-if="link.href.startsWith('#') || link.href.startsWith('/#')" :href="link.href" @click="mobileMenuOpen = false" class="block px-3 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">{{ link.label }}</a>
                        <Link v-else :href="link.href" @click="mobileMenuOpen = false" class="block px-3 py-2 text-sm text-gray-700 hover:bg-gray-50 rounded-lg">{{ link.label }}</Link>
                    </template>
                    <Link v-if="canLogin" :href="route('login')" class="block mt-2 px-3 py-2 text-sm font-bold text-noun-green">Student Portal →</Link>
                </div>
            </div>
        </header>

        <main class="flex-grow">

            <!-- ── HERO ── -->
            <section class="relative pt-20 overflow-hidden bg-noun-dark">
                <div class="absolute -top-[20%] -right-[10%] w-[700px] h-[700px] bg-noun-green/10 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-0 left-[10%] w-[500px] h-[500px] bg-noun-yellow/5 rounded-full blur-[100px] pointer-events-none"></div>

                <div class="relative w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto py-24 lg:py-32">
                    <div class="max-w-3xl">
                        <div v-reveal class="inline-flex items-center gap-2 bg-noun-green/20 border border-noun-green/30 text-noun-yellow text-xs font-bold uppercase tracking-widest px-4 py-2 rounded-full mb-8">
                            <span class="w-1.5 h-1.5 rounded-full bg-noun-yellow animate-pulse"></span>
                            We're Hiring
                        </div>
                        <h1 v-reveal="100" class="text-4xl sm:text-5xl lg:text-6xl font-black text-white leading-[1.05] mb-6">
                            Build the Future of<br>
                            <span class="text-noun-yellow">Business Education</span>
                        </h1>
                        <p v-reveal="200" class="text-lg text-white/70 leading-relaxed max-w-2xl mb-10">
                            Join a passionate team delivering transformative graduate education to professionals across Nigeria and Africa — online, at scale, and with real impact.
                        </p>
                        <div v-reveal="300" class="flex flex-wrap gap-4">
                            <a href="#roles" class="inline-flex items-center gap-2 bg-noun-yellow text-noun-dark px-7 py-3.5 rounded-full font-bold text-sm hover:bg-white transition shadow-lg">
                                See Open Roles
                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
                            </a>
                            <a href="#faculty-form" class="inline-flex items-center gap-2 border border-white/30 text-white px-7 py-3.5 rounded-full font-bold text-sm hover:bg-white/10 transition">
                                Join Our Faculty
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Stats strip -->
                <div class="relative border-t border-white/10 bg-black/20 backdrop-blur-sm">
                    <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto">
                        <div class="grid grid-cols-2 lg:grid-cols-4 divide-x divide-white/10">
                            <div v-for="stat in [
                                { value: '3', label: 'Open Positions' },
                                { value: '60+', label: 'Academic Tracks' },
                                { value: '10k+', label: 'Students Served' },
                                { value: 'Remote', label: 'Work Options' },
                            ]" :key="stat.label" class="px-6 py-7 text-center">
                                <div class="text-2xl lg:text-3xl font-black text-noun-yellow mb-1">{{ stat.value }}</div>
                                <div class="text-xs text-white/50 uppercase tracking-widest font-semibold">{{ stat.label }}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ── PERKS ── -->
            <section class="py-20 bg-gray-50 border-b border-gray-200">
                <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto">
                    <div class="text-center mb-14" v-reveal>
                        <span class="text-xs font-bold uppercase tracking-[0.12em] text-noun-green">Why Join Us</span>
                        <h2 class="text-3xl font-black text-noun-dark mt-3">More than just a job</h2>
                        <p class="text-gray-500 mt-3 max-w-xl mx-auto text-sm leading-relaxed">We invest in our people as much as we invest in our students.</p>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                        <div
                            v-for="(perk, i) in perks"
                            :key="perk.label"
                            v-reveal="i * 80"
                            class="bg-white border border-gray-100 rounded-2xl p-6 hover:border-noun-green/30 hover:shadow-md transition-all duration-300 group"
                        >
                            <div class="w-11 h-11 rounded-xl bg-noun-green/10 flex items-center justify-center mb-4 group-hover:bg-noun-green transition-all duration-300">
                                <svg class="w-5 h-5 text-noun-green group-hover:text-white transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="perk.icon"/>
                                </svg>
                            </div>
                            <h3 class="font-bold text-noun-dark text-sm mb-1">{{ perk.label }}</h3>
                            <p class="text-xs text-gray-500 leading-relaxed">{{ perk.text }}</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ── OPEN ROLES ── -->
            <section id="roles" class="py-20 bg-white">
                <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto">

                    <div class="mb-12" v-reveal>
                        <span class="text-xs font-bold uppercase tracking-[0.12em] text-noun-green">Open Positions</span>
                        <h2 class="text-3xl font-black text-noun-dark mt-3">Current Opportunities</h2>
                        <p class="text-gray-500 mt-3 max-w-xl text-sm leading-relaxed">Browse all active openings across our academic, administrative, and operational teams.</p>
                    </div>

                    <!-- Tab Bar -->
                    <div class="flex flex-wrap gap-2 mb-10" v-reveal="100">
                        <button
                            v-for="tab in tabs"
                            :key="tab.key"
                            @click="activeTab = tab.key; openRole = null"
                            class="px-5 py-2.5 rounded-full text-sm font-bold transition-all border"
                            :class="activeTab === tab.key
                                ? 'bg-noun-dark text-white border-noun-dark shadow-md'
                                : 'border-gray-200 text-gray-500 hover:border-gray-300 hover:text-gray-700 bg-white'"
                        >
                            {{ tab.label }}
                            <span
                                class="ml-2 text-[10px] font-bold px-1.5 py-0.5 rounded-full"
                                :class="activeTab === tab.key ? 'bg-white/20 text-white' : 'bg-gray-100 text-gray-500'"
                            >{{ tab.count }}</span>
                        </button>
                    </div>

                    <!-- Vacancy List -->
                    <div v-if="vacancies[activeTab] && vacancies[activeTab].length > 0" class="space-y-4">
                        <div
                            v-for="(role, idx) in vacancies[activeTab]"
                            :key="role.id"
                            v-reveal="idx * 100"
                            class="border border-gray-200 rounded-2xl overflow-hidden hover:border-noun-green/40 hover:shadow-md transition-all duration-300 group"
                        >
                            <!-- Role header -->
                            <button
                                @click="openRole = openRole === role.id ? null : role.id"
                                class="w-full text-left px-6 py-6 flex items-start sm:items-center justify-between gap-4 bg-white group-hover:bg-gray-50/50 transition-colors"
                            >
                                <div class="flex-1">
                                    <div class="flex flex-wrap items-center gap-2 mb-3">
                                        <span class="text-[11px] font-bold uppercase tracking-widest bg-noun-green/10 text-noun-green px-2.5 py-1 rounded-full">{{ role.dept }}</span>
                                        <span class="text-[11px] font-semibold text-gray-500 bg-gray-100 px-2.5 py-1 rounded-full">{{ role.type }}</span>
                                        <span class="text-[11px] font-semibold text-gray-500 bg-gray-100 px-2.5 py-1 rounded-full flex items-center gap-1">
                                            <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                                            {{ role.location }}
                                        </span>
                                        <span v-if="role.badge" class="text-[11px] font-bold bg-noun-yellow text-noun-dark px-2.5 py-1 rounded-full">{{ role.badge }}</span>
                                    </div>
                                    <h3 class="font-bold text-noun-dark text-base sm:text-lg">{{ role.title }}</h3>
                                </div>
                                <div class="flex-shrink-0 w-9 h-9 rounded-full border border-gray-200 flex items-center justify-center transition-all duration-300"
                                    :class="openRole === role.id ? 'bg-noun-green border-noun-green rotate-180' : 'group-hover:border-noun-green/40'">
                                    <svg class="w-4 h-4 transition-colors" :class="openRole === role.id ? 'text-white' : 'text-gray-400'" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
                                </div>
                            </button>

                            <!-- Role detail -->
                            <div v-if="openRole === role.id" class="border-t border-gray-100 px-6 pt-6 pb-8 bg-gray-50/60">
                                <p class="text-sm text-gray-600 leading-relaxed mb-8 max-w-3xl">{{ role.description }}</p>

                                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                                    <div>
                                        <h4 class="text-[11px] font-black uppercase tracking-[0.1em] text-gray-400 mb-4">Key Responsibilities</h4>
                                        <ul class="space-y-3">
                                            <li v-for="r in role.responsibilities" :key="r" class="flex items-start gap-3 text-sm text-gray-700">
                                                <span class="w-5 h-5 rounded-full bg-noun-green/15 flex items-center justify-center flex-shrink-0 mt-0.5">
                                                    <svg class="w-3 h-3 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>
                                                </span>
                                                {{ r }}
                                            </li>
                                        </ul>
                                    </div>
                                    <div>
                                        <h4 class="text-[11px] font-black uppercase tracking-[0.1em] text-gray-400 mb-4">Requirements</h4>
                                        <ul class="space-y-3">
                                            <li v-for="r in role.requirements" :key="r" class="flex items-start gap-3 text-sm text-gray-700">
                                                <span class="w-5 h-5 rounded-full bg-noun-green/15 flex items-center justify-center flex-shrink-0 mt-0.5">
                                                    <svg class="w-3 h-3 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>
                                                </span>
                                                {{ r }}
                                            </li>
                                        </ul>
                                    </div>
                                </div>

                                <a
                                    :href="`mailto:careers@noun.edu.ng?subject=Application: ${role.title}`"
                                    class="inline-flex items-center gap-2 bg-noun-dark text-white px-7 py-3 rounded-full text-sm font-bold hover:bg-noun-green transition shadow-md"
                                >
                                    Apply for This Role
                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Empty state -->
                    <div v-else class="border-2 border-dashed border-gray-200 rounded-2xl px-10 py-20 text-center" v-reveal>
                        <div class="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center mx-auto mb-5">
                            <svg class="w-8 h-8 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        </div>
                        <h4 class="text-xl font-bold text-noun-dark mb-2">No openings right now</h4>
                        <p class="text-sm text-gray-400 max-w-sm mx-auto leading-relaxed">Open roles in this category will be listed here as they become available. Submit a general CV below to stay on our radar.</p>
                    </div>

                </div>
            </section>

            <!-- ── FACULTY FORM ── -->
            <section id="faculty-form" class="py-24 bg-noun-dark relative overflow-hidden">
                <div class="absolute -top-[30%] right-0 w-[600px] h-[600px] bg-noun-green/10 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-0 left-[5%] w-[400px] h-[400px] bg-noun-yellow/5 rounded-full blur-[80px] pointer-events-none"></div>

                <div class="relative w-full 2xl:px-12 px-4 sm:px-6 lg:px-8 max-w-[1200px] mx-auto">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">

                        <!-- Left: Pitch -->
                        <div v-reveal>
                            <span class="text-xs font-bold uppercase tracking-[0.12em] text-noun-yellow mb-4 block">Faculty & Facilitators</span>
                            <h2 class="text-3xl sm:text-4xl font-black text-white leading-tight mb-6">
                                Shape the next generation of business leaders.
                            </h2>
                            <p class="text-white/60 text-base leading-relaxed mb-10">
                                Whether you are a seasoned academic or a senior practitioner with domain expertise, we want to hear from you. Our visiting and associate faculty model lets you contribute on your own terms.
                            </p>

                            <!-- Quote -->
                            <div class="bg-white/5 border border-white/10 rounded-2xl p-6 mb-6">
                                <p class="text-white/80 text-sm leading-relaxed italic mb-4">
                                    "Teaching at NBS is uniquely rewarding. The students are professionals who bring real boardroom experience to every discussion."
                                </p>
                                <div class="flex items-center gap-3">
                                    <div class="w-8 h-8 rounded-full bg-noun-green flex items-center justify-center text-white text-xs font-bold">FK</div>
                                    <div>
                                        <div class="text-xs font-bold text-white">Dr. F. Kabir</div>
                                        <div class="text-xs text-white/40">Visiting Lecturer, Strategic Management</div>
                                    </div>
                                </div>
                            </div>

                            <!-- General CV card -->
                            <div class="border border-white/10 rounded-2xl p-6">
                                <h3 class="text-base font-bold text-white mb-2">Submit a General CV</h3>
                                <p class="text-sm text-white/50 mb-5 leading-relaxed">Not applying to a specific role? Send your CV and we'll keep it on file for future openings.</p>
                                <a
                                    href="mailto:careers@noun.edu.ng?subject=General CV Submission"
                                    class="inline-flex items-center gap-2 bg-white text-noun-dark px-6 py-2.5 rounded-full text-sm font-bold hover:bg-noun-yellow transition"
                                >
                                    Send CV via Email
                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                                </a>
                            </div>
                        </div>

                        <!-- Right: Form -->
                        <div v-reveal="200" class="bg-white rounded-3xl p-8 shadow-2xl">
                            <h3 class="text-xl font-black text-noun-dark mb-1">Apply as Faculty / Facilitator</h3>
                            <p class="text-sm text-gray-400 mb-7">Our academic team reviews all submissions and will be in touch if there's a match.</p>

                            <div v-if="formSubmitted" class="py-12 text-center">
                                <div class="w-16 h-16 rounded-full bg-noun-green/10 flex items-center justify-center mx-auto mb-4">
                                    <svg class="w-8 h-8 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/></svg>
                                </div>
                                <h4 class="font-bold text-noun-dark text-lg mb-2">Application Received!</h4>
                                <p class="text-sm text-gray-400 max-w-xs mx-auto">Thank you! We'll review your submission and reach out if there's an opportunity that fits your profile.</p>
                            </div>

                            <form v-else @submit.prevent="submitFacultyForm" class="space-y-4">
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Full Name</label>
                                        <input v-model="form.name" type="text" required placeholder="Dr. Jane Smith" class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                    </div>
                                    <div>
                                        <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Email Address</label>
                                        <input v-model="form.email" type="email" required placeholder="you@example.com" class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Area of Expertise</label>
                                    <input v-model="form.expertise" type="text" required placeholder="e.g. Corporate Governance, Public Sector Leadership" class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                </div>
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Years of Experience</label>
                                        <input v-model="form.years" type="text" placeholder="e.g. 8+" class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                    </div>
                                    <div>
                                        <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">Availability</label>
                                        <input v-model="form.availability" type="text" placeholder="Weekends / Full-time" class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-bold uppercase tracking-widest text-gray-400 mb-1.5">LinkedIn Profile</label>
                                    <input v-model="form.linkedin" type="url" placeholder="https://linkedin.com/in/..." class="w-full px-4 py-3 border border-gray-200 rounded-xl text-sm text-gray-900 bg-gray-50 focus:bg-white focus:outline-none focus:border-noun-green focus:ring-2 focus:ring-noun-green/20 transition" />
                                </div>
                                <div class="bg-gray-50 border border-dashed border-gray-200 rounded-xl p-4 text-center text-xs text-gray-400">
                                    Send your CV to
                                    <a href="mailto:careers@noun.edu.ng" class="text-noun-green font-semibold hover:underline mx-1">careers@noun.edu.ng</a>
                                    with subject <em>"Faculty Application"</em>
                                </div>
                                <button type="submit" class="w-full bg-noun-dark text-white font-bold py-3.5 rounded-xl hover:bg-noun-green transition text-sm tracking-wide shadow-md">
                                    Submit Application
                                </button>
                            </form>
                        </div>

                    </div>
                </div>
            </section>

        </main>

        <!-- ── FOOTER ── -->
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
                        <p class="text-white/60 text-sm leading-relaxed">
                            Delivering flexible, rigorous and practice-relevant graduate business education through Open Distance Learning — for professionals across Nigeria and Africa.
                        </p>
                    </div>
                    <div>
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Quick Links</h4>
                        <ul class="space-y-3">
                            <li v-for="link in navLinks.filter(l => !['Contact'].includes(l.label))" :key="link.label">
                                <a v-if="link.href.startsWith('#') || link.href.startsWith('/#')" :href="link.href" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ link.label }}</a>
                                <Link v-else :href="link.href" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ link.label }}</Link>
                            </li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Programmes</h4>
                        <ul class="space-y-3 text-sm text-white/60">
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">Graduate Diploma (GDBA)</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">MBA — 28 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">DBA — 28 Tracks</a></li>
                            <li><a href="/#programmes" class="hover:text-noun-yellow transition-colors">MPA / DPA</a></li>
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
                                <svg class="w-4 h-4 text-noun-yellow flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                                <a href="mailto:careers@noun.edu.ng" class="hover:text-noun-yellow transition-colors">careers@noun.edu.ng</a>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-4 h-4 text-noun-yellow flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
                                <a href="https://www.noun.edu.ng" target="_blank" class="hover:text-noun-yellow transition-colors">www.noun.edu.ng</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="mt-16 pt-8 border-t border-white/5 flex flex-col sm:flex-row justify-between items-center gap-4">
                    <p class="text-white/40 text-xs">© {{ new Date().getFullYear() }} NOUN Business School. All rights reserved.</p>
                    <p class="text-white/40 text-xs">National Open University of Nigeria</p>
                </div>
            </div>
        </footer>

    </div>
</template>

<style scoped>
:global(html) { scroll-behavior: smooth; }
</style>
