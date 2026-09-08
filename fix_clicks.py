import re

# Fix Welcome.vue Mobile Menu
welcome_path = 'resources/js/Pages/Welcome.vue'
with open(welcome_path, 'r') as f:
    welcome = f.read()

old_link = """                        <Link
                            v-else
                            :href="link.href"
                            class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors"
                        >{{ link.label }}</Link>"""
new_link = """                        <Link
                            v-else
                            :href="link.href"
                            @click="mobileMenuOpen = false"
                            class="block px-3 py-3 text-gray-700 hover:text-noun-green hover:bg-gray-50 rounded-md text-sm font-medium transition-colors"
                        >{{ link.label }}</Link>"""
welcome = welcome.replace(old_link, new_link)

with open(welcome_path, 'w') as f:
    f.write(welcome)
print("Patched Welcome.vue mobile menu")

# Fix Login.vue button feedback
login_path = 'resources/js/Pages/Auth/Login.vue'
with open(login_path, 'r') as f:
    login = f.read()

old_btn = """                <PrimaryButton
                    class="w-full justify-center py-3 text-sm shadow-sm hover:shadow-md"
                    :class="{ 'opacity-25': form.processing }"
                    :disabled="form.processing"
                >
                    Sign in
                </PrimaryButton>"""
new_btn = """                <PrimaryButton
                    class="w-full justify-center py-3 text-sm shadow-sm hover:shadow-md transition-all duration-200"
                    :class="{ 'opacity-70 cursor-not-allowed': form.processing }"
                    :disabled="form.processing"
                >
                    <svg v-if="form.processing" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {{ form.processing ? 'Signing in...' : 'Sign in' }}
                </PrimaryButton>"""
login = login.replace(old_btn, new_btn)

with open(login_path, 'w') as f:
    f.write(login)
print("Patched Login.vue button")
