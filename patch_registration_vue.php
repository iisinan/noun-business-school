<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/Registration.vue';
$content = file_get_contents($file);

$searchScript = <<<VUE
const props = defineProps({
    application: Object,
    hasRegisteredSemester: Boolean,
    availableCourses: Array,
    registeredCourses: Array,
});
VUE;

$replaceScript = <<<VUE
const props = defineProps({
    application: Object,
    hasRegisteredSemester: Boolean,
    availableCourses: Array,
    registeredCourses: Array,
    registrationOpen: Boolean,
});
VUE;

$content = str_replace($searchScript, $replaceScript, $content);

$searchTemplate = <<<VUE
    <StudentLayout>
        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8 space-y-6">
VUE;

$replaceTemplate = <<<VUE
    <StudentLayout>
        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8 space-y-6">
                
                <div v-if="!registrationOpen" class="bg-red-50 border-l-4 border-red-500 p-4 rounded-r-xl">
                    <div class="flex">
                        <div class="flex-shrink-0">
                            <svg class="h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                            </svg>
                        </div>
                        <div class="ml-3">
                            <h3 class="text-sm font-medium text-red-800">Registration Closed</h3>
                            <div class="mt-1 text-sm text-red-700">
                                Registration for the current semester has been closed by the administration. You cannot register for the semester or add new courses at this time.
                            </div>
                        </div>
                    </div>
                </div>
VUE;

$content = str_replace($searchTemplate, $replaceTemplate, $content);

$searchBtnSem = <<<VUE
                        <button @click="registerSemester" :disabled="form.processing" class="bg-noun-green text-white px-6 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm disabled:opacity-50">
                            Pay ₦25,000 & Register
                        </button>
VUE;

$replaceBtnSem = <<<VUE
                        <button @click="registerSemester" :disabled="form.processing || !registrationOpen" class="bg-noun-green text-white px-6 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm disabled:opacity-50">
                            Pay ₦25,000 & Register
                        </button>
VUE;

$content = str_replace($searchBtnSem, $replaceBtnSem, $content);

$searchBtnCourses = <<<VUE
                            <button @click="registerCourses" :disabled="form.processing || selectedCourses.length === 0" class="bg-noun-green text-white px-6 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm disabled:opacity-50 flex items-center gap-2">
                                Pay ₦{{ (selectedCourses.length * 5000).toLocaleString() }} & Register Courses
                            </button>
VUE;

$replaceBtnCourses = <<<VUE
                            <button @click="registerCourses" :disabled="form.processing || selectedCourses.length === 0 || !registrationOpen" class="bg-noun-green text-white px-6 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm disabled:opacity-50 flex items-center gap-2">
                                Pay ₦{{ (selectedCourses.length * 5000).toLocaleString() }} & Register Courses
                            </button>
VUE;

$content = str_replace($searchBtnCourses, $replaceBtnCourses, $content);

file_put_contents($file, $content);
echo "Patched Registration.vue\n";
