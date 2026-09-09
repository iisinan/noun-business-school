<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref, onMounted, onUnmounted } from 'vue';

defineProps({
    canLogin: { type: Boolean },
    canRegister: { type: Boolean },
});

// ── Custom Reveal Directive ───────────────────────────────────────────────────
const vReveal = {
    mounted: (el, binding) => {
        const delay = binding.value || 0;
        el.classList.add('opacity-0', 'translate-y-8', 'transition-all', 'duration-1000', 'ease-out');
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

// ── Navigation state ──────────────────────────────────────────────────────────
const mobileMenuOpen = ref(false);
const scrolled = ref(false);
const showMainLogo = ref(false);
let logoInterval;

function handleScroll() {
    scrolled.value = window.scrollY > 60;
}

onMounted(() => {
    window.addEventListener('scroll', handleScroll);
    logoInterval = setInterval(() => {
        showMainLogo.value = !showMainLogo.value;
    }, 5000);
});

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
    clearInterval(logoInterval);
});

// ── Specialisation accordion state ────────────────────────────────────────────
const openAccordion = ref(null);

function toggleAccordion(id) {
    openAccordion.value = openAccordion.value === id ? null : id;
}

// ── Data ──────────────────────────────────────────────────────────────────────
const navLinks = [
    { label: 'Home',             href: route('home') },
    { label: 'About',            href: route('about') },
    { label: 'Programmes',       href: route('programmes') },
    { label: 'Admissions',       href: '#admissions' },
    { label: 'Media',            href: route('media') },
    { label: 'Resources',        href: route('resources') },
    { label: 'Contact',          href: '#contact' },
];

const mbaTracks = [
    'Digital Business Transformation',
    'FinTech & Financial Innovation',
    'Energy Transition & Sustainability Management',
    'Entrepreneurship & Innovation Management',
    'Agribusiness & Food Systems',
    'Logistics & Supply Chain Management',
    'Procurement Management',
    'Project Management',
    'Peace & Conflict Management',
    'Cyber-Risk & Information Security',
    'Defence & Strategic Studies',
    'Family Business Management',
    'Aviation Management',
    'Migration Studies',
    'Entertainment Economy & Creative Industries',
    'Executive Leadership',
    'Oil & Gas Management',
    'Infrastructure & Utility Regulation',
    'Energy Management',
    'Social Standards',
    'Advertising & Marketing Communications',
    'Advertising & Public Relations',
    'Marketing & Communication',
    'Risk Management & Insurance',
    'Enterprise Risk Management',
    'Capital Markets & Investments',
    'Quantitative Finance',
    'Real Estate Development',
];

const mpaTracks = [
    'Public Policy & Governance Management',
    'Healthcare Administration & HealthTech Management',
];

const dbaTracks = [
    'Digital Business Transformation',
    'FinTech & Financial Innovation',
    'Energy Transition & Sustainability Management',
    'Entrepreneurship & Innovation Management',
    'Agribusiness & Food Systems',
    'Logistics & Supply Chain Management',
    'Procurement Management',
    'Project Management',
    'Peace & Conflict Management',
    'Cyber-Risk & Information Security',
    'Defence & Strategic Studies',
    'Family Business Management',
    'Aviation Management',
    'Migration Studies',
    'Entertainment Economy & Creative Industries',
    'Executive Leadership',
    'Oil & Gas Management',
    'Infrastructure & Utility Regulation',
    'Energy Management',
    'Social Standards',
    'Advertising & Marketing Communications',
    'Advertising & Public Relations',
    'Marketing & Communication',
    'Risk Management & Insurance',
    'Enterprise Risk Management',
    'Capital Markets & Investments',
    'Quantitative Finance',
    'Real Estate Development',
];

const dpaTracks = [
    'Public Policy & Governance Management',
    'Healthcare Administration & HealthTech Management',
];

const programmes = [
    {
        id: 'gdba',
        level: 'Graduate Diploma',
        title: 'Graduate Diploma in Business Administration',
        abbr: 'GDBA',
        duration: '1 Year (2 Semesters)',
        description: 'The structured foundation pathway into postgraduate management study. Designed for graduates of any discipline — including HND holders — who need rigorous grounding in core business fundamentals before specialised study.',
        tracks: null,
        color: 'bg-noun-dark',
    },
    {
        id: 'mba',
        level: "Master's Degree",
        title: 'Master of Business Administration',
        abbr: 'MBA',
        duration: '2 Years (4 Semesters)',
        description: 'A Senate-approved graduate qualification with a common foundational core and 28 MBA specialisation tracks. Combining rigorous academic instruction with applied, practice-based learning via the ODL blended model.',
        tracks: mbaTracks,
        color: 'bg-noun-green',
    },
    {
        id: 'mpa',
        level: "Master's Degree",
        title: 'Master of Public Administration',
        abbr: 'MPA',
        duration: '2 Years (4 Semesters)',
        description: 'Specialist public-sector tracks within the MBA/MPA framework, equipping public servants, policymakers and health administrators with leadership and governance competencies for modern institutions.',
        tracks: mpaTracks,
        color: 'bg-noun-green',
    },
    {
        id: 'dba',
        level: 'Doctoral Degree',
        title: 'Doctor of Business Administration',
        abbr: 'DBA',
        duration: '3 Years (minimum)',
        description: 'A rigorous applied doctorate with 28 DBA specialisation tracks. Culminates in an applied dissertation grounded in real organisational problems, delivered through weekend residencies and a global immersion tour.',
        tracks: dbaTracks,
        color: 'bg-noun-yellow',
    },
    {
        id: 'dpa',
        level: 'Doctoral Degree',
        title: 'Doctor of Public Administration',
        abbr: 'DPA',
        duration: '3 Years (minimum)',
        description: 'The doctoral pathway for senior public sector leaders, combining advanced policy analysis, governance research and practice-oriented dissertation work at the highest level of public management scholarship.',
        tracks: dpaTracks,
        color: 'bg-noun-yellow',
    },
    {
        id: 'exec',
        level: 'Professional Certificate',
        title: 'Executive Certificate Programmes',
        abbr: 'ECP',
        duration: '12 – 16 Weeks',
        description: 'Intensive non-degree programmes for executives and mid-career professionals. Focus areas include Data Analytics, ESG & Sustainability Reporting, and Entrepreneurship & Innovation.',
        tracks: null,
        color: 'bg-gray-700',
    },
];

