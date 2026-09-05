<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue';
$content = file_get_contents($file);

$scriptSearch = <<<VUE
const toggleStatus = (id, isActive) => {
    const action = isActive ? 'suspend' : 'activate';
    if (confirm(`Are you sure you want to \${action} this programme?`)) {
        router.post(route('admin.programmes.toggleStatus', id), {}, { preserveScroll: true });
    }
};
</script>
VUE;

$scriptReplace = <<<VUE
const toggleStatus = (id, isActive) => {
    const action = isActive ? 'suspend' : 'activate';
    if (confirm(`Are you sure you want to \${action} this programme?`)) {
        router.post(route('admin.programmes.toggleStatus', id), {}, { preserveScroll: true });
    }
};

const expandedProgrammes = ref([]);

const toggleExpand = (id) => {
    const index = expandedProgrammes.value.indexOf(id);
    if (index > -1) {
        expandedProgrammes.value.splice(index, 1);
    } else {
        expandedProgrammes.value.push(id);
    }
};
</script>
VUE;

$content = str_replace($scriptSearch, $scriptReplace, $content);

$templateSearch = <<<VUE
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
VUE;

$templateReplace = <<<VUE
                            <template v-for="prog in programmes" :key="prog.id">
                                <!-- Parent Programme Row -->
                                <tr class="bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer group" @click="toggleExpand(prog.id)">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ prog.type }}</span>
                                    </td>
                                    <td class="px-6 py-4">
                                        <div class="flex items-center gap-2">
                                            <svg class="w-4 h-4 text-gray-400 group-hover:text-gray-600 transition-transform duration-200" :class="{ 'rotate-90': expandedProgrammes.includes(prog.id) }" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                            <div class="text-sm font-bold text-gray-900">{{ prog.name }} (Core)</div>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 font-medium">
                                        <span class="bg-white border border-gray-200 px-2.5 py-0.5 rounded-full">{{ prog.specialisations?.length ?? 0 }} Tracks</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                              :class="prog.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                            {{ prog.is_active ? 'Active' : 'Suspended' }}
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm" @click.stop>
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
                                
                                <!-- Specialisations Rows (Dropdown) -->
                                <tr v-for="spec in prog.specialisations" :key="spec.id" v-show="expandedProgrammes.includes(prog.id)" class="bg-white hover:bg-gray-50 transition-colors border-l-2 border-l-noun-green">
VUE;

$content = str_replace($templateSearch, $templateReplace, $content);

file_put_contents($file, $content);
echo "Patched Index.vue for accordion style\n";
