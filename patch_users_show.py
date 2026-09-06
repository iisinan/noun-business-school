file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Users/Show.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """            <!-- User Profile Header -->
            <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100 flex flex-col md:flex-row gap-6 items-center">
                <div class="h-20 w-20 rounded-full bg-noun-dark flex items-center justify-center text-white text-2xl font-bold flex-shrink-0 shadow-inner">
                    {{ getInitials(user.first_name, user.last_name) }}
                </div>"""

replace = """            <!-- User Profile Header -->
            <div class="bg-white p-6 shadow-sm rounded-xl border border-gray-100 flex flex-col md:flex-row gap-6 items-center">
                <div v-if="user.passport_url" class="h-20 w-20 rounded-full flex items-center justify-center flex-shrink-0 border border-gray-200 shadow-sm overflow-hidden bg-gray-50">
                    <img :src="user.passport_url" class="h-full w-full object-cover" alt="User Passport" />
                </div>
                <div v-else class="h-20 w-20 rounded-full bg-noun-dark flex items-center justify-center text-white text-2xl font-bold flex-shrink-0 shadow-inner">
                    {{ getInitials(user.first_name, user.last_name) }}
                </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Users/Show.vue")
else:
    print("Search block not found")
