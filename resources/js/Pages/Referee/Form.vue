<script setup>
import { useForm, Head } from '@inertiajs/vue3';
import ApplicationLogo from '@/Components/ApplicationLogo.vue';

const props = defineProps({
    referee: Object,
});

const form = useForm({
    reference_content: '',
});

const submit = () => {
    form.post(route('referee.store', props.referee.token));
};
</script>

<template>
    <Head title="Submit Reference" />

    <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-3xl">
            <div class="flex justify-center">
                <ApplicationLogo class="h-16 w-auto" />
            </div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                Reference Submission
            </h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                NOUN Business School Admissions
            </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-3xl">
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10 border-t-4 border-noun-green">
                
                <div class="mb-6 bg-green-50 p-4 rounded-lg border border-green-100">
                    <h3 class="text-lg font-medium text-green-900">Applicant Details</h3>
                    <dl class="mt-2 text-sm text-green-800 grid grid-cols-1 md:grid-cols-2 gap-x-4 gap-y-2">
                        <div>
                            <dt class="font-bold">Applicant Name:</dt>
                            <dd>{{ referee.application.user.full_name }}</dd>
                        </div>
                        <div>
                            <dt class="font-bold">Programme Applied For:</dt>
                            <dd>{{ referee.application.programme.name }}</dd>
                        </div>
                    </dl>
                </div>

                <div class="mb-6">
                    <p class="text-sm text-gray-700 leading-relaxed">
                        Dear <strong>{{ referee.name }}</strong>,<br><br>
                        You have been listed as a referee by the applicant above. We would appreciate it if you could provide a candid evaluation of the applicant's academic/professional capabilities, character, and suitability for the chosen programme.
                    </p>
                </div>

                <form @submit.prevent="submit" class="space-y-6">
                    <div>
                        <label for="reference_content" class="block text-sm font-medium text-gray-700">
                            Reference Letter <span class="text-red-500">*</span>
                        </label>
                        <div class="mt-1">
                            <textarea id="reference_content" v-model="form.reference_content" rows="12" class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-noun-green focus:border-noun-green sm:text-sm" placeholder="Please write or paste your reference here..."></textarea>
                        </div>
                        <p v-if="form.errors.reference_content" class="mt-2 text-sm text-red-600">{{ form.errors.reference_content }}</p>
                        <p class="mt-2 text-xs text-gray-500">Minimum 50 characters required.</p>
                    </div>

                    <div>
                        <button type="submit" :disabled="form.processing" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-noun-green hover:bg-noun-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-noun-green disabled:opacity-50 transition-colors">
                            {{ form.processing ? 'Submitting...' : 'Submit Reference' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
