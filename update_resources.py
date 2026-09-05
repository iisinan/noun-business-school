with open('resources/js/Pages/About.vue', 'r') as f:
    about = f.read()

# Extract the script block
script_start = about.find('<script setup>')
script_end = about.find('</script>') + len('</script>')
script_block = about[script_start:script_end]

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

resources_main = """
        <!-- MAIN CONTENT -->
        <main class="flex-grow pt-20 bg-gray-50">
            <!-- Hero Section -->
            <section class="relative pt-32 pb-24 lg:pt-40 lg:pb-32 bg-gradient-to-br from-white via-white to-noun-light/30 overflow-hidden text-center">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#004d0005_1px,transparent_1px),linear-gradient(to_bottom,#004d0005_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                
                <div class="absolute top-0 left-[-10%] w-[40%] h-[40%] bg-noun-green/10 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-noun-yellow/10 rounded-full blur-[120px] pointer-events-none"></div>

                <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8" v-reveal>
                    <div class="inline-flex items-center gap-3 mb-6">
                        <div class="h-px w-8 bg-gradient-to-r from-noun-yellow to-transparent"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Knowledge Hub</span>
                        <div class="h-px w-8 bg-gradient-to-l from-noun-yellow to-transparent"></div>
                    </div>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-noun-dark via-noun-green to-noun-dark leading-tight tracking-tight mb-8">
                        Student & Academic<br>
                        <span class="relative inline-block">
                            <span class="relative z-10 text-transparent bg-clip-text bg-gradient-to-r from-noun-yellow to-noun-yellow-light">Resources</span>
                            <span class="absolute bottom-2 left-0 w-full h-3 bg-noun-yellow/10 -z-10 -skew-x-12"></span>
                        </span>
                    </h1>
                    <p class="text-lg lg:text-xl text-gray-600 leading-relaxed max-w-3xl mx-auto">
                        Access essential documents, download official course brochures, and connect to university-wide research and support portals.
                    </p>
                </div>
            </section>

            <!-- Key Downloads -->
            <section class="py-24 relative bg-gray-50 border-b border-gray-200">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="text-center mb-16" v-reveal>
                        <h2 class="text-3xl font-bold text-noun-dark mb-4">Essential Downloads</h2>
                        <p class="text-gray-600 max-w-2xl mx-auto">Quick access to the most requested academic documents and guidelines.</p>
                    </div>

                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
                        
                        <!-- Course Brochure -->
                        <div class="bg-white rounded-3xl p-8 shadow-sm border border-noun-green/20 hover:shadow-xl hover:-translate-y-1 hover:border-noun-green/40 transition-all duration-300 group flex flex-col items-start" v-reveal>
                            <div class="w-16 h-16 bg-noun-green/10 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-noun-green transition-all duration-300">
                                <svg class="w-8 h-8 text-noun-green group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-noun-dark mb-3">Official Course Brochure</h3>
                            <p class="text-gray-600 mb-8 leading-relaxed text-sm">Comprehensive breakdown of all 28 MBA and DBA specialisation tracks, course units, and faculty profiles for the 2026/2027 academic year.</p>
                            
                            <a href="#" class="mt-auto inline-flex items-center gap-2 bg-noun-dark text-white px-6 py-3 rounded-xl hover:bg-noun-green font-bold text-sm transition-colors w-full justify-center">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                Download PDF (4.2 MB)
                            </a>
                        </div>

                        <!-- Student Handbook -->
                        <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group flex flex-col items-start" v-reveal="100">
                            <div class="w-16 h-16 bg-gray-50 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                                <svg class="w-8 h-8 text-noun-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-noun-dark mb-3">Student Handbook</h3>
                            <p class="text-gray-600 mb-8 leading-relaxed text-sm">Policies, procedures, grading rubrics, and the code of conduct for all enrolled candidates in NOUN Business School.</p>
                            
                            <a href="#" class="mt-auto inline-flex items-center gap-2 bg-gray-100 text-noun-dark px-6 py-3 rounded-xl hover:bg-gray-200 font-bold text-sm transition-colors w-full justify-center">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                Download PDF (1.8 MB)
                            </a>
                        </div>

                        <!-- Academic Calendar -->
                        <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group flex flex-col items-start" v-reveal="200">
                            <div class="w-16 h-16 bg-gray-50 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                                <svg class="w-8 h-8 text-noun-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                            </div>
                            <h3 class="text-xl font-bold text-noun-dark mb-3">Academic Calendar</h3>
                            <p class="text-gray-600 mb-8 leading-relaxed text-sm">Important dates for the current academic session including residency periods, examination windows, and holidays.</p>
                            
                            <a href="#" class="mt-auto inline-flex items-center gap-2 bg-gray-100 text-noun-dark px-6 py-3 rounded-xl hover:bg-gray-200 font-bold text-sm transition-colors w-full justify-center">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                Download PDF (0.5 MB)
                            </a>
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
"""

new_content = script_block + "\n\n<template>\n    <Head title=\"Resources - NOUN Business School\" />\n    <div id=\"resources-page\" class=\"min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col\">\n" + header_block + resources_main + footer_block + "\n    </div>\n</template>\n\n" + style_block

with open('resources/js/Pages/Resources.vue', 'w') as f:
    f.write(new_content)

print("Resources.vue fully developed.")
