import re

files = [
    '/Users/sinan/Herd/Business School/resources/js/Layouts/StudentLayout.vue',
    '/Users/sinan/Herd/Business School/resources/js/Layouts/ApplicantLayout.vue'
]

search = """                    <div class="h-10 w-10 rounded-lg bg-noun-green flex items-center justify-center text-white font-bold shrink-0 shadow-inner">
                        {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                    </div>"""

replace = """                    <div v-if="user.passport_url" class="h-10 w-10 rounded-lg flex items-center justify-center shrink-0 border border-white/20 shadow-sm overflow-hidden bg-white/5">
                        <img :src="user.passport_url" class="h-full w-full object-cover" alt="Profile" />
                    </div>
                    <div v-else class="h-10 w-10 rounded-lg bg-noun-green flex items-center justify-center text-white font-bold shrink-0 shadow-inner">
                        {{ user.first_name.charAt(0) }}{{ user.last_name.charAt(0) }}
                    </div>"""

for file_path in files:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        if search in content:
            content = content.replace(search, replace)
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Patched {file_path}")
        else:
            print(f"Search block not found in {file_path}")
    except Exception as e:
        print(f"Error in {file_path}: {e}")

