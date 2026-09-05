import re

with open('resources/js/Pages/Welcome.vue', 'r') as f:
    welcome = f.read()

prog_start = welcome.find('<!-- Core Programmes -->')
prog_end = welcome.find('<!-- Secondary CTA -->')

print(f"Start: {prog_start}, End: {prog_end}")
