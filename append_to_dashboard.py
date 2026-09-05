with open('resources/js/Pages/Student/Dashboard.vue', 'r') as f:
    content = f.read()

placeholder = """
                    <!-- Quick Links -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                        <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
                            <h3 class="font-bold text-gray-800 text-lg mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                                Academics
                            </h3>
                            <p class="text-sm text-gray-500 mb-4">Register for your semester courses or check your latest examination results.</p>
                            <a :href="route('student.registration')" class="text-sm font-bold text-noun-green hover:text-noun-dark">Go to Course Registration &rarr;</a>
                        </div>
                        
                        <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
                            <h3 class="font-bold text-gray-800 text-lg mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-noun-green" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                                Finances
                            </h3>
                            <p class="text-sm text-gray-500 mb-4">View your wallet transactions and payment history for the academic year.</p>
                            <a href="#" class="text-sm font-bold text-gray-400 cursor-not-allowed">View Payment History</a>
                        </div>
                    </div>
"""

content = content.replace("                </div>\n\n            </div>\n        </div>", placeholder + "\n                </div>\n\n            </div>\n        </div>")

with open('resources/js/Pages/Student/Dashboard.vue', 'w') as f:
    f.write(content)
