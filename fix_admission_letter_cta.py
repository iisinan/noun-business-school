import re

with open('resources/js/Pages/Applicant/Dashboard.vue', 'r') as f:
    content = f.read()

target = """                                    <div class="flex flex-col sm:items-end gap-2">
                                        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-noun-yellow text-noun-dark rounded-full text-xs font-black uppercase tracking-wide">
                                            <span class="w-1.5 h-1.5 rounded-full bg-noun-dark animate-pulse"></span>
                                            Enrolled
                                        </span>
                                        <a :href="route('applicant.application.letter')" target="_blank" class="inline-flex items-center gap-1.5 px-3 py-2 bg-white/15 hover:bg-white/25 text-white text-xs font-semibold rounded-lg transition">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                            Print Admission Letter
                                        </a>
                                    </div>"""

replacement = """                                    <div class="flex flex-col sm:items-end gap-2">
                                        <span class="inline-flex items-center gap-1.5 px-3 py-1 bg-noun-yellow text-noun-dark rounded-full text-xs font-black uppercase tracking-wide">
                                            <span class="w-1.5 h-1.5 rounded-full bg-noun-dark animate-pulse"></span>
                                            Enrolled
                                        </span>
                                    </div>"""

content = content.replace(target, replacement)

# Add the massive CTA right below the Matric Card
matric_card_end = """                                <div class="h-1 bg-gradient-to-r from-noun-yellow via-noun-gold to-noun-yellow"></div>
                            </div>"""

cta_block = """                                <div class="h-1 bg-gradient-to-r from-noun-yellow via-noun-gold to-noun-yellow"></div>
                            </div>

                            <!-- Massive Admission Letter CTA -->
                            <div class="bg-green-50 border border-green-200 rounded-2xl p-6 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-6">
                                <div>
                                    <h4 class="font-bold text-green-900 text-lg flex items-center gap-2">
                                        <svg class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                        </svg>
                                        Official Admission Letter
                                    </h4>
                                    <p class="text-sm text-green-800 mt-2">
                                        Please download and print your official admission letter. You will need a physical copy of this document for your physical clearance and final registration at the study centre.
                                    </p>
                                </div>
                                <a :href="route('applicant.application.letter')" target="_blank" class="flex-shrink-0 inline-flex items-center gap-2 px-6 py-3 bg-noun-green text-white font-bold rounded-xl hover:bg-noun-dark transition shadow-md whitespace-nowrap">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                    Download Letter
                                </a>
                            </div>"""

content = content.replace(matric_card_end, cta_block)

with open('resources/js/Pages/Applicant/Dashboard.vue', 'w') as f:
    f.write(content)

