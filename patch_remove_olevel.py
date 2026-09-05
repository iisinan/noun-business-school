with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Add removeOlevel function
target_script = """const addOlevel = () => {
    if(form.olevel_results.length < 2) {
        form.olevel_results.push({ exam_type: '', exam_year: '', exam_number: '', sitting: 2, subjects: [{name: 'English Language', grade: ''}, {name: 'Mathematics', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}] });
    }
};"""

replacement_script = """const addOlevel = () => {
    if(form.olevel_results.length < 2) {
        form.olevel_results.push({ exam_type: '', exam_year: '', exam_number: '', sitting: 2, subjects: [{name: 'English Language', grade: ''}, {name: 'Mathematics', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}] });
    }
};

const removeOlevel = (index) => {
    form.olevel_results.splice(index, 1);
};"""

content = content.replace(target_script, replacement_script)

# Add remove button to template
target_template = """                                <div v-for="(olevel, index) in form.olevel_results" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl mb-4">
                                    <h4 class="font-medium text-gray-800 mb-4">Sitting #{{ olevel.sitting }}</h4>
                                    <div class="grid grid-cols-3 gap-4 mb-5">"""

replacement_template = """                                <div v-for="(olevel, index) in form.olevel_results" :key="index" class="bg-gray-50 p-5 border border-gray-200 rounded-xl mb-4 relative">
                                    <div class="flex items-center justify-between mb-4">
                                        <h4 class="font-medium text-gray-800">Sitting #{{ olevel.sitting }}</h4>
                                        <button v-if="index > 0" type="button" @click="removeOlevel(index)" class="text-xs text-red-500 hover:text-red-700 font-bold flex items-center gap-1 transition">
                                            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                            Remove Sitting
                                        </button>
                                    </div>
                                    <div class="grid grid-cols-3 gap-4 mb-5">"""

content = content.replace(target_template, replacement_template)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
