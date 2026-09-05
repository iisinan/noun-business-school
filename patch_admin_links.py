with open('resources/js/Layouts/AdminLayout.vue', 'r') as f:
    content = f.read()

target_nav = """                <nav class="flex-1 px-4 py-6 space-y-2">
                    <Link
                        v-for="item in navigation"
                        :key="item.name"
                        :href="item.href"
                        :class="[
                            item.active ? 'bg-noun-green text-white font-semibold shadow-md' : 'text-gray-300 hover:bg-[#004d1f] hover:text-white transition-colors',
                            'group flex items-center px-4 py-3 text-sm rounded-xl'
                        ]"
                    >
                        <svg class="mr-3 h-5 w-5 flex-shrink-0" :class="item.active ? 'text-white' : 'text-gray-400 group-hover:text-white'" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                        </svg>
                        {{ item.name }}
                    </Link>
                </nav>

                <div class="p-4 border-t border-[#004d1f]">
                    <Link
                        :href="route('logout')"
                        method="post"
                        as="button"
                        class="group flex w-full items-center px-4 py-3 text-sm rounded-xl text-gray-300 hover:bg-red-500 hover:text-white transition-colors"
                    >
                        <svg class="mr-3 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                        </svg>
                        Sign Out
                    </Link>
                </div>"""

replacement_nav = """                <nav class="flex-1 px-4 py-6 space-y-1.5">
                    <Link
                        v-for="item in navigation"
                        :key="item.name"
                        :href="item.href"
                        :class="[
                            item.active 
                                ? 'bg-white/10 text-white shadow-sm ring-1 ring-white/20' 
                                : 'text-gray-300 hover:bg-white/5 hover:text-white',
                            'group flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all duration-200'
                        ]"
                    >
                        <svg :class="[item.active ? 'text-noun-yellow' : 'text-gray-400 group-hover:text-gray-300', 'h-5 w-5 flex-shrink-0 transition-colors']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                        </svg>
                        <span class="flex-1">{{ item.name }}</span>
                        <!-- Active Indicator -->
                        <div v-if="item.active" class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div>
                    </Link>
                </nav>

                <div class="p-4 border-t border-white/10 shrink-0">
                    <Link 
                        :href="route('logout')" 
                        method="post" 
                        as="button" 
                        class="w-full flex items-center justify-center gap-2 px-4 py-2 text-sm font-semibold text-red-400 hover:text-red-300 hover:bg-red-400/10 rounded-lg transition-colors"
                    >
                        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" /></svg>
                        Sign Out
                    </Link>
                </div>"""

if target_nav in content:
    content = content.replace(target_nav, replacement_nav)
    with open('resources/js/Layouts/AdminLayout.vue', 'w') as f:
        f.write(content)
    print("Patched AdminLayout.vue links")
else:
    print("Could not find nav block in AdminLayout.vue")
