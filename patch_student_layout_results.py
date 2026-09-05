import re

with open('resources/js/Layouts/StudentLayout.vue', 'r') as f:
    content = f.read()

target = """                            <!-- Coming Soon: My Results -->
                            <div class="flex items-center gap-3 px-4 py-2.5 rounded-xl text-gray-400/50 cursor-not-allowed">
                                <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                                <span class="text-sm">My Results (Coming Soon)</span>
                            </div>"""

replacement = """                            <Link :href="route('student.results')" class="flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" :class="route().current('student.results') ? 'bg-noun-green/20 text-white font-bold' : 'text-gray-300 hover:bg-noun-green/10 hover:text-white'">
                                <svg class="w-5 h-5 flex-shrink-0 opacity-70" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                                <span class="text-sm">My Results</span>
                                <div v-if="route().current('student.results')" class="w-1.5 h-1.5 rounded-full bg-noun-yellow ml-auto"></div>
                            </Link>"""

content = content.replace(target, replacement)

with open('resources/js/Layouts/StudentLayout.vue', 'w') as f:
    f.write(content)
