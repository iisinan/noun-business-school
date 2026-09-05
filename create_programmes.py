with open('resources/js/Pages/About.vue', 'r') as f:
    about = f.read()

# Extract the script block
script_start = about.find('<script setup>')
script_end = about.find('</script>') + len('</script>')
script_block = about[script_start:script_end]

# Modify the navLinks inside the script block to fix the routing globally for the new file
# We don't need to do it here, we will replace navLinks directly in the new script block.

# Extract the header block
header_start = about.find('<!-- HEADER -->')
header_end = about.find('</header>') + len('</header>')
header_block = about[header_start:header_end]

# Extract the footer block
footer_start = about.find('<!-- FOOTER -->')
footer_end = about.find('</footer>') + len('</footer>')
footer_block = about[footer_start:footer_end]

# Extract style block
style_start = about.find('<style scoped>')
style_block = about[style_start:]

new_script = """<script setup>
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

const programmes = {
    gdp: [
        { title: 'Graduate Diploma in Business Administration (GDBA)', code: 'NBS-701' },
    ],
    mpa: [
        { title: 'Public Administration', code: 'NBS-801' },
        { title: 'Public Policy', code: 'NBS-802' },
    ],
    dpa: [
        { title: 'Doctor of Public Administration (DPA)', code: 'NBS-901' },
    ],
    mba: [
        { title: 'Accounting', code: 'NBS-811' },
        { title: 'Aviation Management', code: 'NBS-812' },
        { title: 'Banking and Finance', code: 'NBS-813' },
        { title: 'Business Analytics', code: 'NBS-814' },
        { title: 'Cooperative Management', code: 'NBS-815' },
        { title: 'Corporate Governance', code: 'NBS-816' },
        { title: 'Digital Marketing', code: 'NBS-817' },
        { title: 'E-Business', code: 'NBS-818' },
        { title: 'Entrepreneurship', code: 'NBS-819' },
        { title: 'Event Management', code: 'NBS-820' },
        { title: 'Financial Management', code: 'NBS-821' },
        { title: 'Financial Technology (FinTech)', code: 'NBS-822' },
        { title: 'Health Care Management', code: 'NBS-823' },
        { title: 'Hospitality Management', code: 'NBS-824' },
        { title: 'Human Resource Management', code: 'NBS-825' },
        { title: 'Information Technology', code: 'NBS-826' },
        { title: 'International Business', code: 'NBS-827' },
        { title: 'Islamic Banking & Finance', code: 'NBS-828' },
        { title: 'Logistics and Supply Chain', code: 'NBS-829' },
        { title: 'Management', code: 'NBS-830' },
        { title: 'Marketing', code: 'NBS-831' },
        { title: 'Operations Management', code: 'NBS-832' },
        { title: 'Organisational Behaviour', code: 'NBS-833' },
        { title: 'Procurement Management', code: 'NBS-834' },
        { title: 'Project Management', code: 'NBS-835' },
        { title: 'Risk Management', code: 'NBS-836' },
        { title: 'Strategic Management', code: 'NBS-837' },
        { title: 'Tourism Management', code: 'NBS-838' },
    ],
    dba: [
        { title: 'Accounting', code: 'NBS-911' },
        { title: 'Aviation Management', code: 'NBS-912' },
        { title: 'Banking and Finance', code: 'NBS-913' },
        { title: 'Business Analytics', code: 'NBS-914' },
        { title: 'Cooperative Management', code: 'NBS-915' },
        { title: 'Corporate Governance', code: 'NBS-916' },
        { title: 'Digital Marketing', code: 'NBS-917' },
        { title: 'E-Business', code: 'NBS-918' },
        { title: 'Entrepreneurship', code: 'NBS-919' },
        { title: 'Event Management', code: 'NBS-920' },
        { title: 'Financial Management', code: 'NBS-921' },
        { title: 'Financial Technology (FinTech)', code: 'NBS-922' },
        { title: 'Health Care Management', code: 'NBS-923' },
        { title: 'Hospitality Management', code: 'NBS-924' },
        { title: 'Human Resource Management', code: 'NBS-925' },
        { title: 'Information Technology', code: 'NBS-926' },
        { title: 'International Business', code: 'NBS-927' },
        { title: 'Islamic Banking & Finance', code: 'NBS-928' },
        { title: 'Logistics and Supply Chain', code: 'NBS-929' },
        { title: 'Management', code: 'NBS-930' },
        { title: 'Marketing', code: 'NBS-931' },
        { title: 'Operations Management', code: 'NBS-932' },
        { title: 'Organisational Behaviour', code: 'NBS-933' },
        { title: 'Procurement Management', code: 'NBS-934' },
        { title: 'Project Management', code: 'NBS-935' },
        { title: 'Risk Management', code: 'NBS-936' },
        { title: 'Strategic Management', code: 'NBS-937' },
        { title: 'Tourism Management', code: 'NBS-938' },
    ]
};
</script>
"""

