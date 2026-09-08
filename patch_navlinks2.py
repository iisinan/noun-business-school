old = "    { label: 'Contact', href: '/#contact' },"
new = "    { label: 'Careers', href: route('career') },\n    { label: 'Contact', href: '/#contact' },"

for path in ['resources/js/Pages/Resources.vue', 'resources/js/Pages/Programmes.vue']:
    with open(path, 'r') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new, 1)
        with open(path, 'w') as f:
            f.write(content)
        print(f"Patched: {path}")
    else:
        print(f"No match: {path}")
