with open('resources/js/Pages/Resources.vue', 'r') as f:
    resources = f.read()

# Add navLinks and mobileMenuOpen back to the script setup
missing_code = """
const mobileMenuOpen = ref(false);

const navLinks = [
    { label: 'Home', href: '/' },
    { label: 'About', href: route('about') },
    { label: 'Programmes', href: '/#programmes' },
    { label: 'Admissions', href: '/#admissions' },
    { label: 'Media', href: route('media') },
    { label: 'Resources', href: route('resources') },
    { label: 'Contact', href: '/#contact' },
];
"""

# Insert it before const documentResources
pos = resources.find('const documentResources')
resources = resources[:pos] + missing_code + "\n" + resources[pos:]

with open('resources/js/Pages/Resources.vue', 'w') as f:
    f.write(resources)

print("Fixed missing navLinks in Resources.vue")
