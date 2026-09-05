import re

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    welcome = f.read()

# Extract script block
script_start = welcome.find('<script setup>')
script_end = welcome.find('</script>') + len('</script>')
script_block = welcome[script_start:script_end]

# Modify the script block for About.vue (we only need navLinks and vReveal)
# Let's just create a custom script block for About.vue that imports Head/Link and defines navLinks/mobileMenu/scroll
about_script = """<script setup>
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
    { label: 'Programmes',       href: '/#programmes' },
    { label: 'Admissions',       href: '/#admissions' },
    { label: 'Media',            href: route('media') },
    { label: 'Resources',        href: route('resources') },
    { label: 'Contact',          href: '#contact' },
];
</script>"""

# Extract Header
header_start = welcome.find('<header')
header_end = welcome.find('</header>') + len('</header>')
header_block = welcome[header_start:header_end]
# The mobile drawer is right below header
drawer_start = welcome.find('<!-- Mobile drawer -->')
drawer_end = welcome.find('</div>\n        </header>') # wait, it's outside header?
if drawer_start > -1:
    drawer_end = welcome.find('</div>', welcome.find('<!-- Mobile drawer -->'))
    # actually let's just grab from <header to the end of the mobile drawer or we can just regex it.

# To be safe, I'll manually construct About.vue.

