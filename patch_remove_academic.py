with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Add removeAcademic function
target_script = """const addAcademic = () => {
    form.academic_background.push({ institution: '', qualification: '', course_of_study: '', graduation_year: '', grade: '' });
};"""

replacement_script = """const addAcademic = () => {
    form.academic_background.push({ institution: '', qualification: '', course_of_study: '', graduation_year: '', grade: '' });
};

const removeAcademic = (index) => {
    form.academic_background.splice(index, 1);
};"""

content = content.replace(target_script, replacement_script)

# Add remove button to template
target_template = """                            <div v-for="(academic, index) in form.academic_background" :key="index" class="bg-gray-50 p-5 rounded-xl border border-gray-200 mb-4">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

replacement_template = """                            <div v-for="(academic, index) in form.academic_background" :key="index" class="bg-gray-50 p-5 rounded-xl border border-gray-200 mb-4 relative">
                                <button v-if="index > 0" type="button" @click="removeAcademic(index)" class="absolute top-4 right-4 text-xs text-red-500 hover:text-red-700 font-bold flex items-center gap-1 transition">
                                    <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                    Remove
                                </button>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">"""

content = content.replace(target_template, replacement_template)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
