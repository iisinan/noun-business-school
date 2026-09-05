<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref } from 'vue';


const mobileMenuOpen = ref(false);

const navLinks = [
    { label: 'Home', href: '/' },
    { label: 'About', href: route('about') },
    { label: 'Programmes', href: route('programmes') },
    { label: 'Admissions', href: '/#admissions' },
    { label: 'Media', href: route('media') },
    { label: 'Resources', href: route('resources') },
    { label: 'Contact', href: '/#contact' },
];

const documentResources = ref([
    {
        id: 'brochure',
        title: 'Official Course Brochure (2026/2027)',
        category: 'Admissions',
        description: 'Comprehensive breakdown of all 28 MBA and DBA specialisation tracks, course units, and faculty profiles for the upcoming academic year. This guide contains everything you need to know about our executive programmes.',
        fileSize: '4.2 MB',
        pages: 34,
        updatedAt: 'August 2026',
        previewImage: 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=800&q=80',
        downloadUrl: '/NOUN_Business_School_Brochure.pdf',
    },
    {
        id: 'handbook',
        title: 'Student Handbook',
        category: 'Student Life',
        description: 'Policies, procedures, grading rubrics, and the code of conduct for all enrolled candidates in NOUN Business School.',
        fileSize: '1.8 MB',
        pages: 120,
        updatedAt: 'January 2026',
        previewImage: 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800&q=80',
        downloadUrl: '#',
    },
    {
        id: 'calendar',
        title: 'Academic Calendar',
        category: 'Administration',
        description: 'Important dates for the current academic session including residency periods, examination windows, and holidays.',
        fileSize: '0.5 MB',
        pages: 2,
        updatedAt: 'September 2026',
        previewImage: 'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&q=80',
        downloadUrl: '#',
    },
    {
        id: 'timetable',
        title: 'Lecture Timetable - Fall Semester',
        category: 'Academics',
        description: 'Detailed schedule for physical residencies and online live sessions for all MBA and DBA cohorts.',
        fileSize: '1.1 MB',
        pages: 5,
        updatedAt: 'August 2026',
        previewImage: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80',
        downloadUrl: '#',
    }
]);

const selectedResource = ref(documentResources.value[0]);

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

</script>

<template>
    <Head title="Resources - NOUN Business School" />
    <div id="resources-page" class="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">
