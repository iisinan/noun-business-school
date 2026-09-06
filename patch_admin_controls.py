file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Applications/Show.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                        <div class="px-6 py-5">
                            <form @submit.prevent="updateStatus">
                                <div class="mb-4">
                                    <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">Update Status</label>
                                    <select v-model="statusForm.status" @change="updateStatus" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green text-sm">
                                        <option value="UNDER REVIEW">Under Review</option>
                                        <option value="ADMITTED">Admitted</option>
                                        <option value="REJECTED">Rejected</option>
                                    </select>
                                </div>

                                <button
                                    type="submit"
                                    :disabled="statusForm.processing"
                                    class="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg text-sm font-semibold text-white bg-noun-green hover:bg-noun-dark transition disabled:opacity-50 shadow-md"
                                >
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    Update Status
                                </button>
                            </form>
                        </div>"""

replace = """                        <div class="px-6 py-5">
                            <div v-if="application.status === 'STARTED'" class="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                                <div class="flex gap-2">
                                    <svg class="h-5 w-5 text-yellow-600 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                                    <div>
                                        <h4 class="text-xs font-bold text-yellow-800 uppercase tracking-wider mb-1">Fee Pending</h4>
                                        <p class="text-xs text-yellow-700">This applicant has not paid the application fee yet. You cannot review or make an admissions decision until payment is complete.</p>
                                    </div>
                                </div>
                            </div>
                            <form v-else @submit.prevent="updateStatus">
                                <div class="mb-4">
                                    <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-1.5">Update Status</label>
                                    <select v-model="statusForm.status" @change="updateStatus" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green text-sm">
                                        <option value="UNDER REVIEW">Under Review</option>
                                        <option value="ADMITTED">Admitted</option>
                                        <option value="REJECTED">Rejected</option>
                                    </select>
                                </div>

                                <button
                                    type="submit"
                                    :disabled="statusForm.processing"
                                    class="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg text-sm font-semibold text-white bg-noun-green hover:bg-noun-dark transition disabled:opacity-50 shadow-md"
                                >
                                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                    Update Status
                                </button>
                            </form>
                        </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Admin Controls")
else:
    print("Search block not found")
