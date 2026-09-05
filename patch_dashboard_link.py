with open('resources/js/Pages/Student/Dashboard.vue', 'r') as f:
    content = f.read()

target = """                            <a href="#" class="text-sm font-bold text-gray-400 cursor-not-allowed">View Payment History</a>"""

replacement = """                            <Link :href="route('student.payments')" class="text-sm font-bold text-noun-green hover:underline">View Payment History &rarr;</Link>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Student/Dashboard.vue', 'w') as f:
    f.write(content)