<!-- HEADER -->
        <header
            class="fixed top-0 inset-x-0 z-50 transition-all duration-500"
            :class="scrolled ? 'bg-white/85 backdrop-blur-lg border-b border-gray-200/50 shadow-[0_4px_30px_rgba(0,0,0,0.03)]' : 'bg-transparent'"
        >
            <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-20">
                    <Link :href="route('home')" class="flex items-center gap-3 flex-shrink-0">
                        <img src="/nbs-logo.png" alt="NOUN Business School Logo" class="h-12 w-auto object-contain drop-shadow-sm" />
                        <div class="leading-tight">
                            <div class="font-bold text-sm tracking-tight text-noun-dark transition-colors duration-300">
                                NOUN Business School
                            </div>
                            <div class="text-xs text-gray-500 transition-colors duration-300">
                                National Open University
                            </div>
                        </div>
                    </Link>

                    <nav class="hidden lg:flex items-center gap-7">
                        <template v-for="link in navLinks" :key="link.label">
                            <a
                                v-if="link.href.startsWith('#') || link.href.startsWith('/#')"
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

                    <div class="hidden lg:flex items-center gap-3">
                        <Link v-if="$page.props.auth?.user" :href="route('dashboard')" class="text-sm font-medium text-noun-green hover:text-noun-dark transition-colors">My Dashboard</Link>
                        <template v-else>
                            <Link :href="route('login')" class="text-sm font-medium border rounded-md px-4 py-2 transition-all duration-200 text-noun-dark border-gray-300 hover:border-noun-dark hover:bg-gray-50">Applicant Login</Link>
                            <Link :href="route('admission.start')" class="text-sm font-semibold bg-noun-green text-white px-5 py-2 rounded-md hover:bg-noun-dark transition-colors shadow-sm">Apply Now</Link>
                        </template>
                    </div>

                    <button class="lg:hidden p-2 rounded-md text-noun-dark transition-colors" @click="mobileMenuOpen = !mobileMenuOpen" aria-label="Toggle menu">
                        <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
                        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>
            </div>

            <!-- Mobile drawer -->
            <div v-if="mobileMenuOpen" class="lg:hidden bg-white border-t border-gray-100 shadow-xl">
                <div class="px-4 pt-4 pb-6 space-y-1">
                    <template v-for="link in navLinks" :key="link.label">
                        <a v-if="link.href.startsWith('#') || link.href.startsWith('/#')" :href="link.href" class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors" @click="mobileMenuOpen = false">{{ link.label }}</a>
                        <Link v-else :href="link.href" class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors" @click="mobileMenuOpen = false">{{ link.label }}</Link>
                    </template>
                    <div class="pt-4 border-t border-gray-100 space-y-2 mt-4">
                        <Link :href="route('login')" class="block px-3 py-3 text-center text-noun-dark border border-gray-200 rounded-md text-sm font-medium hover:bg-gray-50 transition-colors" @click="mobileMenuOpen = false">Applicant Login</Link>
                        <Link :href="route('admission.start')" class="block px-3 py-3 text-center bg-noun-green text-white rounded-md text-sm font-semibold hover:bg-noun-dark transition-colors" @click="mobileMenuOpen = false">Apply Now</Link>
                    </div>
                </div>
            </div>
        </header>
        <!-- MAIN CONTENT -->
        <main class="flex-grow pt-20 bg-gray-50">
            <!-- Interactive Document Viewer -->
            <section class="py-16 relative bg-gray-50 border-b border-gray-200">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    
                    <div class="flex flex-col lg:flex-row gap-8 bg-white rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-gray-100 overflow-hidden min-h-[600px]" v-reveal>
                        
                        <!-- Left Side: List of Resources -->
                        <div class="w-full lg:w-1/3 bg-gray-50/50 border-r border-gray-100 flex flex-col">
                            <div class="p-6 border-b border-gray-100 bg-white">
                                <h3 class="text-xl font-bold text-noun-dark">Document Library</h3>
                                <p class="text-sm text-gray-500 mt-1">Select a document to preview</p>
                            </div>
                            
                            <div class="flex-grow overflow-y-auto p-4 space-y-2 h-[500px]">
                                <button 
                                    v-for="doc in documentResources" 
                                    :key="doc.id"
                                    @click="selectedResource = doc"
                                    class="w-full text-left p-4 rounded-2xl transition-all duration-300 border group"
                                    :class="selectedResource.id === doc.id ? 'bg-noun-green/10 border-noun-green/30 shadow-sm' : 'bg-white border-transparent hover:border-gray-200 hover:bg-gray-50'"
                                >
                                    <div class="flex items-start gap-4">
                                        <div class="w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 transition-colors"
                                             :class="selectedResource.id === doc.id ? 'bg-noun-green text-white' : 'bg-gray-100 text-gray-400 group-hover:bg-gray-200 group-hover:text-noun-dark'">
                                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                                        </div>
                                        <div>
                                            <div class="text-xs font-bold uppercase tracking-wider mb-1" :class="selectedResource.id === doc.id ? 'text-noun-green' : 'text-gray-400'">{{ doc.category }}</div>
                                            <h4 class="font-bold text-sm leading-tight transition-colors" :class="selectedResource.id === doc.id ? 'text-noun-dark' : 'text-gray-600 group-hover:text-noun-dark'">{{ doc.title }}</h4>
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </div>

                        <!-- Right Side: Preview & Download -->
                        <div class="w-full lg:w-2/3 p-8 lg:p-12 flex flex-col bg-white">
                            <div class="flex flex-col md:flex-row gap-8 h-full">
                                
                                <!-- Document Preview Image / PDF Viewer -->
                                <div class="w-full md:w-1/2 flex flex-col items-center justify-center bg-gray-100 rounded-2xl overflow-hidden relative shadow-inner border border-gray-200 group h-[500px]">
                                    <iframe v-if="selectedResource.downloadUrl !== '#'" :src="selectedResource.downloadUrl + '#toolbar=0&navpanes=0&scrollbar=0'" class="w-full h-full border-0"></iframe>
                                    <template v-else>
                                        <img :src="selectedResource.previewImage" :alt="selectedResource.title" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-500 mix-blend-multiply" />
                                        <div class="absolute inset-0 flex items-center justify-center bg-noun-dark/20 backdrop-blur-[2px]">
                                            <div class="bg-white/90 text-noun-dark px-4 py-2 rounded-full font-bold text-sm shadow-lg flex items-center gap-2">
                                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                                Document Coming Soon
                                            </div>
                                        </div>
                                    </template>
                                </div>

                                <!-- Document Details & Actions -->
                                <div class="w-full md:w-1/2 flex flex-col">
                                    <div class="inline-block bg-noun-yellow/20 text-noun-dark text-xs font-bold tracking-widest uppercase mb-4 px-3 py-1 rounded-full self-start">{{ selectedResource.category }}</div>
                                    <h2 class="text-3xl font-extrabold text-noun-dark mb-4 leading-tight">{{ selectedResource.title }}</h2>
                                    <p class="text-gray-600 mb-8 text-base leading-relaxed">{{ selectedResource.description }}</p>
                                    
                                    <div class="bg-gray-50 rounded-xl p-5 mb-8 border border-gray-100">
                                        <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Document Information</h4>
                                        <div class="grid grid-cols-2 gap-4">
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">File Size</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.fileSize }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Pages</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.pages }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Last Updated</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.updatedAt }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Format</span>
                                                <span class="font-bold text-noun-dark">PDF</span>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="mt-auto pt-4 flex flex-col sm:flex-row gap-4">
                                        <a :href="selectedResource.downloadUrl" target="_blank" download class="flex-1 bg-noun-green text-white px-6 py-4 rounded-xl hover:bg-noun-dark font-bold text-center transition-all duration-300 shadow-[0_4px_15px_rgba(0,102,0,0.2)] hover:shadow-[0_8px_25px_rgba(0,102,0,0.3)] hover:-translate-y-0.5 flex items-center justify-center gap-2">
                                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                            Download Document
                                        </a>
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>
            </section>

            <!-- Portals & Digital Resources -->
            <section class="py-24 bg-white relative overflow-hidden">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                    <div class="flex items-center justify-between mb-16" v-reveal>
                        <div>
                            <h2 class="text-3xl font-bold text-noun-dark mb-2">Digital Ecosystem</h2>
                            <p class="text-gray-600">Access platforms dedicated to research, administration, and support.</p>
                        </div>
                    </div>

                    <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                        <!-- E-Library -->
                        <a href="#" class="flex items-start gap-6 p-6 rounded-2xl border border-gray-100 hover:border-noun-green/30 hover:bg-noun-light/5 transition-all group" v-reveal>
                            <div class="w-14 h-14 bg-gray-50 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-noun-green/10 transition-colors">
                                <svg class="w-7 h-7 text-noun-dark group-hover:text-noun-green transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-noun-dark mb-1 group-hover:text-noun-green transition-colors">NOUN E-Library</h4>
                                <p class="text-sm text-gray-600">Access millions of peer-reviewed journals, ebooks, and research databases across all management disciplines.</p>
                            </div>
                        </a>

                        <!-- LMS -->
                        <a href="#" class="flex items-start gap-6 p-6 rounded-2xl border border-gray-100 hover:border-noun-green/30 hover:bg-noun-light/5 transition-all group" v-reveal="100">
                            <div class="w-14 h-14 bg-gray-50 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-noun-green/10 transition-colors">
                                <svg class="w-7 h-7 text-noun-dark group-hover:text-noun-green transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-noun-dark mb-1 group-hover:text-noun-green transition-colors">Learning Management System</h4>
                                <p class="text-sm text-gray-600">Log in to Moodle to access your course materials, submit assignments, and participate in discussion forums.</p>
                            </div>
                        </a>

                        <!-- IT Support -->
                        <a href="#" class="flex items-start gap-6 p-6 rounded-2xl border border-gray-100 hover:border-noun-yellow/40 hover:bg-noun-yellow/5 transition-all group" v-reveal="200">
                            <div class="w-14 h-14 bg-gray-50 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-noun-yellow/20 transition-colors">
                                <svg class="w-7 h-7 text-noun-dark group-hover:text-noun-dark transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-noun-dark mb-1">IT Service Desk</h4>
                                <p class="text-sm text-gray-600">Get technical support for your student email, portal access, password resets, and network connectivity.</p>
                            </div>
                        </a>

                        <!-- Faculty Portal -->
                        <a href="#" class="flex items-start gap-6 p-6 rounded-2xl border border-gray-100 hover:border-noun-dark/20 hover:bg-gray-50 transition-all group" v-reveal="300">
                            <div class="w-14 h-14 bg-gray-50 rounded-xl flex items-center justify-center flex-shrink-0 group-hover:bg-noun-dark group-hover:text-white transition-colors">
                                <svg class="w-7 h-7 text-noun-dark group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                            </div>
                            <div>
                                <h4 class="text-lg font-bold text-noun-dark mb-1">Faculty & Staff Portal</h4>
                                <p class="text-sm text-gray-600">Exclusive access for academics to grade management, internal memos, and research grant applications.</p>
                            </div>
                        </a>
                    </div>
                </div>
            </section>
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
                                <span class="text-noun-yellow mt-0.5 flex-shrink-0">📍</span>
                                <span>NOUN Headquarters, University Village, Jabi, Abuja, Nigeria</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <span class="text-noun-yellow mt-0.5 flex-shrink-0">🌐</span>
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
</style>
