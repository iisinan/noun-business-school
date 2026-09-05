<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

const form = useForm({
    name: '',
    type: 'MBA',
    duration: 4,
    description: '',
    specialisations: [
        { name: '' }
    ]
});

const addSpecialisation = () => {
    form.specialisations.push({ name: '' });
};

const removeSpecialisation = (index) => {
    form.specialisations.splice(index, 1);
};

const submit = () => {
    form.post(route('admin.programmes.store'));
};
</script>

<template>
    <Head title="Create Programme" />
    <AdminLayout>
        <template #header>
            <div class="flex items-center gap-3">
                <Link :href="route('admin.programmes.index')" class="text-gray-500 hover:text-noun-green">
                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                </Link>
                <h2 class="text-xl font-semibold leading-tight text-gray-800">Create New Programme</h2>
            </div>
        </template>

        <div class="py-8">
            <div class="mx-auto max-w-4xl sm:px-6 lg:px-8">
                <form @submit.prevent="submit" class="bg-white shadow-sm rounded-xl border border-gray-100 overflow-hidden">
                    
                    <div class="p-6 border-b border-gray-100 bg-gray-50">
                        <h3 class="text-lg font-bold text-gray-900">Programme Details</h3>
                        <p class="text-sm text-gray-500">Define the core attributes of the new academic programme.</p>
                    </div>

                    <div class="p-6 space-y-6">
                        <!-- Name & Type -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="md:col-span-2">
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Programme Name</label>
                                <input v-model="form.name" type="text" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="e.g. Master of Business Administration">
                                <p v-if="form.errors.name" class="text-sm text-red-600 mt-1">{{ form.errors.name }}</p>
                            </div>
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Degree Type</label>
                                <select v-model="form.type" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                    <option value="PGD">Postgraduate Diploma (PGD)</option>
                                    <option value="MBA">Master of Business Admin (MBA)</option>
                                    <option value="MSc">Master of Science (MSc)</option>
                                    <option value="PhD">Doctor of Philosophy (PhD)</option>
                                </select>
                                <p v-if="form.errors.type" class="text-sm text-red-600 mt-1">{{ form.errors.type }}</p>
                            </div>
                        </div>

                        <!-- Duration & Description -->
                        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                            <div>
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Duration (Semesters)</label>
                                <input v-model="form.duration" type="number" min="1" max="10" required class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm">
                                <p v-if="form.errors.duration" class="text-sm text-red-600 mt-1">{{ form.errors.duration }}</p>
                            </div>
                            <div class="md:col-span-3">
                                <label class="block text-sm font-semibold text-gray-700 mb-1">Description (Optional)</label>
                                <textarea v-model="form.description" rows="2" class="block w-full border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="Brief overview of the programme..."></textarea>
                            </div>
                        </div>
                    </div>

                    <!-- Specialisations Builder -->
                    <div class="p-6 border-t border-gray-100 bg-gray-50">
                        <div class="flex items-center justify-between mb-4">
                            <div>
                                <h3 class="text-lg font-bold text-gray-900">Specialisation Tracks</h3>
                                <p class="text-sm text-gray-500">Add the various tracks applicants can choose from.</p>
                            </div>
                            <button type="button" @click="addSpecialisation" class="inline-flex items-center gap-1 bg-white border border-gray-300 text-gray-700 px-3 py-1.5 rounded-lg text-sm font-semibold hover:bg-gray-100 transition shadow-sm">
                                <svg class="h-4 w-4 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                                </svg>
                                Add Track
                            </button>
                        </div>

                        <div class="space-y-3">
                            <div v-for="(spec, index) in form.specialisations" :key="index" class="flex items-center gap-3 bg-white p-3 border border-gray-200 rounded-lg shadow-sm">
                                <span class="text-gray-400 font-bold w-6 text-center">{{ index + 1 }}.</span>
                                <input v-model="spec.name" type="text" required class="flex-1 border-gray-300 rounded-md focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="e.g. Human Resource Management">
                                <button type="button" @click="removeSpecialisation(index)" class="text-red-400 hover:text-red-600 p-2" title="Remove Track">
                                    <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Submit -->
                    <div class="px-6 py-4 border-t border-gray-100 bg-gray-100 flex items-center justify-end gap-3">
                        <Link :href="route('admin.programmes.index')" class="px-4 py-2 text-sm font-semibold text-gray-700 hover:text-gray-900">Cancel</Link>
                        <button type="submit" :disabled="form.processing" class="inline-flex items-center gap-2 bg-noun-green text-white px-5 py-2.5 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-md disabled:opacity-50">
                            Create Programme
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </AdminLayout>
</template>