const whyReasons = [
    {
        icon: 'odl',
        title: 'Flexible Open Distance Learning',
        body: 'Weekend and evening study, intensive residencies, and digital learning platforms — built for working professionals, public servants, and entrepreneurs across Nigeria.',
    },
    {
        icon: 'curriculum',
        title: 'Practice-Ready Curriculum',
        body: 'A deliberate 60:40 ratio of deep domain expertise to applied, technology-enabled learning. Every track culminates in a live capstone project or applied dissertation.',
    },
    {
        icon: 'location',
        title: 'Strategic Abuja Location',
        body: "Headquartered at the seat of Nigeria's Federal Government — within reach of policymakers, the CBN, SEC, over 70 diplomatic missions and multilateral agencies.",
    },
    {
        icon: 'industry',
        title: 'Industry Partnership Consortium',
        body: 'Our curriculum is co-designed with leading practitioners, keeping graduates relevant and employable from day one through live consultancy engagements.',
    },
    {
        icon: 'accreditation',
        title: 'Pathway to International Accreditation',
        body: 'NOUN Business School is on a clear pathway toward international accreditation and pan-African academic partnerships, benchmarking graduates globally.',
    },
];

const admissionSteps = [
    { n: '01', title: 'Choose a Programme',      body: 'Explore our Graduate Diploma, MBA, MPA, DBA, DPA or Executive Certificate programmes and select the track that matches your career goals.' },
    { n: '02', title: 'Create an Account',        body: 'Register on the secure NOUN Business School admission portal to access your personalised application dashboard.' },
    { n: '03', title: 'Complete the Application', body: 'Fill in your personal, academic and professional details and write your Statement of Purpose (500–1,000 words).' },
    { n: '04', title: 'Upload Documents',         body: 'Submit certified transcripts, certificates, CV, two reference letters and a valid means of identification.' },
    { n: '05', title: 'Pay the Application Fee',  body: 'Pay the non-refundable application fee securely via the portal, processed through Remita.' },
    { n: '06', title: 'Submit & Track',           body: 'Submit your completed application before the deadline and monitor your admission status from your dashboard.' },
];

const featuredSpecialisations = [
    'FinTech & Financial Innovation',
    'Digital Business Transformation',
    'Cyber-Risk & Information Security',
    'Energy Transition & Sustainability',
    'Entrepreneurship & Innovation',
    'Healthcare Administration',
    'Oil & Gas Management',
    'Capital Markets & Investments',
    'Public Policy & Governance',
    'Executive Leadership',
    'Agribusiness & Food Systems',
    'Real Estate Development',
];
</script>

