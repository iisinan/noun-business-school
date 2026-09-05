import glob

for filepath in glob.glob('resources/js/Pages/*.vue'):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '/bns%20logo.png' in content:
        content = content.replace('/bns%20logo.png', '/nbs-logo.png')
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
