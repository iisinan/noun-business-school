<template>
    <GuestLayout>
        <Head title="Forgot Password" />

        <div class="mb-6">
            <h2 class="text-xl font-bold text-gray-900">Forgot password?</h2>
            <p class="mt-1 text-sm text-gray-500">Enter your email and we'll send you a reset link.</p>
        </div>

        <div v-if="status" class="mb-4 text-sm font-medium text-noun-green bg-green-50 px-4 py-3 rounded-lg border border-green-200">
            {{ status }}
        </div>

        <form @submit.prevent="submit">
            <div>
                <InputLabel for="email" value="Email address" />

                <TextInput
                    id="email"
                    type="email"
                    class="mt-1 block w-full"
                    v-model="form.email"
                    required
                    autofocus
                    autocomplete="username"
                />

                <InputError class="mt-2" :message="form.errors.email" />
            </div>

            <div class="mt-6">
                <PrimaryButton
                    class="w-full justify-center py-3"
                    :class="{ 'opacity-25': form.processing }"
                    :disabled="form.processing"
                >
                    Send Reset Link
                </PrimaryButton>
            </div>

            <div class="mt-5 text-center">
                <Link :href="route('login')" class="text-sm text-gray-500 hover:text-noun-green transition">
                    ← Back to sign in
                </Link>
            </div>
        </form>
    </GuestLayout>
</template>

<script setup>
import GuestLayout from '@/Layouts/GuestLayout.vue';
import InputError from '@/Components/InputError.vue';
import InputLabel from '@/Components/InputLabel.vue';
import PrimaryButton from '@/Components/PrimaryButton.vue';
import TextInput from '@/Components/TextInput.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

defineProps({ status: { type: String } });

const form = useForm({ email: '' });
const submit = () => form.post(route('password.email'));
</script>
