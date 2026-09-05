import re

with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

# Fix the course title on desktop
target_title = """<p class="text-sm font-bold text-gray-900 truncate">{{ course.code }}</p>
                                        <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>"""

replacement_title = """<p class="text-sm font-bold text-gray-900 truncate">{{ course.code }}</p>
                                        <span class="text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>"""

content = content.replace(target_title, replacement_title)

# Display total registered units
target_registered = """<p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Registered Courses</p>"""
replacement_registered = """<div class="flex items-center justify-between mb-3">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Registered Courses</p>
                                <span class="text-xs font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-md">{{ totalRegisteredCredits }} Units Total</span>
                            </div>"""

content = content.replace(target_registered, replacement_registered)

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)
