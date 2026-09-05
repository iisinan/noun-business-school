with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

target = """<template>
    <div class="space-y-6">"""

replacement = """<template>
    <Head title="Course Registration" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Course Registration</h2>
        </template>
        
        <div class="py-8 px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start relative">
                <div class="lg:col-span-2 space-y-6">"""

content = content.replace(target, replacement)

# We also need to fix the end of the file because StudentDashboard had just </div>
# The very end of the file is:
#     </div>
# 
#             </div>
#         </div>
#     </StudentLayout>
# </template>
# We can just leave that as is, but let's make sure it's valid Vue.

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)
