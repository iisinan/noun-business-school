file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Applicant/Dashboard.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                    <div class="px-8 py-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                        <div>
                            <p class="text-noun-yellow text-sm font-medium uppercase tracking-wider mb-1">NOUN Business School</p>
                            <h3 class="text-2xl font-bold text-white">Welcome, {{ $page.props.auth.user.first_name }}!</h3>"""

replace = """                    <div class="px-8 py-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-6">
                            <div v-if="$page.props.auth.user.passport_url" class="h-16 w-16 sm:h-20 sm:w-20 rounded-full border-2 border-noun-yellow shadow-lg overflow-hidden shrink-0 bg-gray-50">
                                <img :src="$page.props.auth.user.passport_url" class="h-full w-full object-cover" alt="Passport" />
                            </div>
                            <div>
                                <p class="text-noun-yellow text-sm font-medium uppercase tracking-wider mb-1">NOUN Business School</p>
                                <h3 class="text-2xl font-bold text-white">Welcome, {{ $page.props.auth.user.first_name }}!</h3>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Applicant Dashboard")
else:
    print("Search block not found in Applicant Dashboard")
