with open('resources/js/Pages/Welcome.vue', 'r') as f:
    welcome = f.read()

# First, remove the bad injection
bad_start = welcome.find('<!-- Latest News -->')
bad_end = welcome.find('</section>', bad_start) + len('</section>')

if bad_start != -1:
    welcome = welcome[:bad_start] + welcome[bad_end:]

# Now extract news properly from Media.vue again
with open('resources/js/Pages/Media.vue', 'r') as f:
    media = f.read()

news_start = media.find('<!-- Latest News -->')
news_end = media.find('<!-- Video/Media Highlights -->')
news_section = media[news_start:news_end]

# Modify it
news_section = news_section.replace('bg-white', 'bg-gray-50')
filter_start = news_section.find('<!-- Category Filter -->')
if filter_start != -1:
    filter_end = news_section.find('</div>', filter_start)
    filter_end = news_section.find('</div>', filter_end + 6) + 6
    news_section = news_section[:filter_start] + news_section[filter_end:]
news_section = news_section.replace('href="#" class="text-noun-green', 'href="/media" class="text-noun-green')

# Inject properly right above <!-- Footer --> inside the template
# There is a Footer component inside <main> or the top level template?
# Let's find "<!-- Footer -->" but make sure it's the one inside <template>
footer_idx = welcome.find('<!-- FOOTER -->')
if footer_idx == -1:
    footer_idx = welcome.find('<!-- Footer -->')

if footer_idx != -1:
    welcome = welcome[:footer_idx] + news_section + "\n        " + welcome[footer_idx:]

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(welcome)

print("Fixed Welcome.vue")
