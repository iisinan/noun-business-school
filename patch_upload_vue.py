with open('resources/js/Pages/Admin/Results/Upload.vue', 'r') as f:
    content = f.read()

# Update the radio button label
target_radio = """                                            <span class="text-xs font-bold tracking-wide">Semester</span>
                                        </label>"""
replacement_radio = """                                            <span class="text-xs font-bold tracking-wide">Multiple Courses</span>
                                        </label>"""

if target_radio in content:
    content = content.replace(target_radio, replacement_radio)

# Remove the semester dropdown
target_dropdown = """                                    <div v-if="templateForm.mode === 'multiple'">
                                        <label class="block text-sm font-bold text-gray-700 mb-1.5">Semester</label>
                                        <select v-model="templateForm.semester" class="block w-full border-gray-300 rounded-lg shadow-sm focus:ring-noun-green focus:border-noun-green text-sm bg-white">
                                            <option v-for="i in 6" :key="i" :value="i">Semester {{ i }}</option>
                                        </select>
                                    </div>"""
replacement_dropdown = """"""

if target_dropdown in content:
    content = content.replace(target_dropdown, replacement_dropdown)

with open('resources/js/Pages/Admin/Results/Upload.vue', 'w') as f:
    f.write(content)
print("Patched Upload.vue")
