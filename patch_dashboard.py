with open('resources/js/Pages/Applicant/Dashboard.vue', 'r') as f:
    content = f.read()

target = "if (status === 'SUBMITTED') return 2;"
replacement = "if (status === 'DRAFT' || status === 'SUBMITTED') return 2;"
content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/Dashboard.vue', 'w') as f:
    f.write(content)
