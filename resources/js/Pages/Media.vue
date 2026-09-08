<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref, onMounted, onUnmounted } from 'vue';

defineProps({
    canLogin: { type: Boolean },
    canRegister: { type: Boolean },
});

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

const mobileMenuOpen = ref(false);
const scrolled = ref(false);

function handleScroll() {
    scrolled.value = window.scrollY > 60;
}

onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));

const navLinks = [
    { label: 'Home',             href: route('home') },
    { label: 'About',            href: route('about') },
    { label: 'Programmes',       href: route('programmes') },
    { label: 'Admissions',       href: '/#admissions' },
    { label: 'Media',            href: route('media') },
    { label: 'Resources',        href: route('resources') },
    { label: 'Careers',          href: route('career') },
    { label: 'Contact',          href: '#contact' },
];
</script>

<template>
    <Head title="Media - NOUN Business School" />
    <div id="media-page" class="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">
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


            <!-- Latest News -->
            <section class="py-24 relative bg-white">
                <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">
                    <div class="flex flex-col md:flex-row md:items-center justify-between mb-12 gap-6" v-reveal>
                        <h2 class="text-3xl font-bold text-noun-dark">Latest News</h2>
                        
                        <!-- Category Filter -->
                        <div class="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0 hide-scrollbar">
                            <button class="px-5 py-2 rounded-full bg-noun-dark text-white text-sm font-semibold whitespace-nowrap">View All</button>
                            <button class="px-5 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 text-sm font-semibold transition-colors whitespace-nowrap">Press Releases</button>
                            <button class="px-5 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 text-sm font-semibold transition-colors whitespace-nowrap">Academics</button>
                            <button class="px-5 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 text-sm font-semibold transition-colors whitespace-nowrap">Events</button>
                        </div>
                    </div>
                    
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <!-- News Card 1 -->
                        <div class="bg-white rounded-3xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-gray-100 overflow-hidden hover:shadow-[0_10px_40px_rgba(0,102,0,0.08)] hover:-translate-y-2 transition-all duration-500 group flex flex-col" v-reveal>
                            <div class="h-60 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000 ease-out" />
                                <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                                <div class="absolute top-4 left-4 bg-noun-yellow text-noun-dark text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest shadow-lg">Press Release</div>
                            </div>
                            <div class="p-8 flex-grow flex flex-col justify-between">
                                <div>
                                    <div class="flex items-center gap-3 text-gray-400 text-sm mb-4 font-medium">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                        September 1, 2026
                                    </div>
                                    <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors line-clamp-2">NOUN Business School Announces Maiden Cohort Resumption</h3>
                                    <p class="text-gray-600 mb-8 line-clamp-3 leading-relaxed">The highly anticipated executive programmes will officially commence lectures, blending world-class physical residencies with advanced open distance learning platforms.</p>
                                </div>
                                <a href="#" class="inline-flex items-center gap-2 text-noun-green font-bold hover:text-noun-dark transition-colors group/link mt-auto">
                                    Read Full Article 
                                    <span class="group-hover/link:translate-x-1 transition-transform">&rarr;</span>
                                </a>
                            </div>
                        </div>

                        <!-- News Card 2 -->
                        <div class="bg-white rounded-3xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-gray-100 overflow-hidden hover:shadow-[0_10px_40px_rgba(0,102,0,0.08)] hover:-translate-y-2 transition-all duration-500 group flex flex-col" v-reveal="100">
                            <div class="h-60 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000 ease-out" />
                                <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                                <div class="absolute top-4 left-4 bg-noun-green text-white text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest shadow-lg">Event</div>
                            </div>
                            <div class="p-8 flex-grow flex flex-col justify-between">
                                <div>
                                    <div class="flex items-center gap-3 text-gray-400 text-sm mb-4 font-medium">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                        August 28, 2026
                                    </div>
                                    <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors line-clamp-2">Strategic Partnership Signed with African Enterprise Institute</h3>
                                    <p class="text-gray-600 mb-8 line-clamp-3 leading-relaxed">A new MOU has been signed to provide DBA candidates with unprecedented access to cross-border trade data and executive mentorship programs.</p>
                                </div>
                                <a href="#" class="inline-flex items-center gap-2 text-noun-green font-bold hover:text-noun-dark transition-colors group/link mt-auto">
                                    Read Full Article 
                                    <span class="group-hover/link:translate-x-1 transition-transform">&rarr;</span>
                                </a>
                            </div>
                        </div>

                        <!-- News Card 3 -->
                        <div class="bg-white rounded-3xl shadow-[0_4px_20px_rgba(0,0,0,0.03)] border border-gray-100 overflow-hidden hover:shadow-[0_10px_40px_rgba(0,102,0,0.08)] hover:-translate-y-2 transition-all duration-500 group flex flex-col" v-reveal="200">
                            <div class="h-60 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1558403194-611308249627?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-1000 ease-out" />
                                <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                                <div class="absolute top-4 left-4 bg-noun-dark text-white text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest shadow-lg">Academics</div>
                            </div>
                            <div class="p-8 flex-grow flex flex-col justify-between">
                                <div>
                                    <div class="flex items-center gap-3 text-gray-400 text-sm mb-4 font-medium">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                        August 15, 2026
                                    </div>
                                    <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors line-clamp-2">Curriculum Innovation: The Integration of AI in Management</h3>
                                    <p class="text-gray-600 mb-8 line-clamp-3 leading-relaxed">NBS unveils its updated curriculum featuring specialized tracks in Artificial Intelligence strategy for modern business leaders.</p>
                                </div>
                                <a href="#" class="inline-flex items-center gap-2 text-noun-green font-bold hover:text-noun-dark transition-colors group/link mt-auto">
                                    Read Full Article 
                                    <span class="group-hover/link:translate-x-1 transition-transform">&rarr;</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            
            <!-- Newsletter Subscription -->
            <section class="py-16 bg-noun-green relative overflow-hidden">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff10_1px,transparent_1px),linear-gradient(to_bottom,#ffffff10_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24 relative z-10">
                    <div class="bg-white/10 border border-white/20 rounded-3xl p-8 md:p-12 backdrop-blur-sm flex flex-col md:flex-row items-center justify-between gap-8 shadow-2xl" v-reveal>
                        <div class="max-w-xl text-center md:text-left">
                            <h3 class="text-2xl md:text-3xl font-bold text-white mb-3">Never miss an update.</h3>
                            <p class="text-white/80 text-lg">Join our media mailing list to receive the latest press releases, event invites, and announcements directly in your inbox.</p>
                        </div>
                        <div class="w-full md:w-auto flex-shrink-0">
                            <form class="flex flex-col sm:flex-row gap-3 w-full sm:w-[400px]">
                                <input type="email" placeholder="Enter your email address" class="flex-grow px-5 py-4 rounded-xl border-none focus:ring-4 focus:ring-noun-yellow/50 shadow-inner" required />
                                <button type="submit" class="px-8 py-4 bg-noun-yellow text-noun-dark font-bold rounded-xl hover:bg-white transition-colors shadow-lg whitespace-nowrap">Subscribe</button>
                            </form>
                        </div>
                    </div>
                </div>
            </section>

<!-- Video/Media Highlights -->
            <section class="py-24 bg-white relative">
                <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="text-center mb-16" v-reveal>
                        <h2 class="text-3xl font-bold text-noun-dark mb-4">Multimedia</h2>
                        <p class="text-gray-600 max-w-2xl mx-auto">Experience the vibrant academic environment and hear directly from our faculty and leaders.</p>
                    </div>

                    <div class="grid lg:grid-cols-2 gap-8">
                        <!-- Main Video -->
                        <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-[0_8px_30px_rgba(0,0,0,0.12)] hover:shadow-[0_20px_50px_rgba(0,102,0,0.2)] transition-all duration-500 min-h-[360px] lg:min-h-full h-full" v-reveal>
                            <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1200&q=80" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000 ease-out" alt="Campus Tour Video" />
                            <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/90 via-noun-dark/30 to-transparent group-hover:from-noun-dark group-hover:via-noun-dark/50 transition-colors duration-500"></div>
                            
                            <!-- Glowing Play Button -->
                            <div class="absolute inset-0 flex items-center justify-center">
                                <div class="relative">
                                    <div class="absolute inset-0 bg-noun-yellow/40 rounded-full blur-xl group-hover:blur-2xl group-hover:scale-125 transition-all duration-500"></div>
                                    <div class="relative w-20 h-20 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/50 group-hover:bg-noun-yellow group-hover:border-noun-yellow transition-all duration-500 transform group-hover:scale-110">
                                        <svg class="w-8 h-8 text-white group-hover:text-noun-dark ml-1 transition-colors" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                    </div>
                                </div>
                            </div>

                            <div class="absolute bottom-0 left-0 w-full p-8 transform translate-y-2 group-hover:translate-y-0 transition-transform duration-500">
                                <div class="inline-block bg-noun-yellow/20 backdrop-blur-sm border border-noun-yellow/30 text-noun-yellow text-xs font-bold tracking-widest uppercase mb-3 px-3 py-1 rounded-full">Campus Tour</div>
                                <h3 class="text-white text-3xl font-extrabold leading-tight">Discover NOUN Business School</h3>
                            </div>
                        </div>

                        <!-- Secondary Videos -->
                        <div class="grid grid-rows-2 gap-6">
                            <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-[0_8px_30px_rgba(0,0,0,0.12)] hover:shadow-[0_20px_50px_rgba(0,102,0,0.2)] transition-all duration-500 min-h-[220px]" v-reveal="100">
                                <img src="/Mande.jpeg" class="absolute inset-0 w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-1000 ease-out" alt="Director Address" />
                                <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/90 via-noun-dark/20 to-transparent group-hover:from-noun-dark transition-colors duration-500"></div>
                                
                                <div class="absolute inset-0 flex items-center justify-center">
                                    <div class="w-14 h-14 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/50 group-hover:bg-noun-yellow group-hover:border-noun-yellow transition-all duration-500 transform group-hover:scale-110 shadow-lg">
                                        <svg class="w-6 h-6 text-white group-hover:text-noun-dark ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                    </div>
                                </div>
                                <div class="absolute bottom-0 left-0 w-full p-6 transform translate-y-1 group-hover:translate-y-0 transition-transform duration-500">
                                    <div class="text-noun-yellow text-xs font-bold tracking-widest uppercase mb-1">Keynote</div>
                                    <h3 class="text-white text-xl font-bold leading-snug">Director's Welcome Address</h3>
                                </div>
                            </div>

                            <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-[0_8px_30px_rgba(0,0,0,0.12)] hover:shadow-[0_20px_50px_rgba(0,102,0,0.2)] transition-all duration-500 min-h-[220px]" v-reveal="200">
                                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000 ease-out" alt="Alumni Stories" />
                                <div class="absolute inset-0 bg-gradient-to-t from-noun-dark/90 via-noun-dark/20 to-transparent group-hover:from-noun-dark transition-colors duration-500"></div>
                                
                                <div class="absolute inset-0 flex items-center justify-center">
                                    <div class="w-14 h-14 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/50 group-hover:bg-noun-yellow group-hover:border-noun-yellow transition-all duration-500 transform group-hover:scale-110 shadow-lg">
                                        <svg class="w-6 h-6 text-white group-hover:text-noun-dark ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                    </div>
                                </div>
                                <div class="absolute bottom-0 left-0 w-full p-6 transform translate-y-1 group-hover:translate-y-0 transition-transform duration-500">
                                    <div class="text-noun-yellow text-xs font-bold tracking-widest uppercase mb-1">Testimonials</div>
                                    <h3 class="text-white text-xl font-bold leading-snug">Alumni Success Stories</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Press Resources & Contact -->
            <section class="py-24 bg-noun-dark text-white relative">
                <div class="w-full mx-auto px-4 sm:px-8 lg:px-16 xl:px-24">
                    <div class="grid lg:grid-cols-2 gap-16 items-center">
                        <div v-reveal>
                            <h2 class="text-3xl font-bold mb-6">Press Resources</h2>
                            <p class="text-white/70 text-lg mb-8 leading-relaxed">
                                Need official logos, executive headshots, or brand guidelines? Access our comprehensive media kit tailored for journalists and partners.
                            </p>
                            <a href="#" class="inline-flex items-center gap-2 px-8 py-4 bg-noun-yellow text-noun-dark font-bold rounded-lg hover:bg-white transition-colors">
                                Download Media Kit
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                            </a>
                        </div>
                        <div class="bg-white/5 border border-white/10 rounded-3xl p-10 backdrop-blur-sm" v-reveal="100">
                            <h3 class="text-xl font-bold text-noun-yellow mb-4">Media Enquiries</h3>
                            <p class="text-white/70 mb-6">For press inquiries, interview requests, or permission to film on campus, please contact the Directorate of Media and Publicity.</p>
                            
                            <div class="space-y-4">
                                <div class="flex items-center gap-4">
                                    <div class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center flex-shrink-0">
                                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                                    </div>
                                    <span class="text-white font-medium">media@noun.edu.ng</span>
                                </div>
                                <div class="flex items-center gap-4">
                                    <div class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center flex-shrink-0">
                                        <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                                    </div>
                                    <span class="text-white font-medium">+234 (0) 800 NOUN BNS</span>
                                </div>
                            </div>
                        </div>
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

.hide-scrollbar::-webkit-scrollbar {
    display: none;
}
.hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
</style>
