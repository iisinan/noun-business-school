import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

content = content.replace(
    '<select v-model="sub.name" class="block w-full rounded-lg border-gray-300',
    '<select v-model="sub.name" :class="errorClass(\'olevel_sub_name_\'+index+\'_\'+subIdx)" class="block w-full rounded-lg'
)

content = content.replace(
    '<select v-model="sub.grade" class="block w-full rounded-lg border-gray-300',
    '<select v-model="sub.grade" :class="errorClass(\'olevel_sub_grade_\'+index+\'_\'+subIdx)" class="block w-full rounded-lg'
)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

