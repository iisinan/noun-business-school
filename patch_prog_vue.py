import sys

with open('resources/js/Pages/Admin/Programmes/Show.vue', 'r') as f:
    content = f.read()

# Replace script
target_script = """const isAttachModalOpen = ref(false);

const attachForm = useForm({
    course_id: ''
});

const submitAttach = () => {
    attachForm.post(route('admin.programmes.courses.attach', props.programme.id), {
        onSuccess: () => {
            isAttachModalOpen.value = false;
            attachForm.reset();
        }
    });
};"""

replacement_script = """const attachCourse = (courseId) => {
    useForm({ course_id: courseId }).post(route('admin.programmes.courses.attach', props.programme.id), { preserveScroll: true });
};"""

if target_script in content:
    content = content.replace(target_script, replacement_script)
else:
    print("Script target not found")
    sys.exit(1)

# Replace the table rendering
target_table = """                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in programme.courses" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span v-if="course.type" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-600'">{{ course.type }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-blue-50 text-blue-700 mr-1">{{ course.level }}L</span>
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-green-50 text-green-700">S{{ course.semester }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                </td>
                            </tr>
                            <tr v-if="!programme.courses || programme.courses.length === 0">
                                <td colspan="6" class="px-6 py-12 text-center text-sm text-gray-400">No courses attached to this programme yet.</td>
                            </tr>
                        </tbody>"""

replacement_table = """                        <tbody class="bg-white divide-y divide-gray-50">
                            <tr v-for="course in allCourses" :key="course.id" class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">{{ course.code }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ course.title }}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span v-if="course.type" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.type === 'Core' ? 'bg-indigo-100 text-indigo-700' : 'bg-gray-100 text-gray-600'">{{ course.type }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-blue-50 text-blue-700 mr-1">{{ course.level }}L</span>
                                    <span class="px-2 py-1 text-xs font-semibold rounded bg-green-50 text-green-700">S{{ course.semester }}</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                    <div v-if="course.is_attached">
                                        <button @click="detachCourse(course.id)" class="text-red-500 hover:text-red-700 font-semibold transition">Remove</button>
                                    </div>
                                    <div v-else>
                                        <button @click="attachCourse(course.id)" class="text-noun-green hover:text-noun-dark font-semibold transition">Add to Programme</button>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="!allCourses || allCourses.length === 0">
                                <td colspan="6" class="px-6 py-12 text-center text-sm text-gray-400">No courses available in the system.</td>
                            </tr>
                        </tbody>"""

if target_table in content:
    content = content.replace(target_table, replacement_table)
else:
    print("Table target not found")
    sys.exit(1)

# Remove the Attach Course button from the header
target_btn = """                        <button @click="isAttachModalOpen = true" class="inline-flex items-center gap-2 bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                            Attach Course
                        </button>"""
if target_btn in content:
    content = content.replace(target_btn, '')

# Also remove the whole modal block if possible
import re
content = re.sub(r'<!-- Attach Course Modal -->.*?</Modal>', '', content, flags=re.DOTALL)

with open('resources/js/Pages/Admin/Programmes/Show.vue', 'w') as f:
    f.write(content)

print("Programme Show.vue patched!")
