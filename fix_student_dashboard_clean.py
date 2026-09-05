with open('resources/js/Pages/Student/Dashboard.vue', 'r') as f:
    content = f.read()

content = content.replace("import StudentDashboardComponent from '@/Components/StudentDashboard.vue';", "")
content = content.replace("<!-- Inject the beautiful Student Portal component -->", "")
content = content.replace("<StudentDashboardComponent v-bind=\"$props\" />", "")

with open('resources/js/Pages/Student/Dashboard.vue', 'w') as f:
    f.write(content)

