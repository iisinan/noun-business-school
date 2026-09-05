import re

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    content = f.read()

content = content.replace('w-full 2xl:px-12', 'w-full max-w-[90rem] mx-auto')

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(content)

print("Container max width fixed.")
