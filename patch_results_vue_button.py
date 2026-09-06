with open('resources/js/Pages/Student/Results.vue', 'r') as f:
    content = f.read()

target = """            <div v-else class="space-y-8">
                
                <!-- CGPA Overview Card -->"""

replacement = """            <div v-else class="space-y-8">
                
                <!-- Header Actions -->
                <div class="flex justify-end">
                    <a v-if="hasAnyGrades" :href="route('student.results.download')" target="_blank" class="inline-flex items-center gap-2 bg-noun-green hover:bg-noun-dark text-white px-5 py-2.5 rounded-xl font-bold transition shadow-md shadow-noun-green/20">
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                        </svg>
                        Download Statement
                    </a>
                </div>

                <!-- CGPA Overview Card -->"""

if target in content:
    content = content.replace(target, replacement)
    with open('resources/js/Pages/Student/Results.vue', 'w') as f:
        f.write(content)
    print("Added button above CGPA card")
else:
    print("Target not found in Results.vue")
