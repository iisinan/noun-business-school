import re

files = [
    'resources/js/Pages/Welcome.vue',
    'resources/js/Pages/Media.vue',
    'resources/js/Pages/Resources.vue',
    'resources/js/Pages/Programmes.vue',
]

old = "    { label: 'Contact',          href: '#contact' },"
new = "    { label: 'Careers',          href: route('career') },\n    { label: 'Contact',          href: '#contact' },"

for path in files:
    try:
        with open(path, 'r') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new)
            with open(path, 'w') as f:
                f.write(content)
            print(f"Patched: {path}")
        else:
            print(f"Skipped (no match): {path}")
    except FileNotFoundError:
        print(f"File not found: {path}")
