import re

with open('resources/js/Pages/Admin/Users/Index.vue', 'r') as f:
    content = f.read()

content = content.replace("import debounce from 'lodash/debounce';", """
function debounce(fn, wait) {
    let timer;
    return function (...args) {
        if (timer) clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), wait);
    };
}
""")

with open('resources/js/Pages/Admin/Users/Index.vue', 'w') as f:
    f.write(content)

