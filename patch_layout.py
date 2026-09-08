file_path = '/Users/sinan/Herd/Business School/resources/js/Layouts/StudentLayout.vue'
with open(file_path, 'r') as f:
    content = f.read()

import re

# 1. Add print classes to main wrapper div
content = content.replace(
    '<div class="min-h-screen bg-gray-50 flex">',
    '<div class="min-h-screen bg-gray-50 flex print:block print:bg-white">'
)

# 2. Add print:hidden to aside
content = content.replace(
    'class="fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-noun-dark to-[#004d00]',
    'class="print:hidden fixed inset-y-0 left-0 z-50 w-72 bg-gradient-to-b from-noun-dark to-[#004d00]'
)

# 3. Add print classes to main container
content = content.replace(
    '<main class="flex-1 flex flex-col min-w-0 overflow-hidden bg-gray-50/50">',
    '<main class="flex-1 flex flex-col min-w-0 overflow-hidden bg-gray-50/50 print:block print:overflow-visible print:bg-white">'
)

# 4. Add print:hidden to header
content = content.replace(
    '<header class="h-20 bg-white border-b border-gray-100',
    '<header class="print:hidden h-20 bg-white border-b border-gray-100'
)

# 5. Add print classes to page content wrapper
content = content.replace(
    '<div class="flex-1 overflow-y-auto">',
    '<div class="flex-1 overflow-y-auto print:overflow-visible">'
)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched StudentLayout")
