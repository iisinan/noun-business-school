import re

with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

target = """                            <div class="flex items-center justify-between mb-3">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Registered Courses</p>
                                <span class="text-xs font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-md">{{ totalRegisteredCredits }} Units Total</span>
                            </div>"""

replacement = """                            <div class="flex items-center justify-between mb-3">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Registered Courses</p>
                                <span class="text-xs font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-md">{{ totalRegisteredCredits }} / {{ MAX_CREDITS }} Units</span>
                            </div>
                            
                            <!-- Credit Progress Bar -->
                            <div class="w-full bg-gray-200 rounded-full h-1.5 mb-4 overflow-hidden flex">
                                <div class="bg-noun-green h-1.5 transition-all" :style="{ width: Math.min((totalRegisteredCredits / MAX_CREDITS) * 100, 100) + '%' }"></div>
                                <div class="bg-noun-yellow h-1.5 transition-all opacity-70" :style="{ width: Math.min((totalSelectedCredits / MAX_CREDITS) * 100, 100 - ((totalRegisteredCredits / MAX_CREDITS) * 100)) + '%' }"></div>
                            </div>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)

