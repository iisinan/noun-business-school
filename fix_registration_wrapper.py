import re

with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

target = """        <div class="py-8 px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start relative">
                <div class="lg:col-span-2 space-y-6">"""

replacement = """        <div class="py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
            <div class="space-y-6">"""

content = content.replace(target, replacement)

# Now we need to remove the two closing divs that were matching that wrapper at the very end.
# Wait, the end of the file is:
#             </div>
#         </div>
#     </StudentLayout>
# </template>
# That matches the two divs we just replaced perfectly! Because we replaced `<div class="grid..."> <div class="col-span-2">` with `<div class="space-y-6">`. Wait!
# Actually, the original wrapper had:
# 1. <div class="py-8 px-4 sm:px-6 lg:px-8">
# 2. <div class="grid ...">
# 3. <div class="lg:col-span-2 space-y-6">
# And the new wrapper has:
# 1. <div class="py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
# 2. <div class="space-y-6">
# So we reduced the depth by 1.
# Which means we have ONE EXTRA `</div>` at the end of the file.

# Let's fix the end of the file.
target_end = """            </div>
        </div>
    </StudentLayout>
</template>"""

replacement_end = """        </div>
    </StudentLayout>
</template>"""

content = content.replace(target_end, replacement_end)

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)
