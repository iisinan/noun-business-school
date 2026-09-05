import os

files = [
    'resources/js/Pages/Welcome.vue',
    'resources/js/Pages/About.vue',
    'resources/js/Pages/Media.vue',
    'resources/js/Pages/Resources.vue',
]

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the navLinks definition
    content = content.replace("{ label: 'Programmes',       href: '#programmes' }", "{ label: 'Programmes',       href: route('programmes') }")
    content = content.replace("{ label: 'Programmes', href: '/#programmes' }", "{ label: 'Programmes', href: route('programmes') }")
    content = content.replace("{ label: 'Programmes', href: '#programmes' }", "{ label: 'Programmes', href: route('programmes') }")
    
    # Also replace Quick Links in footer where it's hardcoded
    content = content.replace("{ label: 'Our Programmes', href: '#programmes' }", "{ label: 'Our Programmes', href: route('programmes') }")
    content = content.replace("{ label: 'Our Programmes', href: '/#programmes' }", "{ label: 'Our Programmes', href: route('programmes') }")
    
    # Also in footer Programmes list
    content = content.replace("href=\"#programmes\"", ":href=\"route('programmes')\"")
    
    with open(filepath, 'w') as f:
        f.write(content)

print("Updated links globally")
