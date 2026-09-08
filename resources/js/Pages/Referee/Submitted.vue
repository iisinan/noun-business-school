<script setup>
import { Head, Link } from '@inertiajs/vue3';
import ApplicationLogo from '@/Components/ApplicationLogo.vue';
</script>

<template>
    <Head title="Reference Submitted" />

    <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <div class="flex justify-center">
                <ApplicationLogo class="h-16 w-auto" />
            </div>
            
            <div class="mt-8 bg-white py-12 px-4 shadow sm:rounded-lg sm:px-10 text-center border-t-4 border-noun-green">
                <div class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-green-100 mb-6">
                    <svg class="h-8 w-8 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                </div>
                
                <h2 class="text-2xl font-extrabold text-gray-900 mb-2">
                    Reference Submitted Successfully
                </h2>
                <p class="text-sm text-gray-600 mb-8">
                    Thank you for your time and effort. Your reference has been securely recorded and will be used by the Admissions Team to evaluate the applicant.
                </p>

                <a href="https://nounbusinessschool.edu.ng" class="inline-flex items-center text-sm font-medium text-noun-green hover:text-noun-dark">
                    &larr; Return to NOUN Business School Website
                </a>
            </div>
        </div>
    </div>
</template>
