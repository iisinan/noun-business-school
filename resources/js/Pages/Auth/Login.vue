<script setup>
import Checkbox from '@/Components/Checkbox.vue';
import GuestLayout from '@/Layouts/GuestLayout.vue';
import InputError from '@/Components/InputError.vue';
import InputLabel from '@/Components/InputLabel.vue';
import PrimaryButton from '@/Components/PrimaryButton.vue';
import TextInput from '@/Components/TextInput.vue';
import PasswordInput from '@/Components/PasswordInput.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';

defineProps({
    canResetPassword: {
        type: Boolean,
    },
    status: {
        type: String,
    },
});

const form = useForm({
    email: '',
    password: '',
    remember: true,
});

const submit = () => {
    form.post(route('login'), {
        onFinish: () => form.reset('password'),
    });
};
</script>

<template>
    <GuestLayout>
        <Head title="Log in" />

        <div class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900">Sign in</h2>
            <p class="mt-1.5 text-sm text-gray-500">Access your NOUN Business School portal</p>
        </div>

        <div v-if="status" class="mb-6 text-sm font-medium text-noun-green bg-noun-light px-4 py-3 rounded-lg border border-noun-green/20">
            {{ status }}
        </div>

        <form @submit.prevent="submit" class="space-y-5">
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
                    placeholder="Enter your email"
                />
                <InputError class="mt-2" :message="form.errors.email" />
            </div>

            <div>
                <div class="flex justify-between items-center mb-1">
                    <InputLabel for="password" value="Password" class="mb-0" />
                    <Link
                        v-if="canResetPassword"
                        :href="route('password.request')"
                        class="text-xs font-medium text-noun-green hover:text-noun-dark transition"
                    >
                        Forgot password?
                    </Link>
                </div>
                <PasswordInput
                    id="password"
                    class="block w-full"
                    v-model="form.password"
                    required
                    autocomplete="current-password"
                    placeholder="••••••••"
                />
                <InputError class="mt-2" :message="form.errors.password" />
            </div>

            <div class="flex items-center">
                <label class="flex items-center cursor-pointer">
                    <Checkbox name="remember" v-model:checked="form.remember" class="rounded border-gray-300 text-noun-green shadow-sm focus:ring-noun-green" />
                    <span class="ms-2 text-sm text-gray-600">Remember me for 30 days</span>
                </label>
            </div>

            <div class="pt-2">
                <PrimaryButton
                    class="w-full justify-center py-3 text-sm shadow-sm hover:shadow-md transition-all duration-200"
                    :class="{ 'opacity-70 cursor-not-allowed': form.processing }"
                    :disabled="form.processing"
                >
                    <svg v-if="form.processing" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    {{ form.processing ? 'Signing in...' : 'Sign in' }}
                </PrimaryButton>
            </div>


        </form>
    </GuestLayout>
</template>
