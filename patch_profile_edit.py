with open('resources/js/Pages/Profile/Edit.vue', 'r') as f:
    content = f.read()

# Remove the Delete Account block
target_block = """                <!-- Delete Account -->
                <div class="bg-white rounded-xl shadow-sm border border-red-100 overflow-hidden">
                    <div class="px-6 py-4 border-b border-red-100 flex items-center gap-3">
                        <div class="h-8 w-8 rounded-full bg-red-500 flex items-center justify-center">
                            <svg class="h-4 w-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                            </svg>
                        </div>
                        <h3 class="text-sm font-semibold text-red-600">Delete Account</h3>
                    </div>
                    <div class="px-6 py-6">
                        <DeleteUserForm class="max-w-xl" />
                    </div>
                </div>"""

content = content.replace(target_block, "")

# Remove the import
content = content.replace("import DeleteUserForm from './Partials/DeleteUserForm.vue';\n", "")

with open('resources/js/Pages/Profile/Edit.vue', 'w') as f:
    f.write(content)
