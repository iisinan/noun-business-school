import re

with open('resources/js/Pages/Admin/Dashboard.vue', 'r') as f:
    content = f.read()

target = """                                <a href="#" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Users</span>
                                </a>"""

replacement = """                                <Link :href="route('admin.users.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Users</span>
                                </Link>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Admin/Dashboard.vue', 'w') as f:
    f.write(content)

