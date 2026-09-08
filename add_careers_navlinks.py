# About and Media use navLinks for their footer, so just add Careers to their navLinks array
old = "    { label: 'Resources',        href: route('resources') },\n    { label: 'Contact',          href: '#contact' },"
new = "    { label: 'Resources',        href: route('resources') },\n    { label: 'Careers',          href: route('career') },\n    { label: 'Contact',          href: '#contact' },"

for path in ['resources/js/Pages/About.vue', 'resources/js/Pages/Media.vue']:
    with open(path, 'r') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w') as f:
            f.write(content)
        print(f"Patched navLinks: {path}")
    else:
        print(f"No match: {path}")
