with open('resources/js/Pages/Auth/Login.vue', 'r') as f:
    content = f.read()

target = """            <div class="mt-6 text-center text-sm text-gray-500">
                Don't have an account?
                <Link
                    :href="route('register')"
                    class="font-semibold text-noun-green hover:text-noun-dark transition ml-1"
                >
                    Sign up
                </Link>
            </div>"""

content = content.replace(target, "")

with open('resources/js/Pages/Auth/Login.vue', 'w') as f:
    f.write(content)
