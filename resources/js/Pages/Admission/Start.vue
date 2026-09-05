<script setup>
import GuestLayout from '@/Layouts/GuestLayout.vue';
import { Head, Link } from '@inertiajs/vue3';
import { ref, computed } from 'vue';

import { usePage } from '@inertiajs/vue3';

const props = defineProps({
    programmes: Array,
});

const form = ref({
    programme_id: '',
    specialisation_id: '',
});

const page = usePage();

const selectedProgramme = computed(() => {
    return props.programmes.find(p => p.id === form.value.programme_id);
});

const programmeRequirements = computed(() => {
    if(!selectedProgramme.value) return [];
    return selectedProgramme.value.admission_requirements;
});

const continueUrl = computed(() => {
    let url = page.props.auth && page.props.auth.user ? route('applicant.application.create') : route('register');
    if (form.value.programme_id) {
        url += '?programme_id=' + form.value.programme_id;
        if (form.value.specialisation_id) {
            url += '&specialisation_id=' + form.value.specialisation_id;
        }
    }
    return url;
});
</script>

<template>
    <GuestLayout>
        <Head title="Apply for Admission" />

        <div class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900">Start Your Application</h2>
            <p class="mt-1.5 text-sm text-gray-500">Select a programme below to view its admission requirements before creating your account.</p>
        </div>

        <div class="space-y-5">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-1.5">Select Programme</label>
                <select v-model="form.programme_id" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5">
                    <option value="">Select a programme...</option>
                    <option v-for="prog in programmes" :key="prog.id" :value="prog.id">
                        {{ prog.name }}
                    </option>
                </select>
            </div>
            
            <div v-if="selectedProgramme && selectedProgramme.specialisations.length > 0">
                <label class="block text-sm font-medium text-gray-700 mb-1.5">Select Specialisation</label>
                <select v-model="form.specialisation_id" class="block w-full rounded-lg border-gray-300 shadow-sm focus:border-noun-green focus:ring-noun-green sm:text-sm py-2.5">
                    <option value="">Select a specialisation...</option>
                    <option v-for="spec in selectedProgramme.specialisations" :key="spec.id" :value="spec.id">
                        {{ spec.name }}
                    </option>
                </select>
            </div>
        </div>

        <div v-if="selectedProgramme" class="mt-6 bg-noun-light border border-noun-green/20 p-5 rounded-xl">
            <h4 class="text-sm font-bold text-noun-dark flex items-center gap-2">
                <svg class="h-4 w-4 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                Admission Requirements
            </h4>
            <ul class="list-disc list-outside ml-5 mt-3 space-y-2">
                <li v-for="req in programmeRequirements" :key="req.id" class="text-sm text-gray-700 leading-relaxed pl-1">
                    {{ req.description }}
                </li>
            </ul>
        </div>

        <div class="mt-8">
            <Link 
                :href="continueUrl"
                :class="[
                    'w-full flex justify-center items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all', 
                    form.programme_id 
                        ? 'bg-noun-green text-white hover:bg-noun-dark shadow-md hover:shadow-lg' 
                        : 'bg-gray-100 text-gray-400 cursor-not-allowed pointer-events-none'
                ]"
            >
                Continue to Application
            </Link>
        </div>
    </GuestLayout>
</template>
