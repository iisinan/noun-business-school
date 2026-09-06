import re

file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/Registration.vue'
with open(file_path, 'r') as f:
    content = f.read()

# Add computed properties for grouped courses
script_setup_block = """const calculateSelectedCost = computed(() => {"""
new_computed_block = """
const coreAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Core' || !c.type) : [];
});
const electiveAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Elective') : [];
});

const calculateSelectedCost = computed(() => {"""
content = content.replace(script_setup_block, new_computed_block)

# Replace the available courses block
html_block_old = """                        <!-- Available courses to register -->
                        <div v-if="availableCourses && availableCourses.length > 0">
                            <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Available Courses</p>
                            <div class="space-y-2">
                                <label
                                    v-for="course in availableCourses"
                                    :key="course.id"
                                    class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all"
                                    :class="courseForm.course_ids.includes(course.id)
                                        ? 'bg-blue-50 border-blue-300 shadow-sm'
                                        : 'bg-white border-gray-200 hover:border-blue-200 hover:bg-blue-50/50'"
                                >
                                    <input
                                        type="checkbox"
                                        :value="course.id"
                                        :checked="courseForm.course_ids.includes(course.id)"
                                        @change="toggleCourse(course.id)"
                                        class="h-4 w-4 rounded border-gray-300 text-noun-green focus:ring-noun-green"
                                    />
                                    <div class="flex-1 min-w-0">
                                        <div class="flex items-center gap-2">
                                            <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                            <span 
                                                v-if="course.type" 
                                                class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider" 
                                                :class="course.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-600'"
                                            >
                                                {{ course.type }}
                                            </span>
                                            <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                        </div>
                                        <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                    </div>
                                    <div class="flex items-center gap-3 flex-shrink-0">
                                        <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded-md font-medium">{{ course.units }} cr</span>
                                        <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                    </div>
                                </label>
                            </div>"""

html_block_new = """                        <!-- Available courses to register -->
                        <div v-if="availableCourses && availableCourses.length > 0">
                            
                            <div v-if="coreAvailableCourses.length > 0" class="mb-6">
                                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Core Courses</p>
                                <div class="space-y-2">
                                    <label
                                        v-for="course in coreAvailableCourses"
                                        :key="course.id"
                                        class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all"
                                        :class="courseForm.course_ids.includes(course.id)
                                            ? 'bg-blue-50 border-blue-300 shadow-sm'
                                            : 'bg-white border-gray-200 hover:border-blue-200 hover:bg-blue-50/50'"
                                    >
                                        <input
                                            type="checkbox"
                                            :value="course.id"
                                            :checked="courseForm.course_ids.includes(course.id)"
                                            @change="toggleCourse(course.id)"
                                            class="h-4 w-4 rounded border-gray-300 text-noun-green focus:ring-noun-green"
                                        />
                                        <div class="flex-1 min-w-0">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider bg-indigo-100 text-indigo-700">CORE</span>
                                                <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                            </div>
                                            <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                        </div>
                                        <div class="flex items-center gap-3 flex-shrink-0">
                                            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded-md font-medium">{{ course.units }} cr</span>
                                            <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <div v-if="electiveAvailableCourses.length > 0" class="mb-6">
                                <div class="flex items-center justify-between mb-3">
                                    <p class="text-xs font-bold text-gray-400 uppercase tracking-wider">Elective Courses</p>
                                    <p class="text-[10px] font-bold text-amber-500 uppercase tracking-wider bg-amber-50 px-2 py-0.5 rounded-full border border-amber-100">Choose Two</p>
                                </div>
                                <div class="space-y-2">
                                    <label
                                        v-for="course in electiveAvailableCourses"
                                        :key="course.id"
                                        class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all"
                                        :class="courseForm.course_ids.includes(course.id)
                                            ? 'bg-blue-50 border-blue-300 shadow-sm'
                                            : 'bg-white border-gray-200 hover:border-blue-200 hover:bg-blue-50/50'"
                                    >
                                        <input
                                            type="checkbox"
                                            :value="course.id"
                                            :checked="courseForm.course_ids.includes(course.id)"
                                            @change="toggleCourse(course.id)"
                                            class="h-4 w-4 rounded border-gray-300 text-noun-green focus:ring-noun-green"
                                        />
                                        <div class="flex-1 min-w-0">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider bg-amber-100 text-amber-700">ELECTIVE</span>
                                                <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                            </div>
                                            <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                        </div>
                                        <div class="flex items-center gap-3 flex-shrink-0">
                                            <span class="text-xs text-gray-400 bg-gray-100 px-2 py-1 rounded-md font-medium">{{ course.units }} cr</span>
                                            <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                        </div>
                                    </label>
                                </div>
                            </div>"""

if html_block_old in content:
    content = content.replace(html_block_old, html_block_new)
    print("Patched Registration.vue")
else:
    print("Could not find HTML block!")

with open(file_path, 'w') as f:
    f.write(content)

