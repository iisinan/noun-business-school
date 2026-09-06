with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

target = """                            <button
                                @click="registerSemester"
                                :disabled="semesterForm.processing || (wallet_balance ?? 0) < 35000"
                                class="flex-shrink-0 inline-flex items-center gap-2 px-4 py-2 bg-emerald-600 text-white font-bold text-xs rounded-lg hover:bg-emerald-700 transition shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
                                title="Advance to the next semester"
                            >
                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                {{ semesterForm.processing ? 'Processing…' : 'Pay for Semester ' + (studentSemester + 1) }}
                            </button>"""

if target in content:
    content = content.replace(target, '')
    with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
        f.write(content)
    print("Button removed!")
else:
    print("Target not found!")
