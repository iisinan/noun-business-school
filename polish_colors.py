import re

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    content = f.read()

# 1. Polish Hero Background and Typography
content = content.replace(
    '<section class="relative min-h-screen flex items-center overflow-hidden bg-gray-50">',
    '<section class="relative min-h-screen flex items-center overflow-hidden bg-gradient-to-br from-[#FAF9F6] via-white to-[#F3EDE0]">'
)
content = content.replace(
    'text-4xl sm:text-5xl lg:text-6xl xl:text-[4.5rem] font-bold text-noun-navy',
    'text-4xl sm:text-5xl lg:text-6xl xl:text-[4.5rem] font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-noun-navy via-noun-navy to-slate-600'
)
content = content.replace(
    'bg-gradient-to-br from-white/95 via-gray-50/90 to-gray-100/80',
    'bg-gradient-to-br from-white/95 via-white/80 to-[#F3EDE0]/80'
)

# 2. Polish About Section
content = content.replace(
    '<section id="about" class="py-24 lg:py-32 bg-white relative overflow-hidden">',
    '<section id="about" class="py-24 lg:py-32 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-[#FCFBF8] via-white to-white relative overflow-hidden">'
)

# 3. Polish Programmes Section
content = content.replace(
    '<section id="programmes" class="py-24 lg:py-32 bg-gray-50 relative">',
    '<section id="programmes" class="py-24 lg:py-32 bg-gradient-to-b from-white via-gray-50/50 to-[#F9F8F5] relative">'
)

# 4. Polish Featured Specialisations Background
content = content.replace(
    '<section class="py-24 lg:py-32 bg-gray-50 relative overflow-hidden">',
    '<section class="py-24 lg:py-32 bg-gradient-to-br from-[#FAF9F6] via-white to-[#F4EFE6] relative overflow-hidden">'
)
content = content.replace(
    'bg-[radial-gradient(#e5e7eb_1px,transparent_1px)]',
    'bg-[radial-gradient(#d1d5db_1px,transparent_1px)]'
)

# 5. Make the "Why NOUN" background much richer (Deep Navy with subtle mesh)
content = content.replace(
    '<section id="why" class="py-24 lg:py-32 bg-noun-navy relative overflow-hidden">',
    '<section id="why" class="py-24 lg:py-32 bg-[#060D18] relative overflow-hidden">'
)

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(content)
print("Polished colors successfully.")
