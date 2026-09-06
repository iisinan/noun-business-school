with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'r') as f:
    content = f.read()

content = content.replace('No courses available in this programme to attach.', 'No courses available in the system.')

with open('resources/js/Pages/Admin/Specialisations/Show.vue', 'w') as f:
    f.write(content)

print("Fixed Show.vue wording")
