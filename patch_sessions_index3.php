<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Sessions/Index.vue';
$content = file_get_contents($file);

$scriptSearch = <<<VUE
const activateSession = (id) => {
    router.post(route('admin.sessions.activate', id));
};
</script>
VUE;

$scriptReplace = <<<VUE
const activateSession = (id) => {
    router.post(route('admin.sessions.activate', id));
};

const advanceSemester = (id, currentSem) => {
    if (confirm(`Are you sure you want to end Semester \${currentSem} and start Semester \${currentSem + 1}?`)) {
        router.post(route('admin.sessions.advance-semester', id));
    }
};

const toggleRegistration = (id, isOpen) => {
    const action = isOpen ? 'close' : 'open';
    if (confirm(`Are you sure you want to \${action} registration for this semester?`)) {
        router.post(route('admin.sessions.toggle-registration', id));
    }
};
</script>
VUE;

$content = str_replace($scriptSearch, $scriptReplace, $content);

$tableSearch = <<<VUE
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        <div>Apps: <span class="font-semibold">{{ session.total_applications || 0 }}</span></div>
                                        <div>Enrolled: <span class="font-semibold">{{ session.enrolled_students || 0 }}</span></div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span v-if="session.is_active" class="px-2.5 py-1 text-xs font-bold rounded-full bg-green-100 text-green-800">
                                            Active
                                        </span>
                                        <span v-else class="px-2.5 py-1 text-xs font-semibold rounded-full bg-gray-100 text-gray-600">
                                            Inactive
                                        </span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
                                        <button 
                                            v-if="!session.is_active"
                                            @click="activateSession(session.id)" 
                                            class="text-noun-green hover:text-noun-dark font-semibold border border-noun-green px-3 py-1.5 rounded-lg hover:bg-green-50 transition"
                                        >
                                            Activate
                                        </button>
                                        <span v-else class="text-gray-400 font-medium italic">Current</span>
                                    </td>
VUE;

$tableReplace = <<<VUE
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
VUE;

$content = str_replace($tableSearch, $tableReplace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue\n";
