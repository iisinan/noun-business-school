file_path = '/Users/sinan/Herd/Business School/resources/js/Layouts/AuthenticatedLayout.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                    <div class="h-10 w-10 rounded-lg bg-noun-green flex items-center justify-center text-white font-bold shrink-0 shadow-inner">
                        {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                    </div>"""

replace = """                    <div v-if="user.passport_url" class="h-10 w-10 rounded-lg flex items-center justify-center shrink-0 border border-white/20 shadow-sm overflow-hidden bg-white/5">
                        <img :src="user.passport_url" class="h-full w-full object-cover" alt="Profile" />
                    </div>
                    <div v-else class="h-10 w-10 rounded-lg bg-noun-green flex items-center justify-center text-white font-bold shrink-0 shadow-inner">
                        {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                    </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched AuthenticatedLayout.vue sidebar")
else:
    print("Search block not found in AuthenticatedLayout.vue sidebar")
    
search2 = """                                        <div class="h-8 w-8 rounded-full bg-noun-dark flex items-center justify-center text-white font-bold text-xs shrink-0 shadow-sm">
                                            {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                                        </div>"""

replace2 = """                                        <div v-if="user.passport_url" class="h-8 w-8 rounded-full shrink-0 shadow-sm overflow-hidden border border-gray-200">
                                            <img :src="user.passport_url" class="h-full w-full object-cover" alt="Profile" />
                                        </div>
                                        <div v-else class="h-8 w-8 rounded-full bg-noun-dark flex items-center justify-center text-white font-bold text-xs shrink-0 shadow-sm">
                                            {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                                        </div>"""

if search2 in content:
    content = content.replace(search2, replace2)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched AuthenticatedLayout.vue topbar")
else:
    print("Search block not found in AuthenticatedLayout.vue topbar")

