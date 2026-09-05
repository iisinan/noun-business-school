import re

with open('resources/js/Layouts/StudentLayout.vue', 'r') as f:
    content = f.read()

target_nav = """const navigation = [
    { name: 'Dashboard', href: route('student.dashboard'), active: route().current('student.dashboard'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
];"""

replacement_nav = """const navigation = [
    { header: 'MAIN' },
    { name: 'Dashboard', href: route('student.dashboard'), active: route().current('student.dashboard'), icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
    { header: 'ACADEMICS' },
    { name: 'Course Registration', href: route('student.dashboard'), active: false, icon: 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253' },
    { name: 'My Results (Coming Soon)', href: '#', active: false, icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
    { header: 'FINANCE' },
    { name: 'Payment History', href: '#', active: false, icon: 'M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z' },
];"""

content = content.replace(target_nav, replacement_nav)

target_aside = """        <!-- Sidebar -->
        <aside :class="[sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0']" class="fixed inset-y-0 left-0 z-50 w-72 bg-noun-dark text-white transition-transform duration-300 ease-in-out flex flex-col shadow-2xl lg:shadow-none lg:static">"""

replacement_aside = """        <!-- Sidebar -->
        <aside :class="[sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0']" class="fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-noun-dark to-[#004d00] text-white transition-transform duration-300 ease-in-out flex flex-col shadow-2xl lg:shadow-none lg:static">"""

content = content.replace(target_aside, replacement_aside)

target_nav_links = """            <div class="flex-1 overflow-y-auto py-6 px-4 space-y-1">
                <Link v-for="item in navigation" :key="item.name" :href="item.href"
                    :class="[
                        item.active 
                            ? 'bg-noun-green text-white shadow-md' 
                            : 'text-gray-300 hover:bg-white/10 hover:text-white',
                        'group flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all duration-200'
                    ]"
                >
                    <svg :class="[item.active ? 'text-white' : 'text-gray-400 group-hover:text-white', 'h-5 w-5 shrink-0 transition-colors']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                    </svg>
                    {{ item.name }}
                </Link>
            </div>"""

replacement_nav_links = """            <div class="flex-1 overflow-y-auto py-6 px-4 space-y-1.5">
                <template v-for="(item, index) in navigation" :key="index">
                    <!-- Section Header -->
                    <div v-if="item.header" class="px-4 pt-4 pb-1 text-[10px] font-black text-gray-400 uppercase tracking-widest">
                        {{ item.header }}
                    </div>
                    
                    <!-- Navigation Link -->
                    <component 
                        :is="item.href === '#' ? 'div' : Link" 
                        v-else 
                        :href="item.href !== '#' ? item.href : undefined"
                        :class="[
                            item.active 
                                ? 'bg-white/10 text-white shadow-sm ring-1 ring-white/20' 
                                : 'text-gray-300 hover:bg-white/5 hover:text-white',
                            item.href === '#' ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer',
                            'group flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all duration-200'
                        ]"
                    >
                        <svg :class="[item.active ? 'text-noun-yellow' : 'text-gray-400 group-hover:text-gray-300', 'h-5 w-5 shrink-0 transition-colors']" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon" />
                        </svg>
                        <span class="flex-1">{{ item.name }}</span>
                        <!-- Active Indicator -->
                        <div v-if="item.active" class="w-1.5 h-1.5 rounded-full bg-noun-yellow"></div>
                    </component>
                </template>
            </div>"""

content = content.replace(target_nav_links, replacement_nav_links)


with open('resources/js/Layouts/StudentLayout.vue', 'w') as f:
    f.write(content)

