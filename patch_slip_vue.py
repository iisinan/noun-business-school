file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/Slip.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                <div class="flex items-center gap-5">
                    <img src="/nbs-logo.png" alt="NOUN Logo" class="h-24 w-auto">
                    <div>
                        <h1 class="text-2xl font-black text-noun-green tracking-tight uppercase">National Open University of Nigeria</h1>
                        <h2 class="text-lg font-bold text-gray-800 tracking-wide mt-1">Business School (NBS)</h2>
                        <p class="text-sm text-gray-500 font-medium mt-0.5">Course Registration E-Slip</p>
                    </div>
                </div>"""

replace = """                <div class="flex items-center gap-5">
                    <img src="/nbs-logo.png" alt="NOUN Logo" class="h-24 w-auto">
                    <div>
                        <h1 class="text-2xl font-black text-noun-green tracking-tight uppercase">National Open University of Nigeria</h1>
                        <h2 class="text-lg font-bold text-gray-800 tracking-wide mt-1">Business School (NBS)</h2>
                        <p class="text-sm text-gray-500 font-medium mt-0.5">Course Registration E-Slip</p>
                    </div>
                </div>
                <!-- Student Passport -->
                <div v-if="$page.props.auth.user.passport_url" class="h-32 w-32 border border-gray-300 p-1 bg-white shrink-0 overflow-hidden shadow-sm">
                    <img :src="$page.props.auth.user.passport_url" class="h-full w-full object-cover" alt="Student Passport">
                </div>
                <div v-else class="h-32 w-32 border border-gray-300 p-1 bg-gray-50 shrink-0 flex items-center justify-center text-gray-400 text-xs text-center shadow-sm">
                    Passport<br>Photograph
                </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Slip.vue")
else:
    print("Search block not found")
