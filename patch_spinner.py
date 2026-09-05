with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = """        <!-- Submit Loader Modal -->
        <div v-if="submitLoader.active" class="fixed inset-0 z-[60] flex items-center justify-center p-4 bg-gray-900/60 backdrop-blur-sm transition-opacity">
            <div class="bg-white rounded-2xl shadow-2xl w-full max-w-sm p-8 text-center transform transition-all flex flex-col items-center">
                <div v-if="submitLoader.text !== 'Submission complete!'" class="relative w-16 h-16 mb-6">
                    <div class="absolute inset-0 border-4 border-gray-100 rounded-full"></div>
                    <div class="absolute inset-0 border-4 border-noun-green rounded-full border-t-transparent animate-spin"></div>
                </div>
                <div v-else class="w-16 h-16 mb-6 bg-green-100 rounded-full flex items-center justify-center">
                    <svg class="w-8 h-8 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" /></svg>
                </div>
                <h3 class="text-lg font-bold text-gray-900 mb-2">{{ submitLoader.text }}</h3>
                <p v-if="submitLoader.text !== 'Submission complete!'" class="text-sm text-gray-500">Please do not close or refresh this page.</p>
                <p v-else class="text-sm text-gray-500">Redirecting you to dashboard...</p>
            </div>
        </div>"""

replacement = """        <!-- Submit Loader Modal -->
        <Transition
            enter-active-class="transition duration-300 ease-out"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="transition duration-200 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
        >
            <div v-if="submitLoader.active" class="fixed inset-0 z-[70] flex items-center justify-center p-4 bg-gray-900/70 backdrop-blur-md">
                <div class="bg-white rounded-3xl shadow-2xl w-full max-w-sm p-10 text-center transform transition-all flex flex-col items-center">
                    
                    <div class="relative w-20 h-20 mb-6">
                        <Transition
                            enter-active-class="transition duration-500 ease-out absolute inset-0"
                            enter-from-class="opacity-0 scale-50 rotate-90"
                            enter-to-class="opacity-100 scale-100 rotate-0"
                            leave-active-class="transition duration-300 ease-in absolute inset-0"
                            leave-from-class="opacity-100 scale-100 rotate-0"
                            leave-to-class="opacity-0 scale-50 -rotate-90"
                        >
                            <div v-if="submitLoader.text !== 'Submission complete!'" class="absolute inset-0">
                                <!-- Pulsing logo inside -->
                                <div class="absolute inset-0 flex items-center justify-center animate-pulse">
                                    <img src="/nbs-logo.png" class="w-10 h-10 object-contain opacity-80" />
                                </div>
                                <!-- Spinning ring -->
                                <div class="absolute inset-0 border-[4px] border-gray-100 rounded-full"></div>
                                <div class="absolute inset-0 border-[4px] border-noun-green rounded-full border-t-transparent border-r-transparent animate-spin" style="animation-duration: 1s;"></div>
                            </div>
                            <div v-else class="absolute inset-0 bg-green-100 rounded-full flex items-center justify-center shadow-inner">
                                <svg class="w-10 h-10 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3.5" d="M5 13l4 4L19 7" /></svg>
                            </div>
                        </Transition>
                    </div>

                    <h3 class="text-xl font-black text-gray-900 mb-2 tracking-tight">{{ submitLoader.text }}</h3>
                    <p v-if="submitLoader.text !== 'Submission complete!'" class="text-sm text-gray-500 font-medium">Please do not close or refresh this page.</p>
                    <p v-else class="text-sm text-gray-500 font-medium">Redirecting you to dashboard...</p>
                </div>
            </div>
        </Transition>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
