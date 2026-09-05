import re

with open('resources/js/Layouts/AdminLayout.vue', 'r') as f:
    content = f.read()

target = "    { name: 'Users', href: route('admin.users.index'), active: route().current('admin.users.*'), icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },"
replacement = """    { name: 'Payments', href: route('admin.payments.index'), active: route().current('admin.payments.*'), icon: 'M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z' },
    { name: 'Users', href: route('admin.users.index'), active: route().current('admin.users.*'), icon: 'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z' },"""

content = content.replace(target, replacement)

with open('resources/js/Layouts/AdminLayout.vue', 'w') as f:
    f.write(content)

with open('resources/js/Pages/Admin/Dashboard.vue', 'r') as f:
    dashboard = f.read()

dashboard_target = """                                <a href="#" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Payments</span>
                                </a>"""

dashboard_replacement = """                                <Link :href="route('admin.payments.index')" class="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-xl border border-gray-100 hover:bg-noun-green hover:text-white hover:border-noun-green transition group">
                                    <svg class="h-6 w-6 text-gray-500 group-hover:text-white mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
                                    </svg>
                                    <span class="text-xs font-semibold text-center">Payments</span>
                                </Link>"""

dashboard = dashboard.replace(dashboard_target, dashboard_replacement)

with open('resources/js/Pages/Admin/Dashboard.vue', 'w') as f:
    f.write(dashboard)

