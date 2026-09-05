import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

content = content.replace(
    'v-if="req.is_document"',
    'v-if="req.is_document == 1 || req.is_document === true || req.is_document === \'1\'"'
)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

