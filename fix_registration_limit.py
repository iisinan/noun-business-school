import re

with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

# Add max credits limit
target_script = """const totalRegisteredCredits = computed(() =>
    props.registeredCourses?.reduce((sum, c) => sum + c.units, 0) ?? 0
);"""

replacement_script = """const totalRegisteredCredits = computed(() =>
    props.registeredCourses?.reduce((sum, c) => sum + c.units, 0) ?? 0
);

const MAX_CREDITS = 24;

const totalSelectedCredits = computed(() => {
    let sum = 0;
    courseForm.course_ids.forEach(id => {
        const course = props.availableCourses.find(c => c.id === id);
        if (course) sum += course.units;
    });
    return sum;
});

const canRegisterMore = computed(() => {
    return (totalRegisteredCredits.value + totalSelectedCredits.value) <= MAX_CREDITS;
});
"""

content = content.replace(target_script, replacement_script)

target_total = """<p class="text-green-300 text-xs font-semibold uppercase tracking-wider">Selection Total</p>
                                    <p class="text-white font-black text-xl mt-0.5">₦{{ calculateSelectedCost.toLocaleString() }}</p>
                                    <p v-if="!canAffordSelection && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        Exceeds balance by ₦{{ (calculateSelectedCost - wallet_balance).toLocaleString() }}
                                    </p>"""

replacement_total = """<p class="text-green-300 text-xs font-semibold uppercase tracking-wider">Selection Total ({{ totalSelectedCredits }} units)</p>
                                    <p class="text-white font-black text-xl mt-0.5">₦{{ calculateSelectedCost.toLocaleString() }}</p>
                                    <p v-if="!canAffordSelection && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        Exceeds balance by ₦{{ (calculateSelectedCost - wallet_balance).toLocaleString() }}
                                    </p>
                                    <p v-if="!canRegisterMore && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        Exceeds maximum {{ MAX_CREDITS }} units per semester!
                                    </p>"""

content = content.replace(target_total, replacement_total)

target_button = """:disabled="courseForm.processing || courseForm.course_ids.length === 0 || !canAffordSelection\""""
replacement_button = """:disabled="courseForm.processing || courseForm.course_ids.length === 0 || !canAffordSelection || !canRegisterMore\""""
content = content.replace(target_button, replacement_button)

target_toast = """    if (!canAffordSelection.value) {
        showToast('error', 'Insufficient wallet balance for the selected courses. Please top up first.');
        return;
    }"""
replacement_toast = """    if (!canAffordSelection.value) {
        showToast('error', 'Insufficient wallet balance for the selected courses. Please top up first.');
        return;
    }
    if (!canRegisterMore.value) {
        showToast('error', `You cannot register more than ${MAX_CREDITS} units per semester.`);
        return;
    }"""
content = content.replace(target_toast, replacement_toast)

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)

