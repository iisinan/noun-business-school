<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Sessions/Index.vue';
$content = file_get_contents($file);

$scriptSearch = <<<VUE
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, router } from '@inertiajs/vue3';
import { ref } from 'vue';
VUE;

$scriptReplace = <<<VUE
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, router } from '@inertiajs/vue3';
import { ref } from 'vue';
import Modal from '@/Components/Modal.vue';
VUE;
$content = str_replace($scriptSearch, $scriptReplace, $content);

$scriptSearch2 = <<<VUE
const toggleRegistration = (id, isOpen) => {
    const action = isOpen ? 'close' : 'open';
    if (confirm(`Are you sure you want to \${action} registration for this semester?`)) {
        router.post(route('admin.sessions.toggle-registration', id));
    }
};
</script>
VUE;

$scriptReplace2 = <<<VUE
const toggleRegistration = (id, isOpen) => {
    const action = isOpen ? 'close' : 'open';
    if (confirm(`Are you sure you want to \${action} registration for this semester?`)) {
        router.post(route('admin.sessions.toggle-registration', id));
    }
};

const deleteSession = (id) => {
    if (confirm('Are you sure you want to delete this session? This action cannot be undone.')) {
        router.delete(route('admin.sessions.destroy', id), {
            preserveScroll: true
        });
    }
};

const isEditModalOpen = ref(false);
const editingSession = ref(null);
const editForm = useForm({
    name: ''
});

const openEditModal = (session) => {
    editingSession.value = session;
    editForm.name = session.name;
    isEditModalOpen.value = true;
};

const submitEdit = () => {
    editForm.put(route('admin.sessions.update', editingSession.value.id), {
        onSuccess: () => {
            isEditModalOpen.value = false;
        }
    });
};
</script>
VUE;
$content = str_replace($scriptSearch2, $scriptReplace2, $content);

$tableSearch = <<<VUE
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
VUE;

$tableReplace = <<<VUE
                                        <div class="flex flex-col sm:flex-row items-end sm:items-center justify-end gap-2">
                                            <!-- Inactive Session Controls -->
                                            <template v-if="!session.is_active">
                                                <button @click="activateSession(session.id)" class="inline-flex items-center gap-1 text-noun-green hover:text-white border border-noun-green hover:bg-noun-green px-3 py-1.5 rounded-lg font-bold text-xs transition shadow-sm">
                                                    Make Active
                                                </button>
                                                <button @click="openEditModal(session)" class="text-gray-400 hover:text-noun-dark transition px-2">
                                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                                                </button>
                                                <button @click="deleteSession(session.id)" class="text-gray-400 hover:text-red-500 transition px-2">
                                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
                                                </button>
                                            </template>

                                            <!-- Active Session Controls -->
                                            <template v-else>
                                                <button 
                                                    @click="toggleRegistration(session.id, session.registration_open)" 
                                                    class="inline-flex items-center gap-1 text-xs font-bold border px-3 py-1.5 rounded-lg transition shadow-sm"
                                                    :class="session.registration_open ? 'border-red-200 text-red-600 bg-red-50 hover:bg-red-100' : 'border-emerald-200 text-emerald-600 bg-emerald-50 hover:bg-emerald-100'"
                                                >
                                                    {{ session.registration_open ? 'Close Reg' : 'Open Reg' }}
                                                </button>
                                                <button 
                                                    @click="advanceSemester(session.id, session.current_semester)" 
                                                    class="inline-flex items-center gap-1 text-xs font-bold border border-gray-200 text-gray-700 bg-white hover:bg-gray-50 px-3 py-1.5 rounded-lg transition shadow-sm"
                                                >
                                                    Advance Sem
                                                </button>
                                                <button @click="openEditModal(session)" class="text-gray-400 hover:text-noun-dark transition px-2 ml-2">
                                                    <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg>
                                                </button>
                                            </template>
                                        </div>
VUE;
$content = str_replace($tableSearch, $tableReplace, $content);

$modalAddition = <<<VUE
            </div>
        </div>

        <!-- Edit Modal -->
        <Modal :show="isEditModalOpen" @close="isEditModalOpen = false" maxWidth="sm">
            <div class="p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-4">Edit Session Name</h3>
                <form @submit.prevent="submitEdit">
                    <div class="mb-5">
                        <label class="block text-sm font-semibold text-gray-700 mb-1.5">Session Name</label>
                        <input v-model="editForm.name" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                        <p v-if="editForm.errors.name" class="mt-1 text-sm text-red-600">{{ editForm.errors.name }}</p>
                    </div>
                    <div class="flex items-center justify-end gap-3 mt-6">
                        <button type="button" @click="isEditModalOpen = false" class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg text-sm font-semibold hover:bg-gray-200 transition">Cancel</button>
                        <button type="submit" :disabled="editForm.processing" class="px-4 py-2 bg-noun-green text-white rounded-lg text-sm font-semibold hover:bg-noun-dark transition disabled:opacity-50">Save Changes</button>
                    </div>
                </form>
            </div>
        </Modal>

    </AdminLayout>
</template>
VUE;

$content = preg_replace('/<\/div>\s*<\/div>\s*<\/AdminLayout>\s*<\/template>/', $modalAddition, $content);
file_put_contents($file, $content);
echo "Patched Index.vue UI\n";
