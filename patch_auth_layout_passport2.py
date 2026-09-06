file_path = '/Users/sinan/Herd/Business School/resources/js/Layouts/AuthenticatedLayout.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                                            type="button"
                                            class="flex items-center justify-center h-9 w-9 rounded-full bg-noun-green text-white font-bold text-sm hover:bg-green-600 transition ring-2 ring-noun-yellow focus:outline-none"
                                        >
                                            {{ $page.props.auth.user.name?.charAt(0)?.toUpperCase() }}
                                        </button>"""

replace = """                                            type="button"
                                            class="flex items-center justify-center h-9 w-9 rounded-full bg-noun-green text-white font-bold text-sm hover:bg-green-600 transition ring-2 ring-noun-yellow focus:outline-none overflow-hidden"
                                        >
                                            <img v-if="$page.props.auth.user.passport_url" :src="$page.props.auth.user.passport_url" class="h-full w-full object-cover" />
                                            <span v-else>{{ $page.props.auth.user.name?.charAt(0)?.toUpperCase() || $page.props.auth.user.first_name?.charAt(0)?.toUpperCase() }}</span>
                                        </button>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched AuthenticatedLayout.vue topbar avatar")
else:
    print("Search block not found in AuthenticatedLayout.vue topbar")
