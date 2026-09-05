import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Fix initial state
content = content.replace(
    "subjects: [{name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}]",
    "subjects: [{name: 'English Language', grade: ''}, {name: 'Mathematics', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}, {name: '', grade: ''}]"
)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

