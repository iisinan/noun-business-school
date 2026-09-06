import sys

# 1. Update Controller
with open('app/Http/Controllers/Admin/SpecialisationController.php', 'r') as f:
    controller_content = f.read()

target_controller = """    public function show(Specialisation $specialisation)
    {
        $specialisation->load('programme', 'courses');
        $allCourses = Course::orderBy('code')->get();
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'allCourses' => $allCourses
        ]);
    }"""

replacement_controller = """    public function show(Specialisation $specialisation)
    {
        $specialisation->load(['programme.courses', 'courses']);
        $allCourses = Course::orderBy('code')->get();
        
        $visibleCourses = $specialisation->programme->courses->merge($specialisation->courses)->unique('id')->sortBy('code')->values();
        
        $programmeCourses = $visibleCourses->map(function($course) use ($specialisation) {
            $specialisationCourse = $specialisation->courses->where('id', $course->id)->first();
            $course->is_attached = $specialisationCourse ? true : false;
            $course->is_elective = $specialisationCourse ? (bool) $specialisationCourse->pivot->is_elective : false;
            return $course;
        });
        
        return Inertia::render('Admin/Specialisations/Show', [
            'specialisation' => $specialisation,
            'programmeCourses' => $programmeCourses,
            'allCourses' => $allCourses
        ]);
    }"""

if target_controller in controller_content:
    controller_content = controller_content.replace(target_controller, replacement_controller)
    with open('app/Http/Controllers/Admin/SpecialisationController.php', 'w') as f:
        f.write(controller_content)
    print("Patched SpecialisationController")
else:
    print("Target not found in SpecialisationController")
    sys.exit(1)

# 2. Update Vue Component
with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'r') as f:
    vue_content = f.read()

# Add programmeCourses to props
vue_content = vue_content.replace('allCourses: Array', 'allCourses: Array,\n    programmeCourses: Array')

# Add inline attach functions
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
vue_content = vue_content.replace('const isAttachModalOpen = ref(false);', script_addition + '\nconst isAttachModalOpen = ref(false);')

# Replace table body
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
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No courses assigned to the parent Programme yet.</td>
                            </tr>
                        </tbody>"""

if target_table in vue_content:
    vue_content = vue_content.replace(target_table, replacement_table)
    with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'w') as f:
        f.write(vue_content)
    print("Patched Show.vue")
else:
    print("Target table not found in Show.vue")
    sys.exit(1)
