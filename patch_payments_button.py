import re

with open('resources/js/Pages/Student/Payments.vue', 'r') as f:
    content = f.read()

target = """                    <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-1 inline-flex w-full sm:w-auto">"""

replacement = """                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                        <!-- Tabs -->
                        <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-1 inline-flex w-full sm:w-auto">
                            <button 
                                @click="activeTab = 'wallet'" 
                                class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                                :class="activeTab === 'wallet' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                            >
                                Wallet Ledger
                            </button>
                            <button 
                                @click="activeTab = 'gateway'" 
                                class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                                :class="activeTab === 'gateway' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                            >
                                External Payments
                            </button>
                        </div>
                        
                        <!-- Print Statement Button -->
                        <a v-if="activeTab === 'wallet'" :href="route('student.payments.statement')" target="_blank" class="inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-gray-900 text-white font-bold text-sm rounded-xl hover:bg-black transition shadow-sm">
                            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                            Download Statement
                        </a>
                    </div>"""

# Remove the old Tabs div since I included it in the replacement above
target_to_remove = """                    <!-- Tabs -->
                    <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-1 inline-flex w-full sm:w-auto">
                        <button 
                            @click="activeTab = 'wallet'" 
                            class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                            :class="activeTab === 'wallet' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                        >
                            Wallet Ledger
                        </button>
                        <button 
                            @click="activeTab = 'gateway'" 
                            class="flex-1 sm:flex-none px-6 py-2.5 text-sm font-bold rounded-xl transition-all"
                            :class="activeTab === 'gateway' ? 'bg-noun-green text-white shadow-sm' : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'"
                        >
                            External Payments
                        </button>
                    </div>"""

content = content.replace(target_to_remove, replacement)

with open('resources/js/Pages/Student/Payments.vue', 'w') as f:
    f.write(content)
