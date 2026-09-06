import json

with open('composer.json', 'r') as f:
    data = json.load(f)

scripts = data.get('scripts', {})
post_autoload_dump = scripts.get('post-autoload-dump', [])

if "@php artisan optimize" not in post_autoload_dump:
    post_autoload_dump.append("@php artisan optimize")
    scripts['post-autoload-dump'] = post_autoload_dump
    data['scripts'] = scripts
    
    with open('composer.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Patched composer.json")
else:
    print("Already patched")
