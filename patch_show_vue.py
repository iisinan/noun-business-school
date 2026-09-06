with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'r') as f:
    content = f.read()

# Replace props
content = content.replace('allCourses: Array', 'programmeCourses: Array')

# We don't need the modal anymore, we can just use inline functions to attach core/elective
script_addition = """
const attachCore = (courseId) => {
    useForm({
        course_id: courseId,
        is_elective: false
    }).post(route('admin.specialisations.courses.attach', props.specialisation.id), { preserveScroll: true });
};

const attachElective = (courseId) => {
    useForm({
        course_id: courseId,
        is_elective: true
    }).post(route('admin.specialisations.courses.attach', props.specialisation.id), { preserveScroll: true });
};
"""

content = content.replace('const isAttachModalOpen = ref(false);', script_addition + '\nconst isAttachModalOpen = ref(false);')

# Replace the table rendering
target_table = """                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in specialisation.courses" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.pivot.is_elective ? 'bg-gray-100 text-gray-600' : 'bg-indigo-100 text-indigo-700'">
                                        {{ course.pivot.is_elective ? 'Elective' : 'Core' }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                </td>
                            </tr>
                            <tr v-if="!specialisation.courses || specialisation.courses.length === 0">
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No courses attached to this track yet.</td>
                            </tr>
                        </tbody>"""

replacement_table = """                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in programmeCourses" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span v-if="course.is_attached" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.is_elective ? 'bg-gray-100 text-gray-600' : 'bg-indigo-100 text-indigo-700'">
                                        {{ course.is_elective ? 'Elective' : 'Core' }}
                                    </span>
                                    <span v-else class="text-xs text-gray-400 font-medium italic">Not in Track</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <div v-if="course.is_attached">
                                        <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                    </div>
                                    <div v-else class="flex justify-end gap-3">
                                        <button @click="attachCore(course.id)" class="text-noun-green hover:text-noun-dark font-semibold transition">Add Core</button>
                                        <button @click="attachElective(course.id)" class="text-gray-500 hover:text-gray-700 font-semibold transition">Add Elective</button>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="!programmeCourses || programmeCourses.length === 0">
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No courses available in this programme to attach.</td>
                            </tr>
                        </tbody>"""

content = content.replace(target_table, replacement_table)

# Remove the Attach Course button from the header
target_btn = """                        <button @click="isAttachModalOpen = true" class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                            Attach Course
                        </button>"""
content = content.replace(target_btn, '')

with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'w') as f:
    f.write(content)

print("Show.vue patched!")
