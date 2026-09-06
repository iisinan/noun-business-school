file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Applicant/Dashboard.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                            <p class="mt-2 text-green-300 text-sm max-w-md">
                                Track your admission progress and complete any pending registrations.
                            </p>
                        </div>
                        <a
                            v-if="!application"
                            href="/apply\""""

replace = """                            <p class="mt-2 text-green-300 text-sm max-w-md">
                                Track your admission progress and complete any pending registrations.
                            </p>
                            </div>
                        </div>
                        <a
                            v-if="!application"
                            href="/apply\""""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Fixed div in Dashboard.vue")
else:
    print("Search block not found")
