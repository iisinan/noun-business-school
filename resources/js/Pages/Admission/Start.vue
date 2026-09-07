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

const requiresSpecialisation = computed(() => {
    return selectedProgramme.value && selectedProgramme.value.specialisations.length > 0;
});

const canContinue = computed(() => {
    if (!form.value.programme_id) return false;
    if (requiresSpecialisation.value && !form.value.specialisation_id) return false;
    return true;
});

const continueUrl = computed(() => {
    if (!canContinue.value) return '#';
    let url = page.props.auth && page.props.auth.user ? route('applicant.application.create') : route('register');
    url += '?programme_id=' + form.value.programme_id;
    if (form.value.specialisation_id) {
        url += '&specialisation_id=' + form.value.specialisation_id;
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
            <p v-if="requiresSpecialisation && !form.specialisation_id" class="mb-3 text-xs text-amber-600 font-medium flex items-center gap-1.5">
                <svg class="w-4 h-4 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
                Please select a specialisation to continue.
            </p>
            <Link 
                :href="continueUrl"
                :class="[
                    'w-full flex justify-center items-center px-4 py-3 text-sm font-semibold rounded-lg transition-all', 
                    canContinue
                        ? 'bg-noun-green text-white hover:bg-noun-dark shadow-md hover:shadow-lg' 
                        : 'bg-gray-100 text-gray-400 cursor-not-allowed pointer-events-none'
                ]"
            >
                Continue to Application
            </Link>
        </div>
    </GuestLayout>
</template>
