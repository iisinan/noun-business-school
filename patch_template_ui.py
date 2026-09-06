file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Results/Upload.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """const templateForm = useForm({
    academic_session_id: props.sessions.length > 0 ? props.sessions[0].id : '',
    semester: 1
});"""

replace = """const templateForm = useForm({
    mode: 'single',
    course_id: '',
    academic_session_id: props.sessions.length > 0 ? props.sessions[0].id : '',
    semester: 1
});"""

content = content.replace(search, replace)

search2 = """                            <div>
                                <label class="block text-sm font-bold text-gray-700 mb-1">Semester</label>
                                <select v-model="templateForm.semester" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="i in 6" :key="i" :value="i">Semester {{ i }}</option>
                                </select>
                            </div>"""

replace2 = """                            <div v-if="templateForm.mode === 'multiple'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Semester</label>
                                <select v-model="templateForm.semester" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option v-for="i in 6" :key="i" :value="i">Semester {{ i }}</option>
                                </select>
                            </div>
                            
                            <div v-if="templateForm.mode === 'single'">
                                <label class="block text-sm font-bold text-gray-700 mb-1">Course</label>
                                <select v-model="templateForm.course_id" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50">
                                    <option value="" disabled>Select a course</option>
                                    <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.code }} - {{ course.title }}</option>
                                </select>
                            </div>"""

content = content.replace(search2, replace2)

search3 = """                    <div class="p-6 border-b border-gray-100 bg-gray-50">
                        <h3 class="text-lg font-bold text-gray-900">Step 1: Download Smart Excel Template</h3>
                        <p class="text-sm text-gray-500 mt-1">Generate a pre-filled Excel file with all registered students and their courses.</p>
                    </div>"""

replace3 = """                    <div class="p-6 border-b border-gray-100 bg-gray-50 flex items-center justify-between">
                        <div>
                            <h3 class="text-lg font-bold text-gray-900">Step 1: Download Smart Excel Template</h3>
                            <p class="text-sm text-gray-500 mt-1">Generate a pre-filled Excel file with registered students.</p>
                        </div>
                        
                        <div class="flex items-center gap-4 bg-white p-1 rounded-lg border border-gray-200 shadow-sm">
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'single' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="templateForm.mode" value="single" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Single Course</span>
                            </label>
                            <label class="flex items-center gap-2 px-3 py-1.5 cursor-pointer rounded-md transition-colors" :class="templateForm.mode === 'multiple' ? 'bg-noun-green text-white' : 'text-gray-600 hover:bg-gray-50'">
                                <input type="radio" v-model="templateForm.mode" value="multiple" class="sr-only">
                                <span class="text-sm font-bold tracking-wide">Entire Semester</span>
                            </label>
                        </div>
                    </div>"""

content = content.replace(search3, replace3)

search4 = """const downloadTemplate = () => {
    window.location.href = route('results.template', {
        academic_session_id: templateForm.academic_session_id,
        semester: templateForm.semester
    });
};"""

replace4 = """const downloadTemplate = () => {
    if (templateForm.mode === 'single' && !templateForm.course_id) {
        alert('Please select a course first.');
        return;
    }
    
    window.location.href = route('results.template', {
        mode: templateForm.mode,
        course_id: templateForm.course_id,
        academic_session_id: templateForm.academic_session_id,
        semester: templateForm.semester
    });
};"""

content = content.replace(search4, replace4)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched Upload.vue")
