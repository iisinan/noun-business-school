import re

with open('resources/js/Layouts/AdminLayout.vue', 'r') as f:
    content = f.read()

target = "    { name: 'Users', href: route('admin.users.index'), active: route().current('admin.users.*'), icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },"
replacement = """    { name: 'Sessions', href: route('admin.sessions.index'), active: route().current('admin.sessions.*'), icon: 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z' },
    { name: 'Users', href: route('admin.users.index'), active: route().current('admin.users.*'), icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },"""

content = content.replace(target, replacement)

with open('resources/js/Layouts/AdminLayout.vue', 'w') as f:
    f.write(content)

with open('resources/js/Pages/Admin/Dashboard.vue', 'r') as f:
    dashboard = f.read()

dashboard_target = """                                <a href="#" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Sessions</span>
                                </a>"""

dashboard_replacement = """                                <Link :href="route('admin.sessions.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Sessions</span>
                                </Link>"""

dashboard = dashboard.replace(dashboard_target, dashboard_replacement)

with open('resources/js/Pages/Admin/Dashboard.vue', 'w') as f:
    f.write(dashboard)

