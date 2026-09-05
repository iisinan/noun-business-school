import re

with open('resources/js/Pages/Student/Dashboard.vue', 'r') as f:
    content = f.read()

content = content.replace("import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout.vue';", "import StudentLayout from '@/Layouts/StudentLayout.vue';")
content = content.replace("<AuthenticatedLayout>", "<StudentLayout>")
content = content.replace("</AuthenticatedLayout>", "</StudentLayout>")

with open('resources/js/Pages/Student/Dashboard.vue', 'w') as f:
    f.write(content)

