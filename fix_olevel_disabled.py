import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Add disabled and bg-gray-100 logic to the select for subject name
target_str = '<select v-model="sub.name" :class="errorClass(\'olevel_sub_name_\'+index+\'_\'+subIdx)" class="block w-full rounded-lg'
replacement = '<select v-model="sub.name" :disabled="subIdx === 0 || subIdx === 1" :class="[errorClass(\'olevel_sub_name_\'+index+\'_\'+subIdx), subIdx === 0 || subIdx === 1 ? \'bg-gray-100 cursor-not-allowed text-gray-600\' : \'\']" class="block w-full rounded-lg'

content = content.replace(target_str, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

