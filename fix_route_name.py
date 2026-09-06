file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Results/Upload.vue'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace("route('results.template'", "route('admin.results.template'")

with open(file_path, 'w') as f:
    f.write(content)
print("Patched route name")
