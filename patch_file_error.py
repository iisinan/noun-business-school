import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Add ref
target_ref = "const submitLoader = ref({ active: false, text: '' });"
replacement_ref = """const submitLoader = ref({ active: false, text: '' });
const fileError = ref(null);"""
content = content.replace(target_ref, replacement_ref)

# Update handlePassportUpload
target_passport = """        if (file.size > 2 * 1024 * 1024) {
            alert('Passport photograph must be less than 2MB.');
            e.target.value = '';
            return;
        }"""
replacement_passport = """        if (file.size > 2 * 1024 * 1024) {
            fileError.value = 'Passport photograph must be less than 2MB.';
            e.target.value = '';
            return;
        }"""
content = content.replace(target_passport, replacement_passport)

# Update handleFileSelect
target_select = """        if (file.size > 5 * 1024 * 1024) {
            alert(`The file "${file.name}" is too large. Please select a file smaller than 5MB.`);
            e.target.value = '';
            return;
        }"""
replacement_select = """        if (file.size > 5 * 1024 * 1024) {
            fileError.value = `The file "${file.name}" is too large. Please select a file smaller than 5MB.`;
            e.target.value = '';
            return;
        }"""
content = content.replace(target_select, replacement_select)

# Add HTML Modal
target_html = "        <!-- Validation Error Modal -->"
replacement_html = """        <!-- File Error Modal -->
        <Transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="opacity-0 scale-95"
            enter-to-class="opacity-100 scale-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="opacity-100 scale-100"
            leave-to-class="opacity-0 scale-95"
        >
            <div v-if="fileError" class="fixed inset-0 z-[80] flex items-center justify-center p-4 bg-gray-900/60 backdrop-blur-sm">
                <div class="bg-white rounded-3xl shadow-2xl w-full max-w-sm overflow-hidden transform transition-all border border-red-100">
                    <div class="bg-red-50 px-6 py-6 border-b border-red-100 flex flex-col items-center text-center">
                        <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mb-4 shadow-sm border border-red-200">
                            <svg class="h-8 w-8 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                            </svg>
                        </div>
                        <h3 class="text-xl font-black text-red-800 tracking-tight">File Too Large</h3>
                    </div>
                    <div class="p-6 text-center">
                        <p class="text-sm text-gray-600 font-medium leading-relaxed">{{ fileError }}</p>
                        <div class="mt-8">
                            <button @click="fileError = null" class="w-full px-5 py-3 bg-red-600 hover:bg-red-700 text-white text-sm font-bold rounded-xl transition-colors shadow-md focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                                Try Again
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </Transition>

        <!-- Validation Error Modal -->"""
content = content.replace(target_html, replacement_html)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
