file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/Registration.vue'
with open(file_path, 'r') as f:
    content = f.read()

# 1. Update computed properties to include Carry Over logic
search_computed = """const coreAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Core' || !c.type) : [];
});
const electiveAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Elective') : [];
});"""

replace_computed = """const carryOverCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.is_carry_over) : [];
});
const coreAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => (c.type === 'Core' || !c.type) && !c.is_carry_over) : [];
});
const electiveAvailableCourses = computed(() => {
    return props.availableCourses ? props.availableCourses.filter(c => c.type === 'Elective' && !c.is_carry_over) : [];
});"""

content = content.replace(search_computed, replace_computed)

# 2. Add the Carry Over UI block before Core Courses
search_html = """                            <div v-if="coreAvailableCourses.length > 0" class="mb-6">"""

replace_html = """                            <div v-if="carryOverCourses.length > 0" class="mb-6">
                                <p class="text-xs font-bold text-red-500 uppercase tracking-wider mb-3">Carry Over Courses</p>
                                <div class="space-y-2">
                                    <label
                                        v-for="course in carryOverCourses"
                                        :key="course.id"
                                        class="flex items-center gap-4 py-3 px-4 rounded-xl border cursor-pointer transition-all bg-red-50/30 border-red-200 hover:border-red-300 hover:bg-red-50/50"
                                        :class="courseForm.course_ids.includes(course.id) ? 'bg-red-50 border-red-400 shadow-sm ring-1 ring-red-400' : ''"
                                    >
                                        <input
                                            type="checkbox"
                                            :value="course.id"
                                            :checked="courseForm.course_ids.includes(course.id)"
                                            @change="toggleCourse(course.id)"
                                            class="h-4 w-4 rounded border-red-300 text-red-600 focus:ring-red-500"
                                        />
                                        <div class="flex-1 min-w-0">
                                            <div class="flex items-center gap-2">
                                                <span class="text-sm font-bold text-gray-800">{{ course.code }}</span>
                                                <span class="px-1.5 py-0.5 text-[10px] font-bold rounded uppercase tracking-wider bg-red-100 text-red-700">CO</span>
                                                <span class="hidden sm:inline text-sm text-gray-500 truncate">— {{ course.title }}</span>
                                            </div>
                                            <span class="sm:hidden text-xs text-gray-500 block mt-0.5 truncate">{{ course.title }}</span>
                                        </div>
                                        <div class="flex items-center gap-3 flex-shrink-0">
                                            <span class="text-xs text-gray-400 bg-white px-2 py-1 rounded-md border font-medium">{{ course.units }} cr</span>
                                            <span class="text-sm font-bold text-gray-900">₦{{ courseCost(course).toLocaleString() }}</span>
                                        </div>
                                    </label>
                                </div>
                            </div>

                            <div v-if="coreAvailableCourses.length > 0" class="mb-6">"""

content = content.replace(search_html, replace_html)

with open(file_path, 'w') as f:
    f.write(content)

print("Patched Registration.vue for Carry Over courses")
