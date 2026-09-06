with open('resources/js/Pages/Student/Results.vue', 'r') as f:
    content = f.read()

target = """        <template #header>
            <div class="flex items-center justify-between w-full">
                <h2 class="text-xl font-bold leading-tight text-noun-dark">Academic Results</h2>
                <a v-if="hasAnyGrades" :href="route('student.results.download')" target="_blank" class="inline-flex items-center gap-2 bg-noun-green hover:bg-noun-dark text-white px-4 py-2 rounded-lg font-semibold transition-colors duration-200 shadow-sm text-sm">
                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Download Statement
                </a>
            </div>
        </template>"""

replacement = """        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Academic Results</h2>
        </template>"""

if target in content:
    content = content.replace(target, replacement)
    with open('resources/js/Pages/Student/Results.vue', 'w') as f:
        f.write(content)
    print("Reverted Results.vue header")
else:
    print("Target not found in Results.vue")
