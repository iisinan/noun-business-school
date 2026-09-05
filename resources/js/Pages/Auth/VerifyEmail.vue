<template>
    <GuestLayout>
        <Head title="Email Verification" />

        <div class="mb-6 text-center">
            <div class="mx-auto h-14 w-14 rounded-full bg-green-50 flex items-center justify-center mb-4">
                <svg class="h-7 w-7 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
            </div>
            <h2 class="text-xl font-bold text-gray-900">Check your email</h2>
            <p class="mt-2 text-sm text-gray-500 leading-relaxed">
                Thanks for signing up! We've sent a verification link to your email. Click it to activate your account.
            </p>
        </div>

        <div
            class="mb-4 text-sm font-medium text-noun-green bg-green-50 px-4 py-3 rounded-lg border border-green-200"
            v-if="verificationLinkSent"
        >
            ✓ A new verification link has been sent to your email address.
        </div>

        <form @submit.prevent="submit">
            <PrimaryButton
                class="w-full justify-center py-3"
                :class="{ 'opacity-25': form.processing }"
                :disabled="form.processing"
            >
                Resend Verification Email
            </PrimaryButton>

            <div class="mt-4 text-center">
                <Link
                    :href="route('logout')"
                    method="post"
                    as="button"
                    class="text-sm text-gray-500 hover:text-noun-green transition focus:outline-none focus:ring-2 focus:ring-noun-green focus:ring-offset-2 rounded"
                >
                    Sign out
                </Link>
            </div>
        </form>
    </GuestLayout>
</template>

<script setup>
import { computed } from 'vue';
import GuestLayout from '@/Layouts/GuestLayout.vue';
import PrimaryButton from '@/Components/PrimaryButton.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

const props = defineProps({ status: { type: String } });
const form = useForm({});
const submit = () => form.post(route('verification.send'));
const verificationLinkSent = computed(() => props.status === 'verification-link-sent');
</script>
