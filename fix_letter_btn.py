import re

with open('resources/js/Pages/Applicant/Dashboard.vue', 'r') as f:
    content = f.read()

content = content.replace(
    '<button class="text-noun-green hover:text-green-700 font-semibold text-sm underline flex items-center gap-1">',
    '<a :href="route(\'applicant.application.letter\')" target="_blank" class="text-noun-green hover:text-green-700 font-semibold text-sm underline flex items-center gap-1">'
)
content = content.replace(
    'Print Admission Letter\n                                    </button>',
    'Print Admission Letter\n                                    </a>'
)

with open('resources/js/Pages/Applicant/Dashboard.vue', 'w') as f:
    f.write(content)