about_content = about_script + """

<template>
    <Head title="About - NOUN Business School" />
    <div id="about-page" class="min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col">

        <!-- HEADER -->
        <header
            class="fixed top-0 inset-x-0 z-50 transition-all duration-500"
            :class="scrolled ? 'bg-white/85 backdrop-blur-lg border-b border-gray-200/50 shadow-[0_4px_30px_rgba(0,0,0,0.03)]' : 'bg-transparent'"
        >
            <div class="w-full 2xl:px-12 px-4 sm:px-6 lg:px-8">
                <div class="flex items-center justify-between h-20">
                    <Link :href="route('home')" class="flex items-center gap-3 flex-shrink-0">
                        <img src="/bns%20logo.png" alt="NOUN Business School Logo" class="h-12 w-auto object-contain drop-shadow-sm" />
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
        <main class="flex-grow pt-20">
            <!-- Hero Section -->
            <section class="relative pt-32 pb-24 lg:pt-40 lg:pb-32 bg-gradient-to-br from-white via-white to-noun-light/30 overflow-hidden">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#004d0005_1px,transparent_1px),linear-gradient(to_bottom,#004d0005_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center" v-reveal>
                    <div class="inline-flex items-center gap-3 mb-6">
                        <div class="h-px w-8 bg-noun-yellow"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Our Story</span>
                        <div class="h-px w-8 bg-noun-yellow"></div>
                    </div>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-noun-dark leading-tight tracking-tight mb-8">
                        Redefining Business Education for the <span class="text-transparent bg-clip-text bg-gradient-to-r from-noun-green to-noun-dark">Modern Professional</span>
                    </h1>
                    <p class="text-lg lg:text-xl text-gray-600 leading-relaxed max-w-3xl mx-auto">
                        NOUN Business School is a specialised graduate institution of the National Open University of Nigeria, designed exclusively to deliver premium, technology-enabled management education to working executives, public servants, and entrepreneurs.
                    </p>
                </div>
            </section>

            <!-- Director's Message -->
            <section class="py-24 bg-white relative">
                <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="lg:grid lg:grid-cols-12 gap-16 items-center">
                        <div class="lg:col-span-5 mb-12 lg:mb-0" v-reveal>
                            <div class="relative">
                                <div class="absolute inset-0 bg-noun-green rounded-3xl translate-x-4 translate-y-4 opacity-10"></div>
                                <img src="/Mande.jpeg" alt="Professor Samaila Mande" class="relative z-10 w-full h-[500px] object-cover rounded-3xl border-4 border-white shadow-xl" />
                                
                                <!-- Floating Badge -->
                                <div class="absolute -bottom-6 -left-6 z-20 bg-white p-6 rounded-2xl shadow-xl border border-gray-100 max-w-[240px]">
                                    <div class="text-noun-dark font-bold text-lg leading-tight">Professor Samaila Mande</div>
                                    <div class="text-noun-yellow font-bold text-xs uppercase tracking-wider mt-2">Director, NOUN Business School</div>
                                </div>
                            </div>
                        </div>
                        <div class="lg:col-span-7" v-reveal="100">
                            <h2 class="text-3xl font-bold text-noun-dark mb-8">A Message from the Director</h2>
                            <div class="space-y-6 text-gray-600 text-lg leading-relaxed">
                                <p>Welcome to NOUN Business School, a trailblazing institution established by the National Open University of Nigeria to fill a critical gap in postgraduate management education in Africa.</p>
                                <p>We recognize that today's leaders cannot always afford to pause their careers for full-time study. Yet, the demand for rigorous, globally benchmarked business knowledge has never been higher. This is the paradox we solve.</p>
                                <p>Our Open Distance Learning (ODL) framework is not merely a convenience; it is a pedagogical innovation. By blending asynchronous digital learning, intensive weekend residencies, and live consultancy engagements, we bring the classroom to the boardroom.</p>
                                <blockquote class="border-l-4 border-noun-yellow pl-6 py-2 my-8 italic text-xl font-medium text-noun-dark">
                                    "To our cohorts: you are not merely enrolling in a programme, you are helping to establish the standards, character and reputation of this Business School."
                                </blockquote>
                                <p>We invite you to join our growing community of professionals who are transforming industries and shaping the future of African business.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Mission, Vision, Core Values -->
            <section class="py-24 bg-noun-dark relative overflow-hidden">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                    <div class="grid lg:grid-cols-3 gap-12 text-white">
                        
                        <!-- Vision -->
                        <div class="bg-white/5 border border-white/10 p-10 rounded-3xl hover:bg-white/10 transition-colors" v-reveal>
                            <div class="w-14 h-14 bg-noun-yellow/20 text-noun-yellow rounded-2xl flex items-center justify-center mb-6">
                                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                            </div>
                            <h3 class="text-2xl font-bold mb-4">Our Vision</h3>
                            <p class="text-white/70 leading-relaxed">
                                To be a leading centre of flexible, technology-enabled business and management education in Africa, producing globally competitive and nationally committed leaders.
                            </p>
                        </div>

                        <!-- Mission -->
                        <div class="bg-white/5 border border-white/10 p-10 rounded-3xl hover:bg-white/10 transition-colors" v-reveal="100">
                            <div class="w-14 h-14 bg-noun-yellow/20 text-noun-yellow rounded-2xl flex items-center justify-center mb-6">
                                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            </div>
                            <h3 class="text-2xl font-bold mb-4">Our Mission</h3>
                            <p class="text-white/70 leading-relaxed">
                                To provide accessible, cost-effective, and high-quality postgraduate business education that empowers working professionals to advance their careers and contribute to national development.
                            </p>
                        </div>

                        <!-- Core Values -->
                        <div class="bg-white/5 border border-white/10 p-10 rounded-3xl hover:bg-white/10 transition-colors" v-reveal="200">
                            <div class="w-14 h-14 bg-noun-yellow/20 text-noun-yellow rounded-2xl flex items-center justify-center mb-6">
                                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                            </div>
                            <h3 class="text-2xl font-bold mb-4">Core Values</h3>
                            <ul class="text-white/70 space-y-3">
                                <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div> Academic Excellence</li>
                                <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div> Integrity & Ethics</li>
                                <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div> Flexibility & Accessibility</li>
                                <li class="flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div> Innovation</li>
                            </ul>
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
                            <img src="/bns%20logo.png" alt="NOUN Business School Logo" class="h-14 w-auto object-contain drop-shadow-lg" />
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
"""

with open('resources/js/Pages/About.vue', 'w') as f:
    f.write(about_content)

print("About.vue developed successfully.")
