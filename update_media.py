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

# We also need the closing tags and style
style_start = about.find('<style scoped>')
style_block = about[style_start:] if style_start != -1 else """<style scoped>
:global(html) {
    scroll-behavior: smooth;
}
</style>"""

media_main = """
        <!-- MAIN CONTENT -->
        <main class="flex-grow pt-20 bg-gray-50">
            <!-- Hero Section -->
            <section class="relative pt-32 pb-24 lg:pt-40 lg:pb-32 bg-gradient-to-br from-noun-dark to-[#001a00] overflow-hidden text-center text-white">
                <div class="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                
                <div class="absolute top-0 left-[-10%] w-[40%] h-[40%] bg-noun-green/20 rounded-full blur-[120px] pointer-events-none"></div>
                <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-noun-yellow/20 rounded-full blur-[120px] pointer-events-none"></div>

                <div class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 lg:px-8" v-reveal>
                    <div class="inline-flex items-center gap-3 mb-6">
                        <div class="h-px w-8 bg-noun-yellow"></div>
                        <span class="text-noun-yellow text-xs font-bold tracking-widest uppercase">Media Center</span>
                        <div class="h-px w-8 bg-noun-yellow"></div>
                    </div>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold leading-tight tracking-tight mb-8 text-white">
                        News, Insights & <span class="text-transparent bg-clip-text bg-gradient-to-r from-noun-yellow to-noun-yellow-light">Stories</span>
                    </h1>
                    <p class="text-lg lg:text-xl text-white/70 leading-relaxed max-w-3xl mx-auto">
                        Discover the latest announcements, thought leadership, and inspiring journeys from the NOUN Business School community.
                    </p>
                </div>
            </section>

            <!-- Latest News -->
            <section class="py-24 relative">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex items-center justify-between mb-12" v-reveal>
                        <h2 class="text-3xl font-bold text-noun-dark">Latest News</h2>
                        <a href="#" class="text-noun-green font-semibold hover:text-noun-dark transition-colors flex items-center gap-2">
                            View All <span aria-hidden="true">&rarr;</span>
                        </a>
                    </div>
                    
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                        <!-- News Card 1 -->
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group" v-reveal>
                            <div class="h-56 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                                <div class="absolute top-4 left-4 bg-noun-yellow text-noun-dark text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">Press Release</div>
                            </div>
                            <div class="p-8">
                                <div class="text-gray-400 text-sm mb-3">September 1, 2026</div>
                                <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors">NOUN Business School Announces Maiden Cohort Resumption</h3>
                                <p class="text-gray-600 mb-6 line-clamp-3">The highly anticipated executive programmes will officially commence lectures, blending world-class physical residencies with advanced open distance learning platforms.</p>
                                <a href="#" class="text-noun-green font-semibold hover:text-noun-dark transition-colors inline-flex items-center gap-2">
                                    Read Article <span aria-hidden="true">&rarr;</span>
                                </a>
                            </div>
                        </div>

                        <!-- News Card 2 -->
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group" v-reveal="100">
                            <div class="h-56 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                                <div class="absolute top-4 left-4 bg-noun-green text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">Event</div>
                            </div>
                            <div class="p-8">
                                <div class="text-gray-400 text-sm mb-3">August 28, 2026</div>
                                <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors">Strategic Partnership Signed with African Enterprise Institute</h3>
                                <p class="text-gray-600 mb-6 line-clamp-3">A new MOU has been signed to provide DBA candidates with unprecedented access to cross-border trade data and executive mentorship programs.</p>
                                <a href="#" class="text-noun-green font-semibold hover:text-noun-dark transition-colors inline-flex items-center gap-2">
                                    Read Article <span aria-hidden="true">&rarr;</span>
                                </a>
                            </div>
                        </div>

                        <!-- News Card 3 -->
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-xl hover:-translate-y-1 transition-all duration-300 group" v-reveal="200">
                            <div class="h-56 bg-gray-200 relative overflow-hidden">
                                <img src="https://images.unsplash.com/photo-1558403194-611308249627?w=800&q=80" alt="News Image" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                                <div class="absolute top-4 left-4 bg-noun-dark text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">Academics</div>
                            </div>
                            <div class="p-8">
                                <div class="text-gray-400 text-sm mb-3">August 15, 2026</div>
                                <h3 class="text-xl font-bold text-noun-dark mb-4 leading-snug group-hover:text-noun-green transition-colors">Curriculum Innovation: The Integration of AI in Management</h3>
                                <p class="text-gray-600 mb-6 line-clamp-3">NBS unveils its updated curriculum featuring specialized tracks in Artificial Intelligence strategy for modern business leaders.</p>
                                <a href="#" class="text-noun-green font-semibold hover:text-noun-dark transition-colors inline-flex items-center gap-2">
                                    Read Article <span aria-hidden="true">&rarr;</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Video/Media Highlights -->
            <section class="py-24 bg-white relative">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="text-center mb-16" v-reveal>
                        <h2 class="text-3xl font-bold text-noun-dark mb-4">Multimedia</h2>
                        <p class="text-gray-600 max-w-2xl mx-auto">Experience the vibrant academic environment and hear directly from our faculty and leaders.</p>
                    </div>

                    <div class="grid lg:grid-cols-2 gap-8">
                        <!-- Main Video -->
                        <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-lg" v-reveal>
                            <img src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1200&q=80" class="w-full h-[400px] object-cover group-hover:scale-105 transition-transform duration-700" alt="Video Thumbnail" />
                            <div class="absolute inset-0 bg-noun-dark/40 group-hover:bg-noun-dark/30 transition-colors"></div>
                            <div class="absolute inset-0 flex items-center justify-center">
                                <div class="w-20 h-20 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/40 group-hover:scale-110 group-hover:bg-noun-yellow group-hover:border-noun-yellow transition-all duration-300">
                                    <svg class="w-8 h-8 text-white group-hover:text-noun-dark ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                </div>
                            </div>
                            <div class="absolute bottom-0 left-0 w-full p-8 bg-gradient-to-t from-noun-dark/90 to-transparent">
                                <div class="text-noun-yellow text-sm font-bold tracking-wide uppercase mb-2">Campus Tour</div>
                                <h3 class="text-white text-2xl font-bold">Discover NOUN Business School</h3>
                            </div>
                        </div>

                        <!-- Secondary Videos -->
                        <div class="grid grid-rows-2 gap-8">
                            <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-lg" v-reveal="100">
                                <img src="/Mande.jpeg" class="w-full h-full min-h-[184px] object-cover object-top group-hover:scale-105 transition-transform duration-700" alt="Video Thumbnail" />
                                <div class="absolute inset-0 bg-noun-dark/60 group-hover:bg-noun-dark/40 transition-colors"></div>
                                <div class="absolute inset-0 flex items-center justify-center">
                                    <div class="w-14 h-14 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/40 group-hover:scale-110 group-hover:bg-noun-yellow transition-all duration-300">
                                        <svg class="w-6 h-6 text-white group-hover:text-noun-dark ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                    </div>
                                </div>
                                <div class="absolute bottom-0 left-0 w-full p-6 bg-gradient-to-t from-noun-dark/90 to-transparent">
                                    <h3 class="text-white text-lg font-bold">Director's Welcome Address</h3>
                                </div>
                            </div>
                            <div class="relative rounded-3xl overflow-hidden group cursor-pointer shadow-lg" v-reveal="200">
                                <img src="https://images.unsplash.com/photo-1577415124269-dba114465553?w=800&q=80" class="w-full h-full min-h-[184px] object-cover group-hover:scale-105 transition-transform duration-700" alt="Video Thumbnail" />
                                <div class="absolute inset-0 bg-noun-dark/40 group-hover:bg-noun-dark/30 transition-colors"></div>
                                <div class="absolute inset-0 flex items-center justify-center">
                                    <div class="w-14 h-14 bg-white/20 backdrop-blur-md rounded-full flex items-center justify-center border border-white/40 group-hover:scale-110 group-hover:bg-noun-yellow transition-all duration-300">
                                        <svg class="w-6 h-6 text-white group-hover:text-noun-dark ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                    </div>
                                </div>
                                <div class="absolute bottom-0 left-0 w-full p-6 bg-gradient-to-t from-noun-dark/90 to-transparent">
                                    <h3 class="text-white text-lg font-bold">Alumni Success Stories</h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Press Resources & Contact -->
            <section class="py-24 bg-noun-dark text-white relative">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
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
"""

new_content = script_block + "\n\n<template>\n    <Head title=\"Media - NOUN Business School\" />\n    <div id=\"media-page\" class=\"min-h-screen bg-white text-gray-900 font-sans antialiased flex flex-col\">\n" + header_block + media_main + footer_block + "\n    </div>\n</template>\n\n" + style_block

with open('resources/js/Pages/Media.vue', 'w') as f:
    f.write(new_content)

print("Media.vue successfully built.")
