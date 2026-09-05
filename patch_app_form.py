with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = """                                    <select v-model="form.programme_id" :class="errorClass('programme_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5">
                                        <option value="">Select a programme...</option>
                                        <option v-for="prog in programmes" :key="prog.id" :value="prog.id">
                                            {{ prog.name }}
                                        </option>
                                    </select>
                                </div>
                                
                                <div v-if="selectedProgramme && selectedProgramme.specialisations.length > 0">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Specialisation <span class="text-red-500">*</span></label>
                                    <select v-model="form.specialisation_id" :class="errorClass('specialisation_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5">
                                        <option value="">Select a specialisation...</option>
                                        <option v-for="spec in selectedProgramme.specialisations" :key="spec.id" :value="spec.id">
                                            {{ spec.name }}
                                        </option>
                                    </select>"""

replacement = """                                    <select v-model="form.programme_id" :disabled="preselected_programme" :class="errorClass('programme_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5 disabled:bg-gray-100 disabled:text-gray-500">
                                        <option value="">Select a programme...</option>
                                        <option v-for="prog in programmes" :key="prog.id" :value="prog.id">
                                            {{ prog.name }}
                                        </option>
                                    </select>
                                    <p v-if="preselected_programme" class="mt-2 text-xs text-noun-green font-medium flex items-center gap-1">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                                        Locked from your initial selection
                                    </p>
                                </div>
                                
                                <div v-if="selectedProgramme && selectedProgramme.specialisations.length > 0">
                                    <label class="block text-sm font-medium text-gray-700 mb-1.5">Specialisation <span class="text-red-500">*</span></label>
                                    <select v-model="form.specialisation_id" :disabled="preselected_specialisation" :class="errorClass('specialisation_id')" class="block w-full rounded-lg shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5 disabled:bg-gray-100 disabled:text-gray-500">
                                        <option value="">Select a specialisation...</option>
                                        <option v-for="spec in selectedProgramme.specialisations" :key="spec.id" :value="spec.id">
                                            {{ spec.name }}
                                        </option>
                                    </select>
                                    <p v-if="preselected_specialisation" class="mt-2 text-xs text-noun-green font-medium flex items-center gap-1">
                                        <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                                        Locked from your initial selection
                                    </p>"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