<template>
    <Head title="NOUN Business School — Transforming Leaders for the Future of Business" />

    <div id="home" class="min-h-screen bg-white text-gray-900 font-sans antialiased">

        <!-- ═══════════════════════════════════════════
             HEADER / NAVIGATION
        ═══════════════════════════════════════════ -->
        <header
            class="fixed top-0 inset-x-0 z-50 transition-all duration-500"
            :class="scrolled ? 'bg-white/85 backdrop-blur-lg border-b border-gray-200/50 shadow-[0_4px_30px_rgba(0,0,0,0.03)]' : 'bg-transparent'"
        >
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">
                <div class="flex items-center justify-between h-20">

                    <!-- Logo -->
                    <a href="#home" class="flex items-center gap-3 flex-shrink-0 group">
                        <div class="relative h-12 w-[3.5rem] flex-shrink-0 [perspective:1000px]">
                            <transition
                                enter-active-class="transition-all duration-1000 ease-in-out absolute inset-0 [transform-style:preserve-3d]"
                                leave-active-class="transition-all duration-1000 ease-in-out absolute inset-0 [transform-style:preserve-3d]"
                                enter-from-class="[transform:rotateY(-180deg)]"
                                enter-to-class="[transform:rotateY(0deg)]"
                                leave-from-class="[transform:rotateY(0deg)]"
                                leave-to-class="[transform:rotateY(180deg)]"
                            >
                                <img v-if="!showMainLogo" src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-12 w-full object-contain drop-shadow-sm absolute inset-0 [backface-visibility:hidden]" />
                                <img v-else src="/noun-logo.png" alt="NOUN Logo" class="h-12 w-full object-contain drop-shadow-sm absolute inset-0 [backface-visibility:hidden]" />
                            </transition>
                        </div>
                        <div class="leading-tight">
                            <div class="font-bold text-sm tracking-tight text-noun-dark transition-colors duration-300">
                                NOUN Business School
                            </div>
                            <div class="text-xs text-gray-500 transition-colors duration-300">
                                National Open University of Nigeria
                            </div>
                        </div>
                    </a>

                    <nav class="hidden lg:flex items-center gap-7">
                        <template v-for="link in navLinks" :key="link.label">
                            <a
                                v-if="link.href.startsWith('#')"
                                :href="link.href"
                                class="text-sm font-medium text-gray-600 hover:text-noun-green transition-colors duration-200"
                            >{{ link.label }}</a>
                            <Link
                                v-else
                                :href="link.href"
                                class="text-sm font-medium text-gray-600 hover:text-noun-green transition-colors duration-200"
                            >{{ link.label }}</Link>
                        </template>
                    </nav>

                    <!-- Desktop CTA -->
                    <div class="hidden lg:flex items-center gap-3">
                        <Link
                            v-if="$page.props.auth?.user"
                            :href="route('dashboard')"
                            class="text-sm font-medium text-noun-green hover:text-noun-dark transition-colors"
                        >My Dashboard</Link>

                        <template v-else>
                            <Link
                                :href="route('login')"
                                class="text-sm font-medium border rounded-md px-4 py-2 transition-all duration-200 text-noun-dark border-gray-300 hover:border-noun-dark hover:bg-gray-50"
                            >Applicant Login</Link>
                            <Link
                                :href="route('admission.start')"
                                class="text-sm font-semibold bg-noun-green text-white px-5 py-2 rounded-md hover:bg-noun-dark transition-colors shadow-sm"
                            >Apply Now</Link>
                        </template>
                    </div>

                    <!-- Mobile toggle -->
                    <button
                        class="lg:hidden p-2 rounded-md text-noun-dark transition-colors"
                        @click="mobileMenuOpen = !mobileMenuOpen"
                        aria-label="Toggle menu"
                    >
                        <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                        </svg>
                        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                        </svg>
                    </button>
                </div>
            </div>

            <!-- Mobile drawer -->
            <div v-if="mobileMenuOpen" class="lg:hidden bg-white border-t border-gray-100 shadow-xl">
                <div class="px-4 pt-4 pb-6 space-y-1">
                    <template v-for="link in navLinks" :key="link.label">
                        <a
                            v-if="link.href.startsWith('#')"
                            :href="link.href"
                            class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors"
                            @click="mobileMenuOpen = false"
                        >{{ link.label }}</a>
                        <Link
                            v-else
                            :href="link.href"
                            class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors"
                            @click="mobileMenuOpen = false"
                        >{{ link.label }}</Link>
                    </template>
                    <div class="pt-4 border-t border-gray-100 space-y-2 mt-4">
                        <Link
                            :href="route('login')"
                            class="block px-3 py-3 text-center text-noun-dark border border-gray-200 rounded-md text-sm font-medium hover:bg-gray-50 transition-colors"
                            @click="mobileMenuOpen = false"
                        >Applicant Login</Link>
                        <Link
                            :href="route('admission.start')"
                            class="block px-3 py-3 text-center bg-noun-green text-white rounded-md text-sm font-semibold hover:bg-noun-dark transition-colors"
                            @click="mobileMenuOpen = false"
                        >Apply Now</Link>
                    </div>
                </div>
            </div>
        </header>


        <!-- ═══════════════════════════════════════════
             HERO
        ═══════════════════════════════════════════ -->
        <section class="relative pt-36 pb-20 lg:pt-48 lg:pb-32 overflow-hidden bg-gradient-to-br from-white via-white to-noun-light/30">
            <!-- Background image & overlay -->
            <div class="absolute inset-0">
                <img
                    src="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=1920&q=80&auto=format&fit=crop"
                    alt="University campus"
                    class="w-full h-full object-cover object-center opacity-[0.04] mix-blend-multiply"
                />
            </div>
            <div class="absolute inset-0 bg-gradient-to-br from-white/95 via-white/80 to-white/80"></div>
            
            <!-- Glowing Orbs (Ambient Light) -->
            <div class="absolute top-0 left-[-10%] w-[40%] h-[40%] bg-noun-green/10 rounded-full blur-[100px] mix-blend-multiply pointer-events-none"></div>
            <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-noun-yellow/10 rounded-full blur-[100px] mix-blend-multiply pointer-events-none"></div>

            <!-- Premium Background & Accents -->
            <div class="absolute inset-0 bg-[#fbfdfc] overflow-hidden">
                <!-- Massive glow blobs -->
                <div class="absolute top-[-20%] right-[-10%] w-[800px] h-[800px] bg-noun-green/10 rounded-full blur-[120px] mix-blend-multiply pointer-events-none"></div>
                <div class="absolute bottom-[-10%] left-[-20%] w-[600px] h-[600px] bg-noun-yellow/15 rounded-full blur-[100px] mix-blend-multiply pointer-events-none"></div>
                <!-- Subtle grid overlay -->
                <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCI+CjxwYXRoIGQ9Ik0wIDBoNDB2NDBIMHoiIGZpbGw9Im5vbmUiLz4KPHBhdGggZD0iTTAgMTBoNDBNMTAgMHY0ME0wIDIwaDQwTTIwIDB2NDBNMCAzMGg0ME0zMCAwdjQwIiBzdHJva2U9InJnYmEoMCwgNzcsIDAsIDAuMDUpIiBzdHJva2Utd2lkdGg9IjEiLz4KPC9zdmc+')] opacity-60 pointer-events-none"></div>
            </div>

            <div class="relative z-10 w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">
                <div class="lg:grid lg:grid-cols-12 lg:gap-16 lg:items-center">

                    <!-- Text Column -->
                    <div class="lg:col-span-6 xl:col-span-7 pt-12 lg:pt-0">
                        <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full bg-noun-yellow/10 border border-noun-yellow/30 mb-8 animate-fade-in-up opacity-0-init">
                            <span class="relative flex h-3 w-3">
                              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-noun-yellow opacity-75"></span>
                              <span class="relative inline-flex rounded-full h-3 w-3 bg-noun-yellow"></span>
                            </span>
                            <span class="text-noun-dark font-bold text-sm tracking-wide">2026/2027 Admissions Are Now Open</span>
                        </div>

                        <h1 class="text-4xl sm:text-5xl lg:text-6xl xl:text-[4.5rem] font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-noun-dark via-noun-green to-noun-dark leading-[1.1] tracking-tight animate-fade-in-up opacity-0-init animation-delay-100">
                            Transforming<br>
                            <span class="relative inline-block">
                                <span class="relative z-10 text-transparent bg-clip-text bg-gradient-to-r from-noun-yellow to-noun-yellow-light">Leaders</span>
                                <span class="absolute bottom-2 left-0 w-full h-3 bg-noun-yellow/10 -z-10 -skew-x-12"></span>
                            </span> for<br>
                            the Future of <span class="text-gray-400 font-light">Business.</span>
                        </h1>

                        <p class="mt-8 text-lg text-gray-600 max-w-xl leading-relaxed animate-fade-in-up opacity-0-init animation-delay-200">
                            NOUN Business School offers Graduate Diploma, MBA, MPA, DBA, DPA and Executive Certificate programmes through a flexible Open Distance Learning model — rigorous, accessible and purpose-built for Nigeria's working professionals.
                        </p>

                        <div class="mt-8 flex flex-wrap gap-2 animate-fade-in-up opacity-0-init animation-delay-300">
                            <span
                                v-for="badge in ['GDBA', 'MBA', 'MPA', 'DBA', 'DPA', 'Exec Certs']"
                                :key="badge"
                                class="text-xs font-semibold tracking-wider text-noun-dark bg-white border border-gray-200 shadow-sm rounded-full px-4 py-1.5"
                            >{{ badge }}</span>
                        </div>

                        <div class="mt-12 flex flex-wrap gap-4 animate-fade-in-up opacity-0-init animation-delay-400">
                            <Link
                                :href="route('admission.start')"
                                class="relative inline-flex items-center gap-2 px-8 py-4 bg-noun-green text-white font-semibold rounded-lg hover:bg-noun-dark transition-all duration-300 shadow-[0_4px_20px_rgba(0,102,0,0.2)] hover:shadow-[0_4px_30px_rgba(0,102,0,0.3)] hover:-translate-y-1 overflow-hidden group"
                            >
                                <div class="absolute inset-0 w-full h-full bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700 ease-in-out"></div>
                                <span class="relative">Apply Now</span>
                                <svg class="relative w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                                </svg>
                            </Link>
                            <a
                                :href="route('programmes')"
                                class="inline-flex items-center gap-2 px-8 py-4 border border-gray-200 bg-white text-gray-700 font-semibold rounded-lg hover:bg-gray-50 hover:border-gray-300 transition-all duration-300 shadow-sm group hover:-translate-y-0.5"
                            >
                                Explore Programmes
                                <svg class="w-4 h-4 text-gray-400 group-hover:text-noun-dark group-hover:translate-y-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- Dashboard/Bento Feature Composition (No Photos) -->
                    <div class="hidden lg:block lg:col-span-6 xl:col-span-5 relative h-[600px] animate-fade-in-up opacity-0-init animation-delay-500">
                        <!-- Abstract circular accents -->
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[550px] h-[550px] border border-noun-green/10 rounded-full"></div>
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[350px] h-[350px] border border-noun-yellow/30 rounded-full border-dashed animate-[spin_60s_linear_infinite]"></div>

                        <!-- Card 1: 60+ Tracks Data -->
                        <div class="absolute right-0 top-8 w-[380px] bg-white rounded-3xl shadow-[0_30px_60px_rgba(0,0,0,0.08)] border border-gray-100 p-8 z-20 hover:-translate-y-2 transition-transform duration-500">
                            <div class="w-14 h-14 rounded-2xl bg-noun-green/10 text-noun-green flex items-center justify-center mb-6">
                                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                            </div>
                            <h3 class="text-4xl font-extrabold text-noun-dark mb-3">60+ Tracks</h3>
                            <p class="text-gray-500 text-sm leading-relaxed mb-8">The most comprehensive suite of postgraduate business specialisations in West Africa.</p>
                            
                            <!-- Mini abstract bar chart grid -->
                            <div class="grid grid-cols-2 gap-y-5 gap-x-6">
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>GDBA</span>
                                        <span class="text-noun-green">1</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-noun-green w-[15%] rounded-full"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>MBA</span>
                                        <span class="text-noun-green">15</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-noun-green w-[85%] rounded-full"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>MPA</span>
                                        <span class="text-noun-green">15</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-noun-green w-[85%] rounded-full"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>DBA</span>
                                        <span class="text-noun-yellow">15</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-noun-yellow w-[85%] rounded-full"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>DPA</span>
                                        <span class="text-noun-yellow">15</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-noun-yellow w-[85%] rounded-full"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] font-bold text-gray-400 mb-1.5 uppercase tracking-widest">
                                        <span>Exec. Certs</span>
                                        <span class="text-gray-400">Var.</span>
                                    </div>
                                    <div class="h-1.5 w-full bg-gray-100 rounded-full overflow-hidden">
                                        <div class="h-full bg-gray-300 w-[50%] rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Card 2: ODL Feature -->
                        <div class="absolute left-[-2rem] top-[45%] w-[260px] bg-noun-dark rounded-3xl shadow-[0_20px_40px_rgba(0,102,0,0.2)] border border-white/10 p-7 z-30 hover:-translate-y-2 transition-transform duration-500">
                            <div class="flex items-center gap-4 mb-6">
                                <div class="relative flex h-5 w-5">
                                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-noun-yellow opacity-75"></span>
                                  <span class="relative inline-flex rounded-full h-5 w-5 bg-noun-yellow"></span>
                                </div>
                                <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">ODL Model</span>
                            </div>
                            <h4 class="text-white font-semibold text-xl leading-snug">Study from anywhere in the world.</h4>
                        </div>

                        <!-- Card 3: Career Growth -->
                        <div class="absolute right-8 bottom-6 w-[340px] bg-white/80 backdrop-blur-xl rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.06)] border border-white p-6 z-20 hover:-translate-y-2 transition-transform duration-500">
                            <div class="flex justify-between items-center mb-6">
                                <div>
                                    <div class="text-noun-dark font-bold text-lg">Career Trajectory</div>
                                    <div class="text-gray-400 text-xs mt-1">Expected ROI across tracks</div>
                                </div>
                                <div class="w-12 h-12 bg-noun-yellow/10 rounded-full flex items-center justify-center text-noun-yellow font-bold text-sm">
                                    +120%
                                </div>
                            </div>
                            <!-- Mini abstract line chart -->
                            <svg class="w-full h-20 drop-shadow-sm" viewBox="0 0 100 30" preserveAspectRatio="none">
                                <path d="M0,28 L15,25 L30,22 L45,24 L60,15 L75,12 L85,8 L100,2" fill="none" stroke="currentColor" stroke-width="2.5" class="text-noun-green" stroke-linecap="round" stroke-linejoin="round"></path>
                                <path d="M0,28 L15,25 L30,22 L45,24 L60,15 L75,12 L85,8 L100,2 L100,30 L0,30 Z" fill="currentColor" class="text-noun-green/10"></path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Premium Scroll Cue -->
            <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 cursor-pointer group" onclick="document.getElementById('about').scrollIntoView({behavior: 'smooth'})">
                <div class="text-[10px] uppercase tracking-[0.3em] text-noun-dark/40 font-bold group-hover:text-noun-dark transition-colors duration-300">Explore</div>
                <div class="w-6 h-10 border-2 border-noun-dark/20 rounded-full flex justify-center p-1 group-hover:border-noun-dark/40 transition-colors duration-300">
                    <div class="w-1 h-2 bg-noun-yellow rounded-full animate-[bounce_2s_infinite]"></div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════
             ACCREDITATIONS / TRUST BANNER
        ═══════════════════════════════════════════ -->
        <div class="border-y border-gray-100 bg-white py-10 lg:py-14 relative overflow-hidden">
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24 relative z-10">
                <p class="text-center text-xs font-bold tracking-widest text-gray-400 uppercase mb-8">Statutory Approvals & Accreditations</p>
                <div class="flex flex-wrap justify-center items-center gap-10 sm:gap-16 lg:gap-24 opacity-60 grayscale hover:grayscale-0 transition-all duration-700">
                    <div class="flex items-center gap-3 font-serif font-bold text-lg lg:text-xl text-gray-800">
                        <div class="w-10 h-10 rounded-full bg-gray-50 border border-gray-100 flex items-center justify-center text-noun-green">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l9-5-9-5-9 5 9 5z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.121 14.121L19 19m-7-7l7-7m-7 7l-2.879 2.879M12 12L9.121 9.121m0 5.758a3 3 0 10-4.243 4.243 3 3 0 004.243-4.243zm0-5.758a3 3 0 10-4.243-4.243 3 3 0 004.243 4.243z" /></svg>
                        </div>
                        NUC Approved
                    </div>
                    <div class="flex items-center gap-3 font-serif font-bold text-lg lg:text-xl text-gray-800">
                        <div class="w-10 h-10 rounded-full bg-gray-50 border border-gray-100 flex items-center justify-center text-noun-green">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9"/></svg>
                        </div>
                        Fed. Ministry of Education
                    </div>
                    <div class="flex items-center gap-3 font-serif font-bold text-lg lg:text-xl text-gray-800">
                        <div class="w-10 h-10 rounded-full bg-gray-50 border border-gray-100 flex items-center justify-center text-noun-green">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg>
                        </div>
                        World-Class Faculty
                    </div>
                </div>
            </div>
        </div>

        <!-- ═══════════════════════════════════════════
             ABOUT
        ═══════════════════════════════════════════ -->
        <section id="about" class="py-24 lg:py-32 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-white via-white to-noun-light/20 relative overflow-hidden">
            <!-- Decorative background element -->
            <div class="absolute top-0 right-0 w-1/3 h-full bg-gray-50/50 skew-x-12 translate-x-1/2"></div>
            
            <div class="relative z-10 w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">
                <div class="lg:grid lg:grid-cols-2 lg:gap-24 lg:items-center">

                    <!-- Pull quote -->
                    <div class="relative" v-reveal="100">
                        <div class="absolute -top-10 -left-8 text-[10rem] text-noun-yellow/10 font-serif leading-none select-none">"</div>
                        <blockquote class="relative mb-12">
                            <p class="text-2xl lg:text-3xl font-light text-noun-dark leading-snug italic">
                                I invite you to join this pioneering cohort — to help shape the culture, standards and legacy of a Business School that will, in time, be counted among Africa's finest. Welcome to NOUN Business School.
                            </p>
                        </blockquote>

                        <div class="relative mb-16 max-w-md lg:max-w-sm xl:max-w-md mx-auto lg:mx-0 mt-8">
                            <div class="absolute inset-0 bg-noun-green rounded-3xl translate-x-4 translate-y-4 opacity-10"></div>
                            <img src="/vc_pic.png" alt="Prof. Uduma. O. Uduma" class="relative z-10 w-full h-[350px] lg:h-[400px] object-cover object-top rounded-3xl border-4 border-white shadow-xl" />
                            
                            <!-- Floating Badge -->
                            <div class="absolute -bottom-6 -left-4 sm:-left-6 z-20 bg-white p-5 rounded-2xl shadow-xl border border-gray-100 max-w-[280px]">
                                <div class="text-noun-dark font-bold text-lg leading-tight">Prof. Uduma. O. Uduma</div>
                                <div class="text-noun-yellow font-bold text-[10px] sm:text-xs uppercase tracking-wider mt-1.5">Vice Chancellor, NOUN</div>
                            </div>
                        </div>

                        <div class="pt-8 border-t border-gray-100">
                            <div class="flex items-start gap-5">
                                <div class="w-1.5 flex-shrink-0 h-16 bg-gradient-to-b from-noun-yellow to-noun-yellow-light rounded-full mt-1"></div>
                                <div>
                                    <div class="text-xs font-bold text-noun-yellow tracking-widest uppercase mb-2">Our Vision</div>
                                    <p class="text-gray-600 leading-relaxed text-lg">To be a leading centre of flexible, technology-enabled business and management education in Africa, producing globally competitive and nationally committed leaders.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Body text -->
                    <div class="mt-20 lg:mt-0" v-reveal="300">
                        <div class="flex items-center gap-3 mb-6">
                            <div class="h-px w-10 bg-noun-yellow"></div>
                            <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">About the School</span>
                        </div>
                        <h2 class="text-3xl lg:text-4xl xl:text-5xl font-bold text-noun-dark mb-8 leading-[1.15]">
                            Graduate Business Education Built for Nigeria's Working Professionals
                        </h2>
                        <div class="space-y-6 text-gray-600 leading-relaxed text-lg">
                            <p>
                                NOUN Business School is a specialised graduate school of the National Open University of Nigeria, delivering postgraduate management education through a blended Open Distance Learning (ODL) model. Headquartered at University Village, Jabi, Abuja, the School is positioned at the seat of Nigeria's Federal Government — offering unrivalled access to policymakers, regulators, diplomatic missions and a fast-growing technocratic and entrepreneurial class.
                            </p>
                            <p>
                                We exist on the conviction that access and excellence are not competing goals. Our ODL model — combining weekend and evening study, intensive residencies and digital learning platforms — is built for Nigeria's working professionals, public servants, entrepreneurs and mid-career executives for whom a full-time campus programme is not realistic, but for whom rigorous, internationally benchmarked business education is a professional necessity.
                            </p>
                            <p>
                                Every track is designed around a practice-ready curriculum, applied capstone projects, live consultancy engagements and an Industry Partnership Consortium that keeps our curriculum current and our graduates employable from day one.
                            </p>
                        </div>
                        <a
                            :href="route('programmes')"
                            class="inline-flex items-center gap-2 mt-12 text-noun-green font-bold text-lg hover:text-noun-dark transition-colors group"
                        >
                            Explore Our Programmes
                            <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             PROGRAMMES
        ═══════════════════════════════════════════ -->
        <section id="programmes" class="py-24 lg:py-32 bg-gray-50">
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">

                <div class="max-w-2xl mb-16" v-reveal>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="h-px w-8 bg-noun-yellow"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Academic Programmes</span>
                    </div>
                    <h2 class="text-3xl lg:text-4xl xl:text-5xl font-bold text-noun-dark leading-tight">
                        A Suite of Programmes Designed for the Modern Professional
                    </h2>
                    <p class="mt-6 text-gray-600 leading-relaxed text-lg">
                        From a one-year graduate diploma to an applied doctorate, NOUN Business School offers a connected pathway of professional and scholarly growth — delivered entirely through flexible distance learning.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
                    <div
                        v-for="(prog, index) in programmes"
                        :key="prog.id"
                        v-reveal="index * 150"
                        class="bg-white rounded-3xl border border-gray-100 overflow-hidden shadow-[0_4px_20px_rgba(0,0,0,0.03)] hover:shadow-[0_20px_40px_rgba(0,0,0,0.06)] hover:-translate-y-2 transition-all duration-500 flex flex-col group"
                    >
                        <!-- Header -->
                        <div class="px-8 pt-8 pb-6 border-b border-gray-50 bg-gradient-to-b from-gray-50/50 to-white">
                            <div class="flex items-start justify-between gap-4 mb-5">
                                <div
                                    class="flex-shrink-0 w-14 h-14 rounded-2xl flex items-center justify-center font-bold text-sm text-white shadow-inner group-hover:scale-105 transition-transform duration-500"
                                    :class="prog.color"
                                >{{ prog.abbr }}</div>
                                <span class="text-xs font-semibold text-noun-yellow bg-noun-yellow/10 border border-noun-yellow/20 rounded-full px-4 py-1.5 whitespace-nowrap">{{ prog.duration }}</span>
                            </div>
                            <div class="text-[10px] font-bold text-gray-400 tracking-widest uppercase mb-2">{{ prog.level }}</div>
                            <h3 class="text-xl font-bold text-noun-dark leading-snug">{{ prog.title }}</h3>
                        </div>

                        <!-- Body -->
                        <div class="px-8 py-8 flex-1 flex flex-col">
                            <p class="text-gray-600 text-sm leading-relaxed flex-1">{{ prog.description }}</p>

                            <!-- Accordion -->
                            <div v-if="prog.tracks?.length" class="mt-8">
                                <button
                                    @click="toggleAccordion(prog.id)"
                                    class="flex items-center justify-between w-full text-sm font-bold text-noun-green hover:text-noun-dark transition-colors bg-noun-green/5 hover:bg-noun-green/10 rounded-xl px-4 py-3"
                                >
                                    <span>{{ prog.tracks.length }} Specialisation Track{{ prog.tracks.length > 1 ? 's' : '' }}</span>
                                    <svg
                                        class="w-4 h-4 transition-transform duration-300"
                                        :class="openAccordion === prog.id ? 'rotate-180' : ''"
                                        fill="none" stroke="currentColor" viewBox="0 0 24 24"
                                    >
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                                    </svg>
                                </button>

                                <div v-if="openAccordion === prog.id" class="mt-2 p-4 border border-gray-100 rounded-xl bg-gray-50/50">
                                    <ul class="space-y-2 max-h-48 overflow-y-auto pr-2">
                                        <li
                                            v-for="track in prog.tracks"
                                            :key="track"
                                            class="flex items-start gap-2 text-xs font-medium text-gray-600"
                                        >
                                            <svg class="w-3.5 h-3.5 text-noun-yellow mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                                            </svg>
                                            <span>{{ track }}</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>

                            <!-- CTA -->
                            <div class="mt-8 pt-6 border-t border-gray-100">
                                <Link
                                    :href="route('admission.start')"
                                    class="inline-flex items-center justify-center w-full gap-2 text-sm font-bold text-white bg-noun-dark hover:bg-noun-dark py-3 rounded-xl transition-all duration-300 group-hover:shadow-md"
                                >
                                    Apply for This Programme
                                    <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                                    </svg>
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             WHY NOUN BUSINESS SCHOOL
        ═══════════════════════════════════════════ -->
        <section id="why" class="py-24 lg:py-32 bg-[#001a00] relative overflow-hidden">
            <!-- Decorative background glowing orb and grid -->
            <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:24px_24px]"></div>
            <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-64 bg-noun-yellow/10 rounded-[100%] blur-[100px] pointer-events-none"></div>

            <div class="relative z-10 w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">

                <div class="text-center max-w-2xl mx-auto mb-16" v-reveal>
                    <div class="flex items-center justify-center gap-3 mb-4">
                        <div class="h-px w-8 bg-noun-yellow"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">The NOUN Advantage</span>
                        <div class="h-px w-8 bg-noun-yellow"></div>
                    </div>
                    <h2 class="text-3xl lg:text-4xl xl:text-5xl font-bold text-white leading-tight">
                        Why Choose NOUN Business School?
                    </h2>
                    <p class="mt-6 text-white/60 leading-relaxed text-lg">
                        Flexible, accessible and cost-effective graduate business education — without compromising academic rigour or global relevance.
                    </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div
                        v-for="(reason, index) in whyReasons"
                        :key="reason.icon"
                        v-reveal="index * 150"
                        class="group relative bg-white/[0.03] border border-white/10 rounded-3xl p-8 hover:bg-white/[0.06] hover:border-noun-yellow/30 hover:shadow-[0_0_40px_rgba(242,169,0,0.1)] hover:-translate-y-2 transition-all duration-500 overflow-hidden"
                    >
                        <div class="absolute -top-10 -right-10 w-40 h-40 bg-noun-yellow/10 rounded-full blur-2xl group-hover:bg-noun-yellow/20 transition-colors duration-500"></div>
                        <div class="relative z-10">
                            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-noun-yellow/20 to-noun-yellow/5 border border-noun-yellow/30 flex items-center justify-center mb-6 shadow-inner">
                                <svg v-if="reason.icon === 'odl'" class="w-7 h-7 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                </svg>
                                <svg v-else-if="reason.icon === 'curriculum'" class="w-7 h-7 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>
                                </svg>
                                <svg v-else-if="reason.icon === 'location'" class="w-7 h-7 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                                </svg>
                                <svg v-else-if="reason.icon === 'industry'" class="w-7 h-7 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                                </svg>
                                <svg v-else class="w-7 h-7 text-noun-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/>
                                </svg>
                            </div>
                            <h3 class="text-xl font-bold text-white mb-3 group-hover:text-noun-yellow transition-colors duration-300">{{ reason.title }}</h3>
                            <p class="text-white/60 text-sm leading-relaxed">{{ reason.body }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             ADMISSIONS PROCESS
        ═══════════════════════════════════════════ -->
        <section id="admissions" class="py-24 lg:py-32 bg-white relative overflow-hidden">
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24 relative z-10">

                <div class="max-w-2xl mb-20" v-reveal>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="h-px w-8 bg-noun-yellow"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Admissions</span>
                    </div>
                    <h2 class="text-3xl lg:text-4xl xl:text-5xl font-bold text-noun-dark leading-tight">
                        A Seamless Application Process
                    </h2>
                    <p class="mt-6 text-gray-600 leading-relaxed text-lg">
                        Applying to NOUN Business School is straightforward. Complete your application entirely online through our secure portal in six steps.
                    </p>
                </div>

                <!-- Steps timeline -->
                <div class="relative max-w-5xl mx-auto">
                    <!-- Connecting line (desktop) -->
                    <div class="hidden lg:block absolute top-8 left-8 right-8 h-0.5 bg-gray-100 -z-10"></div>
                    
                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-12">
                        <div
                            v-for="(step, index) in admissionSteps"
                            :key="step.n"
                            v-reveal="index * 150"
                            class="relative flex flex-col items-start group"
                        >
                            <div class="w-16 h-16 rounded-2xl bg-white border-2 border-noun-yellow flex flex-col items-center justify-center shadow-[0_4px_20px_rgba(242,169,0,0.15)] mb-6 group-hover:scale-110 group-hover:border-noun-yellow-light transition-transform duration-300">
                                <div class="text-[9px] text-noun-yellow font-bold tracking-widest leading-none mb-1">STEP</div>
                                <div class="text-xl font-bold text-noun-dark leading-none">{{ step.n }}</div>
                            </div>
                            <div>
                                <h3 class="text-lg font-bold text-noun-dark mb-2 group-hover:text-noun-green transition-colors">{{ step.title }}</h3>
                                <p class="text-sm text-gray-600 leading-relaxed">{{ step.body }}</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Requirements note -->
                <div class="mt-24 bg-gradient-to-r from-gray-50 to-white border border-gray-100 rounded-3xl p-8 lg:p-10 lg:flex lg:items-start lg:gap-10 shadow-lg shadow-gray-200/40 relative overflow-hidden" v-reveal>
                    <div class="absolute inset-0 bg-[radial-gradient(#d1d5db_1px,transparent_1px)] [background-size:20px_20px] opacity-20"></div>
                    
                    <div class="flex-shrink-0 mb-6 lg:mb-0 relative z-10">
                        <div class="w-14 h-14 rounded-2xl bg-white border border-noun-green/20 shadow-sm flex items-center justify-center">
                            <svg class="w-7 h-7 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                        </div>
                    </div>
                    <div class="flex-1 relative z-10">
                        <h4 class="text-xl font-bold text-noun-dark mb-5">General Entry Requirements</h4>
                        <ul class="grid grid-cols-1 md:grid-cols-2 gap-y-3 gap-x-12 text-sm text-gray-600">
                            <li v-for="req in [
                                'Five (5) O\'Level credits including English & Maths',
                                'First Degree (any discipline) — GDBA, MBA, MPA',
                                'Master\'s degree for DBA/DPA programmes',
                                'Two (2) professional / academic references',
                                'Statement of Purpose (500–1,000 words)',
                                'Current CV and valid means of identification',
                            ]" :key="req" class="flex items-start gap-3">
                                <svg class="w-5 h-5 text-noun-yellow mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                                </svg>
                                <span class="leading-relaxed">{{ req }}</span>
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- CTA -->
                <div class="mt-16 text-center" v-reveal>
                    <Link
                        :href="route('admission.start')"
                        class="inline-flex items-center gap-3 px-12 py-5 bg-noun-green text-white font-bold text-lg rounded-xl hover:bg-noun-dark transition-all duration-300 shadow-[0_4px_20px_rgba(0,102,0,0.3)] hover:shadow-[0_4px_30px_rgba(0,102,0,0.5)] hover:-translate-y-1 group"
                    >
                        Start Your Application
                        <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                        </svg>
                    </Link>
                    <p class="mt-4 text-sm text-gray-500">
                        Application deadline: <span class="font-semibold text-noun-dark">9 August 2026</span>
                    </p>
                </div>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             FEATURED SPECIALISATIONS
        ═══════════════════════════════════════════ -->
        <section class="py-24 lg:py-32 bg-gradient-to-br from-white via-white to-noun-light/30 relative overflow-hidden">
            <div class="absolute inset-0 bg-[radial-gradient(#d1d5db_1px,transparent_1px)] [background-size:20px_20px] opacity-30"></div>
            
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24 relative z-10">
                <div class="lg:flex lg:items-end lg:justify-between lg:gap-12 mb-16" v-reveal>
                    <div class="max-w-xl">
                        <div class="flex items-center gap-3 mb-4">
                            <div class="h-px w-8 bg-noun-yellow"></div>
                            <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Specialisation Tracks</span>
                        </div>
                        <h2 class="text-3xl lg:text-4xl xl:text-5xl font-bold text-noun-dark leading-tight">
                            60+ Tracks Tailored to Today's Industries
                        </h2>
                    </div>
                    <a
                        :href="route('programmes')"
                        class="hidden lg:inline-flex items-center gap-2 text-noun-green font-bold text-lg hover:text-noun-dark transition-colors group flex-shrink-0"
                    >
                        View All Specialisations
                        <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                        </svg>
                    </a>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                    <div
                        v-for="(spec, index) in featuredSpecialisations"
                        :key="spec"
                        v-reveal="index * 50"
                        class="group relative bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
                    >
                        <div class="absolute inset-0 bg-gradient-to-br from-noun-yellow/0 to-noun-yellow/0 group-hover:from-noun-yellow/[0.03] group-hover:to-transparent rounded-2xl transition-colors duration-500"></div>
                        <div class="relative z-10 flex flex-col h-full justify-between">
                            <div class="w-8 h-1 bg-gradient-to-r from-noun-yellow to-noun-yellow-light rounded-full mb-4 group-hover:w-12 transition-all duration-300"></div>
                            <div class="text-[15px] font-bold text-noun-dark leading-snug group-hover:text-noun-green transition-colors">{{ spec }}</div>
                        </div>
                    </div>
                </div>

                <div class="mt-12 text-center lg:hidden" v-reveal>
                    <a
                        :href="route('programmes')"
                        class="inline-flex items-center gap-2 text-noun-green font-bold hover:text-noun-dark transition-colors"
                    >
                        View All 60+ Specialisations
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                        </svg>
                    </a>
                </div>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             FINAL CTA BANNER
        ═══════════════════════════════════════════ -->
        <section class="relative py-24 lg:py-32 bg-noun-dark overflow-hidden group">
            <div class="absolute inset-0">
                <img
                    src="https://images.unsplash.com/photo-1562240020-ce31ccb0fa7d?w=1920&q=80&auto=format&fit=crop"
                    alt="Graduation ceremony"
                    class="w-full h-full object-cover opacity-10 group-hover:scale-105 group-hover:opacity-15 transition-all duration-1000 ease-out"
                />
            </div>
            <div class="absolute inset-0 bg-gradient-to-br from-[#001a00] via-[#003300]/95 to-[#004d00]/80"></div>
            
            <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-noun-yellow to-transparent opacity-50"></div>
            <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-noun-yellow to-transparent opacity-50"></div>

            <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center" v-reveal>
                <div class="flex items-center justify-center gap-3 mb-8">
                    <div class="h-px w-8 bg-noun-yellow"></div>
                    <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Begin Your Journey</span>
                    <div class="h-px w-8 bg-noun-yellow"></div>
                </div>

                <h2 class="text-4xl lg:text-5xl xl:text-6xl font-bold text-white leading-tight">
                    Take the Next Step in<br>Your <span class="text-noun-yellow">Professional Journey.</span>
                </h2>

                <p class="mt-8 text-white/70 text-lg lg:text-xl max-w-2xl mx-auto leading-relaxed">
                    Join NOUN Business School's maiden cohort and be part of a pioneering generation of African business and public sector leaders. Applications for the 2026/2027 session are now open.
                </p>

                <div class="mt-12 flex flex-wrap items-center justify-center gap-5">
                    <Link
                        :href="route('admission.start')"
                        class="inline-flex items-center gap-2 px-10 py-4 bg-noun-green text-white font-bold text-lg rounded-xl hover:bg-noun-dark transition-all duration-300 shadow-[0_4px_20px_rgba(0,102,0,0.3)] hover:shadow-[0_4px_30px_rgba(0,102,0,0.5)] hover:-translate-y-1"
                    >
                        Apply Now
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                        </svg>
                    </Link>
                    <a
                        :href="route('programmes')"
                        class="inline-flex items-center gap-2 px-10 py-4 bg-white/5 border border-white/20 text-white font-bold text-lg rounded-xl hover:bg-white/10 hover:border-noun-yellow/50 transition-all duration-300 backdrop-blur-sm"
                    >
                        Explore Programmes
                    </a>
                </div>

                <p class="mt-8 text-white/50 text-sm">
                    Already applied?
                    <Link :href="route('login')" class="text-noun-yellow font-semibold hover:text-noun-yellow-light hover:underline transition-colors ml-1">
                        Log in to your portal →
                    </Link>
                </p>
            </div>
        </section>


        <!-- ═══════════════════════════════════════════
             FOOTER
        ═══════════════════════════════════════════ -->
        <footer id="contact" class="bg-noun-dark border-t border-white/5">
            <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24 py-16 lg:py-24">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8">

                    <!-- Brand -->
                    <div class="lg:col-span-1 lg:pr-8" v-reveal>
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
                        <div class="flex gap-4">
                            <a v-for="social in [
                                { label: 'Twitter/X', path: 'M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.746l7.73-8.835L1.254 2.25H8.08l4.262 5.636L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z' },
                                { label: 'LinkedIn', path: 'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z' },
                                { label: 'Facebook', path: 'M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z' },
                            ]" :key="social.label"
                               href="#"
                               :aria-label="social.label"
                               class="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-white/50 hover:text-white hover:bg-white/10 hover:border-white/20 hover:-translate-y-1 transition-all duration-300"
                            >
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                                    <path :d="social.path"/>
                                </svg>
                            </a>
                        </div>
                    </div>

                    <!-- Quick Links -->
                    <div v-reveal="100">
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Quick Links</h4>
                        <ul class="space-y-3">
                            <li v-for="link in [
                                { label: 'About the School', href: route('about') },
                                { label: 'Our Programmes', href: route('programmes') },
                                { label: 'Admissions', href: '#admissions' },
                                { label: 'Media', href: route('media') },
                                { label: 'Resources', href: route('resources') },
                                { label: 'Careers', href: route('career') },
                            ]" :key="link.label">
                                <a v-if="link.href.startsWith('#')" :href="link.href" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ link.label }}</a>
                                <Link v-else :href="link.href" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ link.label }}</Link>
                            </li>
                        </ul>
                    </div>

                    <!-- Programmes -->
                    <div v-reveal="200">
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Programmes</h4>
                        <ul class="space-y-3">
                            <li v-for="p in [
                                'Graduate Diploma (GDBA)',
                                'MBA — 28 Tracks',
                                'MPA — 2 Tracks',
                                'DBA — 28 Tracks',
                                'DPA — 2 Tracks',
                                'Executive Certificates',
                            ]" :key="p">
                                <a :href="route('programmes')" class="text-white/60 hover:text-noun-yellow text-sm transition-colors">{{ p }}</a>
                            </li>
                        </ul>
                    </div>

                    <!-- Contact -->
                    <div v-reveal="300">
                        <h4 class="text-white font-bold text-sm mb-6 tracking-wide">Contact</h4>
                        <ul class="space-y-4 text-sm text-white/60">
                            <li class="flex items-start gap-3">
                                <svg class="w-4 h-4 text-noun-yellow mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                                </svg>
                                <span>NOUN Headquarters, University Village, Nnamdi Azikiwe Expressway, Jabi, Abuja, FCT, Nigeria</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-4 h-4 text-noun-yellow mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9"/>
                                </svg>
                                <a href="https://www.noun.edu.ng" target="_blank" rel="noopener" class="hover:text-noun-yellow transition-colors">www.noun.edu.ng</a>
                            </li>
                        </ul>
                        <div class="mt-8">
                            <Link
                                :href="route('admission.start')"
                                class="inline-flex items-center gap-2 text-sm font-bold bg-white/5 border border-white/10 text-white px-6 py-3 rounded-xl hover:bg-noun-green hover:border-noun-green transition-all duration-300"
                            >Apply Now</Link>
                        </div>
                    </div>
                </div>

                <!-- Bottom bar -->
                <div class="mt-20 pt-8 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-6" v-reveal="400">
                    <p class="text-white/40 text-sm">
                        &copy; 2026 NOUN Business School, National Open University of Nigeria. All rights reserved.
                    </p>
                    <div class="flex gap-6 text-sm text-white/40 font-medium">
                        <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                        <a href="#" class="hover:text-white transition-colors">Terms of Use</a>
                        <a href="#" class="hover:text-white transition-colors">Accessibility</a>
                    </div>
                </div>
            </div>
        </footer>

    </div>
</template>

<style scoped>
/* Smooth scroll */
:global(html) {
    scroll-behavior: smooth;
}

/* Thin accent scrollbar for specialisation lists */
ul::-webkit-scrollbar {
    width: 3px;
}
ul::-webkit-scrollbar-track {
    background: transparent;
}
ul::-webkit-scrollbar-thumb {
    background: rgba(201, 152, 42, 0.35);
    border-radius: 2px;
}

/* Custom animations for Hero */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
    animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
.animation-delay-100 { animation-delay: 100ms; }
.animation-delay-200 { animation-delay: 200ms; }
.animation-delay-300 { animation-delay: 300ms; }
.animation-delay-400 { animation-delay: 400ms; }
.animation-delay-500 { animation-delay: 500ms; }
.opacity-0-init { opacity: 0; }
</style>