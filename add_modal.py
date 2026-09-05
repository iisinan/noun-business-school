import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

modal_html = """
        <!-- Validation Error Modal -->
        <div v-if="validationErrors.length > 0" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-900/50 backdrop-blur-sm">
            <div class="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden transform transition-all">
                <div class="bg-red-50 px-6 py-4 border-b border-red-100 flex items-center gap-3">
                    <svg class="h-6 w-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                    <h3 class="text-lg font-bold text-red-800">Missing Information</h3>
                </div>
                <div class="p-6">
                    <ul class="list-disc list-inside text-sm text-gray-700 space-y-1">
                        <li v-for="(err, i) in validationErrors" :key="i">{{ err }}</li>
                    </ul>
                    <div class="mt-6 flex justify-end">
                        <button @click="validationErrors = []" class="px-5 py-2 bg-red-600 hover:bg-red-700 text-white text-sm font-semibold rounded-lg transition-colors shadow-sm focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                            Got it
                        </button>
                    </div>
                </div>
            </div>
        </div>
"""

# Insert right after <template> and before the main div
content = re.sub(r'<template>\s*<AuthenticatedLayout>', '<template>\n    <AuthenticatedLayout>\n' + modal_html, content)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

