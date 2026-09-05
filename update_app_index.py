import re

with open('resources/js/Pages/Admin/Applications/Index.vue', 'r') as f:
    content = f.read()

header = """                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">All Applications</h3>
                            <span class="text-sm text-gray-500">{{ applications.total }} total</span>
                        </div>
                        <a :href="route('admin.applications.export')" class="inline-flex items-center gap-2 bg-white border border-gray-300 text-gray-700 px-4 py-2 rounded-lg text-sm font-semibold hover:bg-gray-50 transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                            </svg>
                            Export CSV
                        </a>
                    </div>"""

content = content.replace("""                    <!-- Table Header -->
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                        <h3 class="text-base font-semibold text-gray-900">All Applications</h3>
                        <span class="text-sm text-gray-500">{{ applications.total }} total</span>
                    </div>""", header)

with open('resources/js/Pages/Admin/Applications/Index.vue', 'w') as f:
    f.write(content)

