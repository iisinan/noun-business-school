import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Update handlePassportUpload for timeout
target_passport = """        if (file.size > 2 * 1024 * 1024) {
            fileError.value = 'Passport photograph must be less than 2MB.';
            e.target.value = '';
            return;
        }"""
replacement_passport = """        if (file.size > 2 * 1024 * 1024) {
            fileError.value = 'Passport photograph must be less than 2MB.';
            setTimeout(() => { fileError.value = null; }, 6000);
            e.target.value = '';
            return;
        }"""
content = content.replace(target_passport, replacement_passport)

# Update handleFileSelect for timeout
target_select = """        if (file.size > 5 * 1024 * 1024) {
            fileError.value = `The file "${file.name}" is too large. Please select a file smaller than 5MB.`;
            e.target.value = '';
            return;
        }"""
replacement_select = """        if (file.size > 5 * 1024 * 1024) {
            fileError.value = `The file "${file.name}" is too large. Please select a file smaller than 5MB.`;
            setTimeout(() => { fileError.value = null; }, 6000);
            e.target.value = '';
            return;
        }"""
content = content.replace(target_select, replacement_select)

# Auto close validation errors
target_validation = """    // Validate Employment Info (if required)"""
replacement_validation = """    if (validationErrors.value.length > 0) {
        setTimeout(() => { validationErrors.value = []; }, 8000);
    }
    // Validate Employment Info (if required)"""
content = content.replace(target_validation, replacement_validation)


# Replace BOTH Modals with Toasts
target_html_start = "        <!-- File Error Modal -->"
target_html_end = "        </Transition>" # I need to be careful with regex here, let's just do a big regex replacement for the whole block of both modals.

# Since regex across multiple lines is tricky in python without re.DOTALL, let's use string splitting.
parts = content.split("        <!-- File Error Modal -->")
if len(parts) == 2:
    top_part = parts[0]
    bottom_part = parts[1].split("<!-- End of Modals -->") # Wait, I didn't add "End of Modals".
    
    # Let's find where the validation error modal ends. It ends right before:
    # <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    bottom_parts = parts[1].split('        <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">')
    
    if len(bottom_parts) == 2:
        new_html = """        <!-- Toasts Container -->
        <div class="fixed top-6 right-6 z-[100] flex flex-col gap-4 items-end pointer-events-none">
            
            <!-- File Error Toast -->
            <Transition
                enter-active-class="transform ease-out duration-300 transition"
                enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-full"
                enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
                leave-active-class="transition ease-in duration-200"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
            >
                <div v-if="fileError" class="pointer-events-auto w-full max-w-sm overflow-hidden bg-white rounded-2xl shadow-2xl ring-1 ring-black ring-opacity-5">
                    <div class="p-5">
                        <div class="flex items-start">
                            <div class="flex-shrink-0">
                                <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center">
                                    <svg class="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                    </svg>
                                </div>
                            </div>
                            <div class="ml-4 w-0 flex-1 pt-1">
                                <p class="text-sm font-black text-gray-900 tracking-tight">File Too Large</p>
                                <p class="mt-1 text-sm text-gray-500 font-medium leading-relaxed">{{ fileError }}</p>
                            </div>
                            <div class="ml-4 flex-shrink-0 flex">
                                <button @click="fileError = null" class="bg-white rounded-md inline-flex text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-colors">
                                    <span class="sr-only">Close</span>
                                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </Transition>

            <!-- Validation Errors Toast -->
            <Transition
                enter-active-class="transform ease-out duration-300 transition"
                enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-full"
                enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
                leave-active-class="transition ease-in duration-200"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
            >
                <div v-if="validationErrors.length > 0" class="pointer-events-auto w-full max-w-sm overflow-hidden bg-white rounded-2xl shadow-2xl ring-1 ring-black ring-opacity-5">
                    <div class="p-5">
                        <div class="flex items-start">
                            <div class="flex-shrink-0">
                                <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center">
                                    <svg class="h-5 w-5 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                    </svg>
                                </div>
                            </div>
                            <div class="ml-4 w-0 flex-1 pt-1">
                                <p class="text-sm font-black text-gray-900 tracking-tight">Missing Information</p>
                                <ul class="mt-2 text-sm text-gray-500 font-medium list-disc list-inside space-y-1">
                                    <li v-for="(err, i) in validationErrors" :key="i">{{ err }}</li>
                                </ul>
                            </div>
                            <div class="ml-4 flex-shrink-0 flex">
                                <button @click="validationErrors = []" class="bg-white rounded-md inline-flex text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500 transition-colors">
                                    <span class="sr-only">Close</span>
                                    <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </Transition>
        </div>

        <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">"""
        
        content = top_part + new_html + bottom_parts[1]
        
        with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
            f.write(content)
