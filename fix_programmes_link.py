files = [
    'resources/js/Pages/About.vue',
    'resources/js/Pages/Career.vue',
    'resources/js/Pages/Media.vue',
]
old = "{ label: 'Programmes',       href: '/#programmes' }"
old2 = "{ label: 'Programmes',  href: '/#programmes' }"
new = "{ label: 'Programmes',       href: route('programmes') }"

for path in files:
    try:
        with open(path, 'r') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new)
        if old2 in content:
            content = content.replace(old2, new)
        with open(path, 'w') as f:
            f.write(content)
        print(f"Patched: {path}")
    except Exception as e:
        print(f"Error: {e}")
