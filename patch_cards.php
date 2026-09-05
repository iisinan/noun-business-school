<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Programmes.vue';
$content = file_get_contents($file);

$search = <<<VUE
                                <div v-for="track in programmes[activeTab]" :key="track.code"
                                    @click="openCourse(track)"
                                    class="relative bg-white border border-gray-100 rounded-2xl p-3 sm:p-4 hover:shadow-[0_12px_40px_rgba(0,77,0,0.10)] hover:-translate-y-1 hover:border-noun-green/20 transition-all duration-300 cursor-pointer group flex flex-col overflow-hidden">
                                    
                                    <!-- Top hover accent line -->
                                    <div class="absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r from-noun-green/0 via-noun-green to-noun-green/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                                    
                                    <!-- Icon + code -->
                                    <div class="flex items-start justify-between mb-3">
                                        <div class="w-8 h-8 rounded-lg bg-noun-green/8 flex items-center justify-center group-hover:bg-noun-green/15 transition-colors duration-300">
                                            <svg class="w-4 h-4 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                        </div>
                                        <span class="text-[10px] font-bold tracking-widest text-noun-yellow bg-noun-yellow/10 px-2.5 py-1 rounded-full uppercase">{{ track.code }}</span>
                                    </div>

                                    <!-- Title -->
                                    <h4 class="text-sm font-bold text-noun-dark mb-2 group-hover:text-noun-green transition-colors duration-300 leading-snug flex-grow">{{ track.title }}</h4>

                                    <!-- Meta pills -->
                                    <div class="flex flex-wrap gap-1.5 mb-3">
                                        <span class="text-[10px] text-gray-500 bg-gray-50 border border-gray-100 px-2.5 py-1 rounded-full font-medium">ODL Mode</span>
                                        <span class="text-[10px] text-gray-500 bg-gray-50 border border-gray-100 px-2.5 py-1 rounded-full font-medium">18–24 Months</span>
                                    </div>

                                    <!-- Footer -->
                                    <div class="pt-3 border-t border-gray-100 flex items-center justify-between mt-auto">
                                        <span class="text-xs font-semibold text-gray-400">NOUN Business School</span>
                                        <span class="flex items-center gap-1.5 text-xs font-bold text-noun-green transition-all duration-300 group-hover:gap-2">
                                            Learn More
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
                                        </span>
                                    </div>
                                </div>
VUE;

$replace = <<<VUE
                                <div v-for="track in programmes[activeTab]" :key="track.code"
                                    @click="openCourse(track)"
                                    class="relative bg-white border border-gray-200/60 rounded-2xl p-4 shadow-sm hover:shadow-[0_16px_40px_-10px_rgba(0,77,0,0.15)] hover:-translate-y-1.5 hover:border-noun-green/30 transition-all duration-300 cursor-pointer group flex flex-col overflow-hidden">
                                    
                                    <!-- Beautiful Top Gradient Glow -->
                                    <div class="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-noun-yellow via-noun-green to-noun-dark opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                                    <div class="absolute -top-12 -right-12 w-24 h-24 bg-noun-green/5 rounded-full blur-2xl group-hover:bg-noun-green/10 transition-colors duration-500"></div>
                                    
                                    <!-- Icon + code -->
                                    <div class="flex items-start justify-between mb-4 relative z-10">
                                        <div class="w-10 h-10 rounded-full bg-gray-50 flex items-center justify-center group-hover:bg-noun-green/10 group-hover:scale-110 transition-all duration-300 shadow-sm border border-gray-100 group-hover:border-noun-green/20">
                                            <svg class="w-4 h-4 text-gray-400 group-hover:text-noun-green transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                                        </div>
                                        <span class="text-[10px] font-black tracking-widest text-noun-dark bg-gray-100 group-hover:bg-noun-yellow group-hover:text-white px-3 py-1.5 rounded-full uppercase transition-colors duration-300 shadow-sm">{{ track.code }}</span>
                                    </div>

                                    <!-- Title -->
                                    <h4 class="text-sm font-extrabold text-gray-900 mb-3 group-hover:text-noun-green transition-colors duration-300 leading-snug flex-grow relative z-10 pr-2">{{ track.title }}</h4>

                                    <!-- Meta items with icons -->
                                    <div class="flex flex-col gap-2 mb-4 relative z-10">
                                        <div class="flex items-center gap-1.5 text-[11px] font-semibold text-gray-500">
                                            <svg class="w-3.5 h-3.5 text-gray-400 group-hover:text-noun-yellow transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>
                                            100% Online (ODL)
                                        </div>
                                        <div class="flex items-center gap-1.5 text-[11px] font-semibold text-gray-500">
                                            <svg class="w-3.5 h-3.5 text-gray-400 group-hover:text-noun-green transition-colors duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                            18–24 Months
                                        </div>
                                    </div>

                                    <!-- Footer -->
                                    <div class="pt-3 border-t border-gray-100 flex items-center justify-between mt-auto relative z-10">
                                        <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wide">NBS Track</span>
                                        <span class="flex items-center gap-1 text-[11px] font-bold text-noun-green transition-all duration-300">
                                            Explore
                                            <svg class="w-3.5 h-3.5 transform group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                                        </span>
                                    </div>
                                </div>
VUE;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Cards\n";
