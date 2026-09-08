files = [
    'resources/js/Pages/Welcome.vue',
    'resources/js/Pages/Media.vue',
    'resources/js/Pages/Resources.vue',
    'resources/js/Pages/Programmes.vue',
    'resources/js/Pages/About.vue',
    'resources/js/Pages/Career.vue',
]

patterns = [
    "    { label: 'Careers',          href: route('career') },\n",
    "    { label: 'Careers', href: route('career') },\n",
]

for path in files:
    try:
        with open(path, 'r') as f:
            content = f.read()
        changed = False
        for p in patterns:
            if p in content:
                content = content.replace(p, '')
                changed = True
        if changed:
            with open(path, 'w') as f:
                f.write(content)
            print(f"Patched: {path}")
        else:
            print(f"No match: {path}")
    except FileNotFoundError:
        print(f"Not found: {path}")
