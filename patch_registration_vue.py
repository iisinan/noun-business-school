file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/Registration.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = "const calculateSelectedCost = computed(() => {"
replace = """const selectedElectivesCount = computed(() => {
    return electiveAvailableCourses.value.filter(c => courseForm.course_ids.includes(c.id)).length;
});

const calculateSelectedCost = computed(() => {"""

content = content.replace(search, replace)

search_html = """<p v-if="!canRegisterMore && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">"""
replace_html = """<p v-if="selectedElectivesCount > 2" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                                        You can only select up to 2 elective courses!
                                    </p>
                                    <p v-if="!canRegisterMore && courseForm.course_ids.length > 0" class="text-red-400 text-xs font-medium mt-1 flex items-center gap-1">"""

content = content.replace(search_html, replace_html)

search_btn = """:disabled="courseForm.processing || courseForm.course_ids.length === 0 || !canAffordSelection || !canRegisterMore\""""
replace_btn = """:disabled="courseForm.processing || courseForm.course_ids.length === 0 || !canAffordSelection || !canRegisterMore || selectedElectivesCount > 2\""""

content = content.replace(search_btn, replace_btn)

with open(file_path, 'w') as f:
    f.write(content)

print("Patched Registration.vue")
