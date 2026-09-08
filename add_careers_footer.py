import re

files = [
    'resources/js/Pages/Welcome.vue',
    'resources/js/Pages/About.vue',
    'resources/js/Pages/Media.vue',
    'resources/js/Pages/Resources.vue',
    'resources/js/Pages/Programmes.vue',
    'resources/js/Pages/Career.vue',
]

# Pattern used in footer Quick Links list
old = "{ label: 'Resources', href: route('resources') },"
new = "{ label: 'Resources', href: route('resources') },\n                                { label: 'Careers', href: route('career') },"

for path in files:
    try:
        with open(path, 'r') as f:
            content = f.read()
        if old in content and "{ label: 'Careers', href: route('career') }" not in content:
            content = content.replace(old, new, 1)
            with open(path, 'w') as f:
                f.write(content)
            print(f"Patched footer: {path}")
        else:
            print(f"Skipped: {path}")
    except FileNotFoundError:
        print(f"Not found: {path}")
