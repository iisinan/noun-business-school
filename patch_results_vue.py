with open('resources/js/Pages/Student/Results.vue', 'r') as f:
    content = f.read()

target = """                <h2 class="text-2xl font-bold text-gray-800 tracking-tight">Academic Results</h2>
                <p class="text-gray-500 mt-1">View your performance across all registered semesters.</p>
            </div>"""

replacement = """                <h2 class="text-2xl font-bold text-gray-800 tracking-tight">Academic Results</h2>
                <p class="text-gray-500 mt-1">View your performance across all registered semesters.</p>
            </div>
            <div v-if="resultsBySession && resultsBySession.length > 0" class="flex-shrink-0">
                <a :href="route('student.results.download')" target="_blank" class="inline-flex items-center gap-2 bg-noun-green hover:bg-noun-dark text-white px-5 py-2.5 rounded-xl font-semibold transition-colors duration-200 shadow-sm">
                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                    </svg>
                    Download Result
                </a>
            </div>"""

if target in content:
    content = content.replace(target, replacement)
    with open('resources/js/Pages/Student/Results.vue', 'w') as f:
        f.write(content)
    print("Patched Results.vue")
else:
    print("Target not found in Results.vue")
