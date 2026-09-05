<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, useForm, router } from '@inertiajs/vue3';
import { ref } from 'vue';
import Modal from '@/Components/Modal.vue';

defineProps({
    sessions: Array
});

const form = useForm({
    name: '',
    is_active: false
});

const submit = () => {
    form.post(route('admin.sessions.store'), {
        onSuccess: () => form.reset()
    });
};

const activateSession = (id) => {
    router.post(route('admin.sessions.activate', id));
};

const advanceSemester = (id, currentSem) => {
    if (confirm(`Are you sure you want to end Semester ${currentSem} and start Semester ${currentSem + 1}?`)) {
        router.post(route('admin.sessions.advance-semester', id));
    }
};

const toggleRegistration = (id, isOpen) => {
    const action = isOpen ? 'close' : 'open';
    if (confirm(`Are you sure you want to ${action} registration for this semester?`)) {
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

<template>
    <Head title="Academic Sessions" />
    <AdminLayout>
        <template #header>
            <h2 class="text-xl font-semibold leading-tight text-gray-800">Academic Sessions</h2>
        </template>

        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-3 gap-6">
                
                <!-- Create Form -->
                <div class="md:col-span-1">
                    <form @submit.prevent="submit" class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                        <div class="px-5 py-4 border-b border-gray-100 bg-gray-50">
                            <h3 class="text-base font-bold text-gray-900">Add New Session</h3>
                        </div>
                        <div class="p-5 space-y-4">
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
                        </div>
                    </form>
                </div>

                <!-- Sessions List -->
                <div class="md:col-span-2">
                    <div class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                        <div class="px-5 py-4 border-b border-gray-100 bg-gray-50">
                            <h3 class="text-base font-bold text-gray-900">All Sessions</h3>
                        </div>
                        <table class="min-w-full divide-y divide-gray-100">
                            <thead>
                                <tr class="bg-gray-50">
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Session</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Stats</th>
                                    <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Status</th>
                                    <th class="px-6 py-3 text-right text-xs font-semibold text-gray-500 uppercase tracking-wider">Action</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-50">
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
                                    </td>
                                </tr>
                                <tr v-if="!sessions.length">
                                    <td colspan="3" class="px-6 py-12 text-center text-gray-400 text-sm">No academic sessions found.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

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
