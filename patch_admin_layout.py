with open('resources/js/Layouts/AdminLayout.vue', 'r') as f:
    content = f.read()

target_remove = """                <div class="flex items-center justify-center h-20 bg-[#002810] border-b border-[#004d1f] px-4">
                    <h1 class="text-white font-black text-xl tracking-wider text-center">NBS <span class="text-noun-yellow">ADMIN</span></h1>
                </div>
                
                <!-- Admin Profile Snippet -->
                <div class="px-6 py-6 border-b border-[#004d1f]">
                    <div class="flex items-center gap-3">
                        <div class="h-10 w-10 rounded-full bg-noun-yellow flex items-center justify-center text-noun-dark font-bold border-2 border-white shadow-sm">
                            {{ $page.props.auth.user.first_name?.charAt(0) || $page.props.auth.user.name?.charAt(0) }}
                        </div>
                        <div>
                            <p class="text-sm font-bold text-white">{{ $page.props.auth.user.first_name || $page.props.auth.user.name }}</p>
                            <p class="text-xs text-green-300">Super Admin</p>
                        </div>
                    </div>
                </div>"""

replacement = """                <!-- Branding -->
                <div class="h-20 flex items-center px-6 bg-[#002810] border-b border-[#004d1f] shrink-0">
                    <Link :href="route('admin.dashboard')" class="flex items-center gap-3 w-full">
                        <div class="h-10 w-10 bg-white rounded-lg flex items-center justify-center shadow-inner p-1 overflow-hidden shrink-0">
                            <img src="/nbs-logo.png" alt="NOUN" class="h-full w-auto object-contain">
                        </div>
                        <div class="min-w-0 flex flex-col justify-center">
                            <span class="text-[13px] font-black text-white tracking-widest block truncate leading-tight">BUSINESS SCHOOL</span>
                            <span class="text-[10px] text-noun-yellow font-bold uppercase tracking-widest block truncate leading-tight mt-0.5">Admin Portal</span>
                        </div>
                    </Link>
                </div>"""

if target_remove in content:
    content = content.replace(target_remove, replacement)
    with open('resources/js/Layouts/AdminLayout.vue', 'w') as f:
        f.write(content)
    print("Patched AdminLayout.vue")
else:
    print("Could not find target block in AdminLayout.vue")

