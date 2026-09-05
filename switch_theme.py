import re

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    content = f.read()

# 1. Typography and core colors
content = content.replace('noun-navy', 'noun-dark')
content = content.replace('noun-gold', 'noun-yellow')

# 2. Dark Backgrounds to Deep Green
content = content.replace('bg-[#060D18]', 'bg-[#001a00]')
content = content.replace('from-[#001a00] via-[#001a00]', 'from-[#002200] via-[#003300]') # For CTA if it had it... wait, it was noun-navy which is now noun-dark.
content = content.replace('from-noun-dark via-noun-dark/95 to-noun-dark/80', 'from-[#001a00] via-[#003300]/95 to-[#004d00]/80')

# 3. Gradients
content = content.replace('from-noun-dark via-noun-dark to-slate-600', 'from-noun-dark via-noun-green to-noun-dark')

# 4. Ivory to White/Green-light
content = content.replace('from-[#FAF9F6] via-white to-[#F3EDE0]', 'from-white via-white to-noun-light/30')
content = content.replace('from-[#FCFBF8] via-white to-white', 'from-white via-white to-noun-light/20')
content = content.replace('from-white via-gray-50/50 to-[#F9F8F5]', 'from-white via-noun-light/10 to-white')
content = content.replace('from-[#FAF9F6] via-white to-[#F4EFE6]', 'from-white via-white to-noun-light/30')
content = content.replace('to-[#F3EDE0]/80', 'to-white/80')

# 5. Fix border and shadow colors for the yellow/green
content = content.replace('rgba(201,152,42', 'rgba(242,169,0') # gold to yellow rgb
content = content.replace('bg-[#001a00]/10', 'bg-noun-yellow/10') # just in case

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(content)
print("Theme switched to Green and White successfully.")
