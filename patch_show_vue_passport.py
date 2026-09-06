file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Applications/Show.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                            <div class="h-10 w-10 rounded-full bg-noun-dark flex items-center justify-center text-white text-sm font-bold">
                                {{ application.user.first_name?.charAt(0) }}{{ application.user.last_name?.charAt(0) }}
                            </div>"""

replace = """                            <div v-if="application.passport_url" class="h-12 w-12 rounded-full flex items-center justify-center shrink-0 border border-gray-200 shadow-sm overflow-hidden bg-gray-50">
                                <img :src="application.passport_url" class="h-full w-full object-cover" alt="Applicant Passport" />
                            </div>
                            <div v-else class="h-12 w-12 rounded-full bg-noun-dark flex items-center justify-center text-white text-sm font-bold shrink-0 shadow-sm">
                                {{ application.user.first_name?.charAt(0) }}{{ application.user.last_name?.charAt(0) }}
                            </div>"""

content = content.replace(search, replace)
with open(file_path, 'w') as f:
    f.write(content)
print("Patched Admin Show.vue")
