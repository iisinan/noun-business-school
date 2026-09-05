import re

with open('resources/js/Pages/Applicant/Dashboard.vue', 'r') as f:
    content = f.read()

target = """                                <div>
                                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Submitted On</p>
                                    <p class="font-semibold text-gray-900">{{ new Date(application.created_at).toLocaleDateString() }}</p>
                                </div>
                            </div>
                        </div>"""

replacement = """                                <div>
                                    <p class="text-xs text-gray-500 uppercase tracking-wider mb-1">Submitted On</p>
                                    <p class="font-semibold text-gray-900">{{ new Date(application.created_at).toLocaleDateString() }}</p>
                                </div>
                                <div v-if="application.status !== 'STARTED'" class="flex items-end">
                                    <a :href="route('applicant.application.docket')" target="_blank" class="text-noun-green hover:text-green-700 font-semibold text-sm underline flex items-center gap-1 mt-2">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                        Print Form Docket
                                    </a>
                                </div>
                            </div>
                        </div>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/Dashboard.vue', 'w') as f:
    f.write(content)

