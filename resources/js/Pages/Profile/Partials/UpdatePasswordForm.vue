<script setup>
import InputError from '@/Components/InputError.vue';
import InputLabel from '@/Components/InputLabel.vue';
import PrimaryButton from '@/Components/PrimaryButton.vue';
import TextInput from '@/Components/TextInput.vue';
import PasswordInput from '@/Components/PasswordInput.vue';
import { useForm } from '@inertiajs/vue3';
import { ref } from 'vue';

const passwordInput = ref(null);
const currentPasswordInput = ref(null);

const form = useForm({
    current_password: '',
    password: '',
    password_confirmation: '',
});

const updatePassword = () => {
    form.put(route('password.update'), {
        preserveScroll: true,
        onSuccess: () => form.reset(),
        onError: () => {
            if (form.errors.password) {
                form.reset('password', 'password_confirmation');
                passwordInput.value.focus();
            }
            if (form.errors.current_password) {
                form.reset('current_password');
                currentPasswordInput.value.focus();
            }
        },
    });
};
</script>

<template>
    <section>
        <header>
            <h2 class="text-lg font-medium text-gray-900">
                Update Password
            </h2>

            <p class="mt-1 text-sm text-gray-600">
                Ensure your account is using a long, random password to stay
                secure.
            </p>
        </header>

        <form @submit.prevent="updatePassword" class="mt-6 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="md:col-span-2 max-w-xl">
                    <InputLabel for="current_password" value="Current Password" class="text-sm font-medium text-gray-700" />

                    <PasswordInput
                        id="current_password"
                        ref="currentPasswordInput"
                        v-model="form.current_password"
                        class="mt-1.5 block w-full"
                        autocomplete="current-password"
                    />

                    <InputError :message="form.errors.current_password" class="mt-2" />
                </div>

                <div class="max-w-xl">
                    <InputLabel for="password" value="New Password" class="text-sm font-medium text-gray-700" />

                    <PasswordInput
                        id="password"
                        ref="passwordInput"
                        v-model="form.password"
                        class="mt-1.5 block w-full"
                        autocomplete="new-password"
                    />

                    <InputError :message="form.errors.password" class="mt-2" />
                </div>

                <div class="max-w-xl">
                    <InputLabel for="password_confirmation" value="Confirm Password" class="text-sm font-medium text-gray-700" />

                    <PasswordInput
                        id="password_confirmation"
                        v-model="form.password_confirmation"
                        class="mt-1.5 block w-full"
                        autocomplete="new-password"
                    />

                    <InputError :message="form.errors.password_confirmation" class="mt-2" />
                </div>
            </div>

            <div class="flex items-center gap-4">
                <PrimaryButton :disabled="form.processing">Update password</PrimaryButton>

                <Transition
                    enter-active-class="transition ease-in-out"
                    enter-from-class="opacity-0"
                    leave-active-class="transition ease-in-out"
                    leave-to-class="opacity-0"
                >
                    <p
                        v-if="form.recentlySuccessful"
                        class="flex items-center gap-1 text-sm font-medium text-noun-green"
                    >
                        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        Saved!
                    </p>
                </Transition>
            </div>
        </form>
    </section>
</template>
