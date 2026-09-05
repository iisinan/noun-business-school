<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Sessions/Index.vue';
$content = file_get_contents($file);

$tableSearch = <<<VUE
                                <tr v-for="session in sessions" :key="session.id" class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-gray-900">
                                        {{ session.name }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        <div>Apps: <span class="font-semibold">{{ session.total_applications || 0 }}</span></div>
                                        <div>Enrolled: <span class="font-semibold">{{ session.enrolled_students || 0 }}</span></div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col gap-1.5">
                                            <div>
                                                <span v-if="session.is_active" class="px-2.5 py-1 text-xs font-bold rounded-full bg-green-100 text-green-800">
                                                    Active Session
                                                </span>
                                                <span v-else class="px-2.5 py-1 text-xs font-semibold rounded-full bg-gray-100 text-gray-600">
                                                    Inactive
                                                </span>
                                            </div>
                                            <div v-if="session.is_active">
                                                <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-blue-100 text-blue-800">
                                                    Semester {{ session.current_semester }}
                                                </span>
                                            </div>
                                            <div v-if="session.is_active">
                                                <span v-if="session.registration_open" class="px-2.5 py-1 text-xs font-semibold rounded-full bg-emerald-100 text-emerald-800">
                                                    Reg: Open
                                                </span>
                                                <span v-else class="px-2.5 py-1 text-xs font-semibold rounded-full bg-red-100 text-red-800">
                                                    Reg: Closed
                                                </span>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                        <button 
                                            v-if="!session.is_active"
                                            @click="activateSession(session.id)" 
                                            class="text-noun-green hover:text-noun-dark font-semibold border border-noun-green px-3 py-1.5 rounded-lg hover:bg-green-50 transition"
                                        >
                                            Activate Session
                                        </button>
                                        <div v-else class="flex flex-col items-end gap-2">
                                            <button 
                                                @click="toggleRegistration(session.id, session.registration_open)" 
                                                class="text-xs font-semibold border px-3 py-1.5 rounded-lg transition"
                                                :class="session.registration_open ? 'border-red-500 text-red-600 hover:bg-red-50' : 'border-emerald-500 text-emerald-600 hover:bg-emerald-50'"
                                            >
                                                {{ session.registration_open ? 'Close Registration' : 'Open Registration' }}
                                            </button>
                                            <button 
                                                @click="advanceSemester(session.id, session.current_semester)" 
                                                class="text-xs font-semibold border border-noun-green text-noun-green px-3 py-1.5 rounded-lg hover:bg-green-50 transition"
                                            >
                                                Start Semester {{ session.current_semester + 1 }}
                                            </button>
                                        </div>
                                    </td>
                                </tr>
VUE;

$tableReplace = <<<VUE
                                <tr v-for="session in sessions" :key="session.id" class="hover:bg-gray-50 transition duration-150">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="text-sm font-black text-gray-900">{{ session.name }}</div>
                                        <div class="text-xs text-gray-500 mt-1">ID: #{{ session.id }}</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col gap-1 text-xs">
                                            <div class="flex justify-between w-32 border-b border-gray-100 pb-1">
                                                <span class="text-gray-500">Apps:</span>
                                                <span class="font-bold text-gray-800">{{ session.total_applications || 0 }}</span>
                                            </div>
                                            <div class="flex justify-between w-32">
                                                <span class="text-gray-500">Enrolled:</span>
                                                <span class="font-bold text-noun-green">{{ session.enrolled_students || 0 }}</span>
                                            </div>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4">
                                        <div class="flex flex-wrap items-center gap-2">
                                            <span v-if="session.is_active" class="px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider rounded-md bg-noun-dark text-white flex items-center gap-1 shadow-sm">
                                                <span class="w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse"></span>
                                                Active
                                            </span>
                                            <span v-else class="px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider rounded-md bg-gray-100 text-gray-500">
                                                Inactive
                                            </span>

                                            <span v-if="session.is_active" class="px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider rounded-md bg-blue-50 text-blue-700 border border-blue-200">
                                                Sem {{ session.current_semester }}
                                            </span>

                                            <span v-if="session.is_active" 
                                                  class="px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider rounded-md border flex items-center gap-1"
                                                  :class="session.registration_open ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-red-50 text-red-700 border-red-200'">
                                                {{ session.registration_open ? 'Reg: Open' : 'Reg: Closed' }}
                                            </span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                        <button 
                                            v-if="!session.is_active"
                                            @click="activateSession(session.id)" 
                                            class="inline-flex items-center gap-1 text-noun-green hover:text-white border border-noun-green hover:bg-noun-green px-4 py-2 rounded-lg font-bold text-xs transition shadow-sm"
                                        >
                                            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                                            Make Active
                                        </button>
                                        
                                        <div v-else class="flex flex-col sm:flex-row items-end sm:items-center justify-end gap-2">
                                            <button 
                                                @click="toggleRegistration(session.id, session.registration_open)" 
                                                class="inline-flex items-center gap-1 text-xs font-bold border px-3 py-2 rounded-lg transition shadow-sm"
                                                :class="session.registration_open ? 'border-red-200 text-red-600 bg-red-50 hover:bg-red-100 hover:border-red-300' : 'border-emerald-200 text-emerald-600 bg-emerald-50 hover:bg-emerald-100 hover:border-emerald-300'"
                                            >
                                                <svg v-if="session.registration_open" class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                                <svg v-else class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                                {{ session.registration_open ? 'Close Reg' : 'Open Reg' }}
                                            </button>
                                            <button 
                                                @click="advanceSemester(session.id, session.current_semester)" 
                                                class="inline-flex items-center gap-1 text-xs font-bold border border-gray-200 text-gray-700 bg-white hover:bg-gray-50 px-3 py-2 rounded-lg transition shadow-sm"
                                            >
                                                <svg class="w-3.5 h-3.5 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7" /></svg>
                                                Advance Semester
                                            </button>
                                        </div>
                                    </td>
                                </tr>
VUE;

$content = str_replace($tableSearch, $tableReplace, $content);

// Also polish the Create form a bit
$createFormSearch = <<<VUE
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Session Name</label>
                                <input v-model="form.name" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="e.g. 2024/2025">
                                <p v-if="form.errors.name" class="text-sm text-red-600 mt-1">{{ form.errors.name }}</p>
                            </div>
                            <div class="flex items-center gap-2">
                                <input v-model="form.is_active" type="checkbox" class="h-4 w-4 text-noun-green focus:ring-noun-green border-gray-300 rounded">
                                <label class="text-sm text-gray-700 font-medium">Set as Active Session</label>
                            </div>
                            <button type="submit" :disabled="form.processing" class="w-full bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm disabled:opacity-50">
                                Create Session
                            </button>
VUE;

$createFormReplace = <<<VUE
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1.5">Session Name</label>
                                <input v-model="form.name" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm bg-gray-50 focus:bg-white transition" placeholder="e.g. 2024/2025">
                                <p v-if="form.errors.name" class="text-sm text-red-600 mt-1">{{ form.errors.name }}</p>
                            </div>
                            <div class="flex items-center gap-2 p-3 bg-gray-50 rounded-lg border border-gray-100">
                                <input v-model="form.is_active" type="checkbox" id="is_active_cb" class="h-4 w-4 text-noun-green focus:ring-noun-green border-gray-300 rounded">
                                <label for="is_active_cb" class="text-sm text-gray-700 font-bold cursor-pointer">Set as Active Session immediately</label>
                            </div>
                            <button type="submit" :disabled="form.processing" class="w-full bg-noun-green text-white px-4 py-2.5 rounded-lg text-sm font-bold hover:bg-noun-dark transition shadow-sm disabled:opacity-50 flex justify-center items-center gap-2">
                                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                                Create Session
                            </button>
VUE;

$content = str_replace($createFormSearch, $createFormReplace, $content);

file_put_contents($file, $content);
echo "Patched Index.vue for polishing\n";
