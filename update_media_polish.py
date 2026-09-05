import re

with open('resources/js/Pages/Media.vue', 'r') as f:
    media = f.read()

# Add categories to the News section
news_section_start = media.find('<!-- Latest News -->')
news_section_end = media.find('<!-- Video/Media Highlights -->')

new_news_section = """<!-- Latest News -->
            <section class="py-24 relative bg-white">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
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
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
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
"""

new_media = media[:news_section_start] + new_news_section + "\n" + media[news_section_end:]

# Add hide-scrollbar style
style_insertion = """
.hide-scrollbar::-webkit-scrollbar {
    display: none;
}
.hide-scrollbar {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
"""

new_media = new_media.replace('</style>', style_insertion + '</style>')

with open('resources/js/Pages/Media.vue', 'w') as f:
    f.write(new_media)

print("Media polished")
