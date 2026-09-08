file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/IdCard.vue'
with open(file_path, 'r') as f:
    content = f.read()

import re

# 1. Remove layout: null
content = re.sub(r'defineOptions\(\{\s*layout:\s*null\s*\}\);\n', '', content)

# 2. Add import for StudentLayout
content = content.replace(
    "import { onMounted } from 'vue';",
    "import { onMounted } from 'vue';\nimport StudentLayout from '@/Layouts/StudentLayout.vue';"
)

# 3. Wrap template in StudentLayout
content = content.replace(
    '<Head title="Student ID Card" />\n\n    <div class="min-h-screen',
    '<Head title="Student ID Card" />\n\n    <StudentLayout>\n    <div class="min-h-screen'
)

# 4. Close StudentLayout at the end
content = content.replace(
    '</div>\n    </div>\n</template>',
    '</div>\n    </div>\n    </StudentLayout>\n</template>'
)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched IdCard.vue")
