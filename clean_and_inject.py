with open('resources/js/Pages/Welcome.vue', 'r') as f:
    welcome = f.read()

# First, remove everything after </style>
style_end = welcome.find('</style>')
if style_end != -1:
    welcome = welcome[:style_end + 8]

# Now let's extract the clean Latest News from Media.vue
with open('resources/js/Pages/Media.vue', 'r') as f:
    media = f.read()

news_start = media.find('<!-- Latest News -->')
news_end = media.find('<!-- Video/Media Highlights -->')
news_section = media[news_start:news_end]

news_section = news_section.replace('bg-white', 'bg-gray-50')
filter_start = news_section.find('<!-- Category Filter -->')
if filter_start != -1:
    filter_end = news_section.find('</div>', filter_start)
    filter_end = news_section.find('</div>', filter_end + 6) + 6
    news_section = news_section[:filter_start] + news_section[filter_end:]
news_section = news_section.replace('href="#" class="text-noun-green', 'href="/media" class="text-noun-green')

# Inject it right before CTA SECTION
cta_header = """        <!-- ═══════════════════════════════════════════
             CTA SECTION"""
             
cta_idx = welcome.find(cta_header)
if cta_idx != -1:
    welcome = welcome[:cta_idx] + news_section + "\n" + welcome[cta_idx:]

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(welcome)

print("Cleaned and injected.")
