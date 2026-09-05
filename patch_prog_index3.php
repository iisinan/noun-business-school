<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue';
$content = file_get_contents($file);

$tableSearch = <<<VUE
                            <tr v-for="prog in programmes" :key="prog.id" class="hover:bg-gray-50 transition-colors">
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2.5 py-1 text-xs font-bold rounded-md bg-noun-dark text-white">{{ prog.type }}</span>
                                </td>
                                <td class="px-6 py-4">
                                    <div class="text-sm font-medium text-gray-900">{{ prog.name }}</div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {{ prog.specialisations?.length ?? 0 }} track{{ (prog.specialisations?.length ?? 0) !== 1 ? 's' : '' }}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                          :class="prog.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                        {{ prog.is_active ? 'Active' : 'Suspended' }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <div class="flex items-center gap-2">
                                        <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm">
                                            Manage
                                            <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                        </Link>
                                        <button @click="toggleStatus(prog.id, prog.is_active)" class="inline-flex items-center gap-1.5 px-3 py-1.5 font-semibold text-xs rounded-lg transition shadow-sm border"
                                                :class="prog.is_active ? 'bg-white border-red-200 text-red-600 hover:bg-red-50' : 'bg-white border-green-200 text-green-600 hover:bg-green-50'">
                                            {{ prog.is_active ? 'Suspend' : 'Activate' }}
                                        </button>
                                    </div>
                                </td>
                            </tr>
                            <tr v-if="!programmes.length">
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No programmes found.</td>
                            </tr>
VUE;

$tableReplace = <<<VUE
                            <template v-for="prog in programmes" :key="prog.id">
                                <!-- Parent Programme Row -->
                                <tr class="bg-gray-100/50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ prog.type }}</span>
                                    </td>
                                    <td class="px-6 py-4">
                                        <div class="text-sm font-bold text-gray-900">{{ prog.name }} (Core)</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ prog.specialisations?.length ?? 0 }} Specialisations
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                              :class="prog.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                            {{ prog.is_active ? 'Active' : 'Suspended' }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm">
                                        <div class="flex items-center gap-2">
                                            <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1 bg-white border border-gray-300 text-gray-700 font-semibold text-xs rounded hover:bg-gray-50 transition shadow-sm">
                                                Manage Core
                                            </Link>
                                            <button @click="toggleStatus(prog.id, prog.is_active)" class="inline-flex items-center gap-1.5 px-3 py-1 font-semibold text-xs rounded transition shadow-sm border"
                                                    :class="prog.is_active ? 'bg-white border-red-200 text-red-600 hover:bg-red-50' : 'bg-white border-green-200 text-green-600 hover:bg-green-50'">
                                                {{ prog.is_active ? 'Suspend' : 'Activate' }}
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                                
                                <!-- Specialisations Rows -->
                                <tr v-for="spec in prog.specialisations" :key="spec.id" class="hover:bg-gray-50 transition-colors border-l-2 border-l-noun-green">
                                    <td class="px-6 py-3 whitespace-nowrap">
                                        <span class="px-2 py-0.5 ml-4 text-[10px] font-semibold rounded bg-gray-100 text-gray-600">Track</span>
                                    </td>
                                    <td class="px-6 py-3">
                                        <div class="text-sm font-medium text-gray-700 pl-4 border-l border-gray-200">{{ spec.name }}</div>
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap text-sm text-gray-400">
                                        Specific Curriculum
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap">
                                        <span class="text-xs text-gray-400">Inherits Status</span>
                                    </td>
                                    <td class="px-6 py-3 whitespace-nowrap text-sm">
                                        <Link :href="route('admin.specialisations.show', spec.id)" class="inline-flex items-center gap-1.5 px-3 py-1 bg-noun-green text-white font-semibold text-[11px] rounded hover:bg-noun-dark transition shadow-sm">
                                            Manage Track
                                            <svg class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                        </Link>
                                    </td>
                                </tr>
                            </template>
                            <tr v-if="!programmes.length">
                                <td colspan="5" class="px-6 py-12 text-center text-sm text-gray-400">No programmes found.</td>
                            </tr>
VUE;

$content = str_replace($tableSearch, $tableReplace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue\n";
