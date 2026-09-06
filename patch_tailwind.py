file_path = '/Users/sinan/Herd/Business School/tailwind.config.js'
with open(file_path, 'r') as f:
    content = f.read()

if 'future:' not in content:
    content = content.replace('export default {', "export default {\n    future: {\n        hoverOnlyWhenSupported: true,\n    },")
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched tailwind.config.js")
else:
    print("Already patched")
