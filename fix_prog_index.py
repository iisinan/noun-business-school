import re

with open('resources/js/Pages/Admin/Programmes/Index.vue', 'r') as f:
    content = f.read()

target = """                        <button class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            Add Programme
                        </button>"""

replacement = """                        <Link :href="route('admin.programmes.create')" class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                            </svg>
                            Add Programme
                        </Link>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Admin/Programmes/Index.vue', 'w') as f:
    f.write(content)

