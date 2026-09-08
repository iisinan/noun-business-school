file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/IdCard.vue'
with open(file_path, 'r') as f:
    content = f.read()

import re

# Remove the fixed action buttons and the title block since they will be in the header slot
content = re.sub(
    r'<!-- Action Buttons \(Hidden in print\) -->.*?<div class="mb-6 text-center print:hidden">.*?<p class="text-gray-500 text-sm mt-1">Please print this page in color on standard card stock\.</p>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

# Insert the header slot right after <StudentLayout>
header_slot = """
        <template #header>
            <div class="flex items-center justify-between w-full">
                <h2 class="font-bold text-gray-800 text-lg hidden sm:flex items-center gap-2">
                    <svg class="w-5 h-5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"></path></svg>
                    Student ID Card
                </h2>
                <div class="flex items-center gap-3 print:hidden ml-4">
                    <button @click="printCard" class="px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-semibold shadow-sm hover:bg-noun-dark transition inline-flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                        Print ID Card
                    </button>
                </div>
            </div>
        </template>
        
        <div class="text-center print:hidden mb-6 mt-4">
            <p class="text-gray-500 text-sm">Please print this page in color on standard card stock.</p>
        </div>
"""

content = content.replace('<StudentLayout>\n    <div class="min-h-screen bg-gray-50 flex flex-col items-center py-10 print:py-0 print:bg-white relative">', 
                          '<StudentLayout>' + header_slot + '\n    <div class="flex flex-col items-center py-10 print:py-0 print:bg-white relative">')


# Remove goBack function since we don't need it anymore
content = content.replace('const goBack = () => { window.history.back(); };\n', '')


with open(file_path, 'w') as f:
    f.write(content)
print("Patched IdCard.vue header")
