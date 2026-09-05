with open('resources/js/Layouts/GuestLayout.vue', 'r') as f:
    content = f.read()

target = """        <!-- Right Side (Auth Form) -->
        <div class="flex-1 flex flex-col justify-center items-center py-12 px-4 sm:px-6 lg:px-20 xl:px-24">
            <div class="mx-auto w-full max-w-sm lg:w-96">"""

replacement = """        <!-- Right Side (Auth Form) -->
        <div class="flex-1 flex flex-col justify-center items-center py-12 px-4 sm:px-6 lg:px-20 xl:px-24 relative">
            <Link :href="route('home')" class="absolute top-8 left-8 sm:left-12 flex items-center gap-2 text-sm font-semibold text-gray-500 hover:text-gray-900 transition bg-white px-4 py-2 rounded-full shadow-sm border border-gray-200">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" /></svg>
                Back to Home
            </Link>

            <div class="mx-auto w-full max-w-sm lg:w-96">"""

content = content.replace(target, replacement)

with open('resources/js/Layouts/GuestLayout.vue', 'w') as f:
    f.write(content)
