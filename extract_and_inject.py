with open('resources/js/Pages/Media.vue', 'r') as f:
    media = f.read()

# Extract the News section from Media.vue
news_start = media.find('<!-- Latest News -->')
news_end = media.find('<!-- Video/Media Highlights -->')
news_section = media[news_start:news_end]

# We should modify the news section slightly for the home page:
# Remove the category filters (All, Press Releases, etc.) because it's just a summary on the home page.
# Keep the header "Latest News" and the "View All ->" link.
# Change the "View All" link to actually point to route('media') if we can, or just /media.

news_section = news_section.replace('bg-white', 'bg-gray-50') # match background maybe, or keep white if CTA is dark

# Remove category filter
filter_start = news_section.find('<!-- Category Filter -->')
if filter_start != -1:
    filter_end = news_section.find('</div>', filter_start)
    filter_end = news_section.find('</div>', filter_end + 6) + 6
    news_section = news_section[:filter_start] + news_section[filter_end:]

# Update the "View All" link
news_section = news_section.replace('href="#" class="text-noun-green', 'href="/media" class="text-noun-green')

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    welcome = f.read()

# Inject into Welcome.vue right before CTA
cta_start = welcome.find('<!-- CTA Section -->')
if cta_start == -1:
    cta_start = welcome.find('<!-- Footer -->') # Fallback
    
new_welcome = welcome[:cta_start] + news_section + "\n            " + welcome[cta_start:]

with open('resources/js/Pages/Welcome.vue', 'w') as f:
    f.write(new_welcome)

print("Injected News into Welcome.vue")
