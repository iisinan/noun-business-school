import re

with open('routes/web.php', 'r') as f:
    content = f.read()

content = content.replace(
    "['programmes' => \App\Models\Programme::all()]",
    "['programmes' => \App\Models\Programme::with('specialisations')->get()]"
)

with open('routes/web.php', 'w') as f:
    f.write(content)