main_content = """
        <!-- MAIN CONTENT -->
        <main class="flex-grow pt-20 bg-gray-50">
            <!-- Hero Section -->
            <section class="relative pt-32 pb-24 lg:pt-40 lg:pb-32 bg-gradient-to-br from-white via-white to-noun-light/30 overflow-hidden text-center border-b border-gray-200">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#004d0005_1px,transparent_1px),linear-gradient(to_bottom,#004d0005_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                
                <div class="absolute top-0 left-[-10%] w-[40%] h-[40%] bg-noun-green/10 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-noun-yellow/10 rounded-full blur-[120px] pointer-events-none"></div>

                <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8" v-reveal>
                    <div class="inline-flex items-center gap-3 mb-6">
                        <div class="h-px w-8 bg-gradient-to-r from-noun-yellow to-transparent"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Academics</span>
                        <div class="h-px w-8 bg-gradient-to-l from-noun-yellow to-transparent"></div>
                    </div>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-noun-dark via-noun-green to-noun-dark leading-tight tracking-tight mb-8">
                        Our Executive<br>
                        <span class="relative inline-block">
                            <span class="relative z-10 text-transparent bg-clip-text bg-gradient-to-r from-noun-yellow to-noun-yellow-light">Programmes</span>
                            <span class="absolute bottom-2 left-0 w-full h-3 bg-noun-yellow/10 -z-10 -skew-x-12"></span>
                        </span>
                    </h1>
                    <p class="text-lg lg:text-xl text-gray-600 leading-relaxed max-w-3xl mx-auto">
                        A diverse portfolio of MBA and DBA specialisations engineered to empower you with industry-specific mastery and strategic leadership capabilities.
                    </p>
                </div>
            </section>

            <!-- Programmes Directory -->
            <section class="py-24 relative bg-gray-50">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    
                    <div class="flex flex-col lg:flex-row gap-12" v-reveal>
                        
                        <!-- Sidebar Navigation -->
                        <div class="w-full lg:w-1/4 flex-shrink-0">
                            <div class="sticky top-32 bg-white rounded-3xl p-6 shadow-sm border border-gray-100">
                                <h3 class="text-lg font-bold text-noun-dark mb-6 px-4">Degrees Offered</h3>
                                <div class="flex flex-col gap-2">
                                    <button @click="activeTab = 'gdp'" :class="activeTab === 'gdp' ? 'bg-noun-green text-white shadow-md' : 'text-gray-600 hover:bg-gray-50'" class="px-6 py-4 rounded-xl text-left font-bold transition-all duration-300">
                                        Graduate Diploma (GDBA)
                                    </button>
                                    <button @click="activeTab = 'mpa'" :class="activeTab === 'mpa' ? 'bg-noun-green text-white shadow-md' : 'text-gray-600 hover:bg-gray-50'" class="px-6 py-4 rounded-xl text-left font-bold transition-all duration-300">
                                        Master of Public Admin.
                                    </button>
                                    <button @click="activeTab = 'mba'" :class="activeTab === 'mba' ? 'bg-noun-green text-white shadow-md' : 'text-gray-600 hover:bg-gray-50'" class="px-6 py-4 rounded-xl text-left font-bold transition-all duration-300">
                                        Master of Business Admin.
                                        <span v-if="activeTab !== 'mba'" class="float-right text-xs bg-gray-200 text-gray-500 py-1 px-2 rounded-full">28</span>
                                        <span v-else class="float-right text-xs bg-white/20 text-white py-1 px-2 rounded-full">28</span>
                                    </button>
                                    <button @click="activeTab = 'dpa'" :class="activeTab === 'dpa' ? 'bg-noun-green text-white shadow-md' : 'text-gray-600 hover:bg-gray-50'" class="px-6 py-4 rounded-xl text-left font-bold transition-all duration-300">
                                        Doctor of Public Admin.
                                    </button>
                                    <button @click="activeTab = 'dba'" :class="activeTab === 'dba' ? 'bg-noun-green text-white shadow-md' : 'text-gray-600 hover:bg-gray-50'" class="px-6 py-4 rounded-xl text-left font-bold transition-all duration-300">
                                        Doctor of Business Admin.
                                        <span v-if="activeTab !== 'dba'" class="float-right text-xs bg-gray-200 text-gray-500 py-1 px-2 rounded-full">28</span>
                                        <span v-else class="float-right text-xs bg-white/20 text-white py-1 px-2 rounded-full">28</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Grid -->
                        <div class="w-full lg:w-3/4">
                            <div class="mb-12">
                                <h2 class="text-3xl font-extrabold text-noun-dark mb-4 uppercase tracking-wider" v-if="activeTab === 'gdp'">Graduate Diploma (GDBA)</h2>
                                <h2 class="text-3xl font-extrabold text-noun-dark mb-4 uppercase tracking-wider" v-if="activeTab === 'mpa'">Master of Public Administration (MPA)</h2>
                                <h2 class="text-3xl font-extrabold text-noun-dark mb-4 uppercase tracking-wider" v-if="activeTab === 'mba'">Master of Business Administration (MBA)</h2>
                                <h2 class="text-3xl font-extrabold text-noun-dark mb-4 uppercase tracking-wider" v-if="activeTab === 'dpa'">Doctor of Public Administration (DPA)</h2>
                                <h2 class="text-3xl font-extrabold text-noun-dark mb-4 uppercase tracking-wider" v-if="activeTab === 'dba'">Doctor of Business Administration (DBA)</h2>
                                
                                <p class="text-gray-600 text-lg">Select a specialisation track below to see the curriculum details.</p>
                            </div>

                            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                                <div v-for="track in programmes[activeTab]" :key="track.code" class="bg-white border border-gray-100 rounded-2xl p-8 hover:shadow-[0_10px_30px_rgba(0,102,0,0.08)] hover:-translate-y-1 transition-all duration-300 cursor-pointer group flex flex-col h-full">
                                    <div class="text-noun-yellow text-sm font-bold tracking-widest mb-3 uppercase">{{ track.code }}</div>
                                    <h4 class="text-lg font-bold text-noun-dark mb-6 group-hover:text-noun-green transition-colors leading-snug">{{ track.title }}</h4>
                                    
                                    <div class="mt-auto inline-flex items-center gap-2 text-sm font-bold text-noun-dark group-hover:text-noun-green transition-colors">
                                        View Curriculum <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        </main>
"""

new_content = new_script + "\n<template>\n    <Head title=\"Programmes - NOUN Business School\" />\n    <div class=\"min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col\">\n" + header_block + main_content + footer_block + "\n    </div>\n</template>\n\n" + style_block

with open('resources/js/Pages/Programmes.vue', 'w') as f:
    f.write(new_content)

print("Created Programmes.vue")
