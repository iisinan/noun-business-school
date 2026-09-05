with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = """                            <div v-for="(edu, index) in form.academic_background" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl">
                                <h4 class="font-semibold text-gray-900 mb-4">Qualification #{{ index + 1 }}</h4>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

replacement = """                            <div v-for="(edu, index) in form.academic_background" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl">
                                <div class="flex justify-between items-center mb-4">
                                    <h4 class="font-semibold text-gray-900">Qualification #{{ index + 1 }}</h4>
                                    <button v-if="index > 0" type="button" @click="removeAcademic(index)" class="text-xs text-red-500 hover:text-red-700 font-bold flex items-center gap-1 transition">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                        Remove Qualification
                                    </button>
                                </div>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
