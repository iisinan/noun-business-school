import re

with open('resources/js/Pages/Applicant/Dashboard.vue', 'r') as f:
    content = f.read()

# Replace the vertical tracker block
# We want to replace everything from `<!-- Tracker Visual -->` up to `<!-- Application Details -->` (which is at the start of lg:col-span-2)
pattern = r'<!-- Tracker Visual -->.*?<div class="lg:col-span-2 space-y-6">'
replacement = """<!-- Horizontal Tracker Visual -->
                    <div class="lg:col-span-3">
                        <div class="bg-[#fdf5e6] rounded-xl border border-orange-200 p-6 shadow-sm mb-2">
                            <div class="flex items-start gap-4 mb-6">
                                <div class="flex-shrink-0 w-12 h-12 bg-orange-100 rounded-full border border-orange-200 flex items-center justify-center text-orange-500">
                                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                </div>
                                <div>
                                    <div class="flex items-center gap-3">
                                        <h3 class="text-xl font-bold text-orange-600">Application Under Review</h3>
                                        <span class="px-2.5 py-0.5 rounded-full bg-orange-200 text-orange-800 text-xs font-bold tracking-wide">SUBMITTED</span>
                                    </div>
                                    <p class="text-sm text-gray-500 mt-1">Your registration has been submitted and is pending verification.</p>
                                </div>
                            </div>
                            
                            <div class="relative max-w-3xl pt-4 mx-auto hidden md:block">
                                <div class="absolute top-[18px] left-[10%] right-[10%] h-0.5 bg-gray-200">
                                    <div class="h-full bg-green-500 transition-all duration-500" :style="{ width: ((currentStep - 1) / (steps.length - 1)) * 100 + '%' }"></div>
                                </div>
                                <ul class="relative flex justify-between">
                                    <li v-for="step in steps" :key="step.id" class="flex flex-col items-center group relative z-10 text-center w-24">
                                        <div class="w-10 h-10 rounded-full border-2 bg-white flex items-center justify-center mb-2 transition-colors duration-200"
                                            :class="[
                                                currentStep > step.id ? 'border-green-500' : 
                                                currentStep === step.id ? 'border-orange-400 text-orange-500' : 
                                                'border-gray-300 text-gray-400'
                                            ]">
                                            <svg v-if="currentStep > step.id" class="w-5 h-5 text-green-500" viewBox="0 0 20 20" fill="currentColor">
                                                <path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 01.143 1.052l-8 10.5a.75.75 0 01-1.127.075l-4.5-4.5a.75.75 0 011.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 011.05-.143z" clip-rule="evenodd" />
                                            </svg>
                                            <svg v-else-if="currentStep === step.id" class="w-5 h-5 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                                            <span v-else class="text-sm font-semibold">{{ step.id }}</span>
                                        </div>
                                        <span class="text-xs font-semibold" :class="currentStep >= step.id ? 'text-gray-900' : 'text-gray-500'">{{ step.name }}</span>
                                        <span class="text-[10px] text-gray-500 mt-0.5 leading-tight">{{ step.description }}</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="lg:col-span-3 space-y-6">"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
with open('resources/js/Pages/Applicant/Dashboard.vue', 'w') as f:
    f.write(new_content)
