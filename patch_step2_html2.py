with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = """                                <div class="md:col-span-2">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Residential Address <span class="text-red-500">*</span></label>
                                    <input type="text" v-model="form.personal_info.address" :class="errorClass('address')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                            </div>
                        </div>"""

replacement = """                                <div class="md:col-span-2">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Residential Address <span class="text-red-500">*</span></label>
                                    <input type="text" v-model="form.personal_info.address" :class="errorClass('address')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm">
                                </div>
                                
                                <div class="col-span-1 md:col-span-2 mt-4 bg-white p-5 rounded-xl border border-gray-100 shadow-sm flex flex-col sm:flex-row gap-6 items-center">
                                    <div class="w-28 h-28 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden flex-shrink-0 border border-gray-200">
                                        <img v-if="passportPreview" :src="passportPreview" class="w-full h-full object-cover" />
                                        <svg v-else class="w-10 h-10 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                                    </div>
                                    <div class="flex-1 w-full text-center sm:text-left">
                                        <h4 class="font-bold text-gray-800 text-sm mb-1">Passport Photograph <span class="text-red-500">*</span></h4>
                                        <p class="text-xs text-gray-500 mb-4">Upload a recent, clear passport-sized photograph. Max 2MB (JPG/PNG).</p>
                                        <div class="flex justify-center sm:justify-start">
                                            <label for="passport_upload" class="cursor-pointer inline-flex items-center gap-1.5 text-xs font-bold text-noun-green hover:text-noun-dark bg-green-50 hover:bg-green-100 px-4 py-2 rounded-full transition-colors border border-green-200 shadow-sm" :class="errorClass('passport_photograph')">
                                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
                                                Choose Image
                                            </label>
                                            <input id="passport_upload" type="file" accept="image/jpeg, image/png" @change="handlePassportUpload" class="hidden">
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
