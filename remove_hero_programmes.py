with open('resources/js/Pages/Programmes.vue', 'r') as f:
    programmes = f.read()

# The hero section starts with <!-- Hero Section --> and ends before <!-- Programmes Directory -->
hero_start = programmes.find('<!-- Hero Section -->')
hero_end = programmes.find('<!-- Programmes Directory -->')

if hero_start != -1 and hero_end != -1:
    programmes = programmes[:hero_start] + programmes[hero_end:]
    with open('resources/js/Pages/Programmes.vue', 'w') as f:
        f.write(programmes)
    print("Removed hero section from Programmes.vue")
else:
    print("Could not find hero section boundaries.")
