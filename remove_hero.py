with open('resources/js/Pages/Resources.vue', 'r') as f:
    resources = f.read()

# The hero section starts with <!-- Hero Section --> and ends before <!-- Interactive Document Viewer -->
hero_start = resources.find('<!-- Hero Section -->')
hero_end = resources.find('<!-- Interactive Document Viewer -->')

if hero_start != -1 and hero_end != -1:
    resources = resources[:hero_start] + resources[hero_end:]
    with open('resources/js/Pages/Resources.vue', 'w') as f:
        f.write(resources)
    print("Removed hero section.")
else:
    print("Could not find hero section boundaries.")
