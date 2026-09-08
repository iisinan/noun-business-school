<template>
    <GuestLayout>
        <Head title="Verify Email — NOUN Business School" />

        <!-- Envelope icon -->
        <div class="flex flex-col items-center text-center mb-6">
            <div class="w-16 h-16 rounded-2xl bg-noun-green/10 flex items-center justify-center mb-4 shadow-sm">
                <svg class="w-8 h-8 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8"
                        d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
            </div>
            <h2 class="text-2xl font-black text-gray-900 tracking-tight">Check your inbox</h2>
            <p class="mt-2 text-sm text-gray-500 leading-relaxed">
                We've sent a verification link to your email.<br>Click the link to activate your account.
            </p>
        </div>

        <!-- Spam warning -->
        <div class="flex gap-3 bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 mb-4">
            <svg class="w-4 h-4 text-amber-500 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 9v2m0 4h.01M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" />
            </svg>
            <p class="text-xs text-amber-800 leading-relaxed">
                <strong>Can't find it?</strong> Check your <strong>spam or junk folder</strong>.
                Look for an email from <em class="font-medium">admissions@noun.edu.ng</em>.
            </p>
        </div>

        <!-- Resend success -->
        <div
            v-if="verificationLinkSent"
            class="flex items-center gap-2 bg-green-50 border border-green-200 text-green-800 text-xs font-medium px-4 py-3 rounded-xl mb-4"
        >
            <svg class="w-4 h-4 flex-shrink-0 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            A new verification link has been sent — check your inbox (and spam folder).
        </div>

        <!-- Steps -->
        <div class="bg-gray-50 border border-gray-100 rounded-xl p-4 mb-5 space-y-3">
            <p class="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-1">What to do next</p>

            <div class="flex items-start gap-3">
                <span class="flex-shrink-0 w-6 h-6 rounded-full bg-noun-green text-white text-[11px] font-black flex items-center justify-center">1</span>
                <p class="text-sm text-gray-700 leading-snug pt-0.5">Open your email and find the message from <strong class="text-gray-900">NOUN Business School</strong></p>
            </div>

            <div class="flex items-start gap-3">
                <span class="flex-shrink-0 w-6 h-6 rounded-full bg-noun-green text-white text-[11px] font-black flex items-center justify-center">2</span>
                <p class="text-sm text-gray-700 leading-snug pt-0.5">Click the <strong class="text-gray-900">"Verify Email Address"</strong> button inside the email</p>
            </div>

            <div class="flex items-start gap-3">
                <span class="flex-shrink-0 w-6 h-6 rounded-full bg-noun-green text-white text-[11px] font-black flex items-center justify-center">3</span>
                <p class="text-sm text-gray-700 leading-snug pt-0.5">You'll be brought back automatically to continue your application</p>
            </div>
        </div>

        <!-- Resend button -->
        <form @submit.prevent="submit">
            <button
                type="submit"
                :disabled="form.processing || resendCooldown > 0"
                class="w-full flex items-center justify-center gap-2 py-3 rounded-xl border-2 border-noun-green text-noun-green font-bold text-sm hover:bg-noun-green hover:text-white transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                <svg v-if="form.processing" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                </svg>
                <svg v-else class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                <span v-if="form.processing">Sending…</span>
                <span v-else-if="resendCooldown > 0">Resend in {{ resendCooldown }}s</span>
                <span v-else>Resend Verification Email</span>
            </button>
        </form>

        <!-- Sign out -->
        <div class="mt-4 text-center">
            <Link
                :href="route('logout')"
                method="post"
                as="button"
                class="text-xs text-gray-400 hover:text-gray-600 transition underline underline-offset-2"
            >
                Sign out and use a different email
            </Link>
        </div>
    </GuestLayout>
</template>

<script setup>
import { computed, ref, onUnmounted } from 'vue';
import GuestLayout from '@/Layouts/GuestLayout.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

const props = defineProps({ status: { type: String } });
const form = useForm({});
const resendCooldown = ref(0);
let cooldownTimer = null;

const verificationLinkSent = computed(() => props.status === 'verification-link-sent');

const submit = () => {
    form.post(route('verification.send'), {
        onSuccess: () => {
            resendCooldown.value = 60;
            cooldownTimer = setInterval(() => {
                resendCooldown.value--;
                if (resendCooldown.value <= 0) clearInterval(cooldownTimer);
            }, 1000);
        },
    });
};

onUnmounted(() => { if (cooldownTimer) clearInterval(cooldownTimer); });
</script>
