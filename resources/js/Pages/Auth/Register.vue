<script setup>
import GuestLayout from '@/Layouts/GuestLayout.vue';
import InputError from '@/Components/InputError.vue';
import InputLabel from '@/Components/InputLabel.vue';
import PrimaryButton from '@/Components/PrimaryButton.vue';
import SecondaryButton from '@/Components/SecondaryButton.vue';
import Modal from '@/Components/Modal.vue';
import TextInput from '@/Components/TextInput.vue';
import PasswordInput from '@/Components/PasswordInput.vue';
import { Head, Link, useForm } from '@inertiajs/vue3';
import { ref } from 'vue';

const urlParams = new URLSearchParams(window.location.search);

const form = useForm({
    first_name: '',
    middle_name: '',
    last_name: '',
    phone: '',
    email: '',
    password: '',
    password_confirmation: '',
    programme_id: urlParams.get('programme_id') || '',
    specialisation_id: urlParams.get('specialisation_id') || '',
});

const confirmingDetails = ref(false);

const submit = () => {
    confirmingDetails.value = true;
};

const confirmAndRegister = () => {
    form.post(route('register'), {
        onSuccess: () => {
            confirmingDetails.value = false;
        },
        onFinish: () => form.reset('password', 'password_confirmation'),
    });
};

const closeModal = () => {
    confirmingDetails.value = false;
};
</script>

<template>
    <GuestLayout>
        <Head title="Register" />

        <div class="mb-8">
            <h2 class="text-2xl font-bold text-gray-900">Create account</h2>
            <p class="mt-1.5 text-sm text-gray-500">Begin your application to NOUN Business School</p>
        </div>

        <form @submit.prevent="submit" class="space-y-5">
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div>
                    <InputLabel for="first_name" value="First Name" />
                    <TextInput
                        id="first_name"
                        type="text"
                        class="mt-1 block w-full"
                        v-model="form.first_name"
                        required
                        autofocus
                        autocomplete="given-name"
                    />
                    <InputError class="mt-2" :message="form.errors.first_name" />
                </div>


                <div>
                    <InputLabel for="middle_name" value="Middle Name (Optional)" />
                    <TextInput
                        id="middle_name"
                        type="text"
                        class="mt-1 block w-full"
                        v-model="form.middle_name"
                        autocomplete="additional-name"
                    />
                    <InputError class="mt-2" :message="form.errors.middle_name" />
                </div>

                <div>
                    <InputLabel for="last_name" value="Last Name" />
                    <TextInput
                        id="last_name"
                        type="text"
                        class="mt-1 block w-full"
                        v-model="form.last_name"
                        required
                        autocomplete="family-name"
                    />
                    <InputError class="mt-2" :message="form.errors.last_name" />
                </div>
            </div>

            <div>
                <InputLabel for="phone" value="Phone Number" />
                <TextInput
                    id="phone"
                    type="tel"
                    class="mt-1 block w-full"
                    v-model="form.phone"
                    required
                    autocomplete="tel"
                />
                <InputError class="mt-2" :message="form.errors.phone" />
            </div>

            <div>
                <InputLabel for="email" value="Email address" />
                <TextInput
                    id="email"
                    type="email"
                    class="mt-1 block w-full"
                    v-model="form.email"
                    required
                    autocomplete="username"
                />
                <InputError class="mt-2" :message="form.errors.email" />
            </div>

            <div>
                <InputLabel for="password" value="Password" />
                <PasswordInput
                    id="password"
                    class="mt-1 block w-full"
                    v-model="form.password"
                    required
                    autocomplete="new-password"
                />
                <InputError class="mt-2" :message="form.errors.password" />
            </div>

            <div>
                <InputLabel for="password_confirmation" value="Confirm Password" />
                <PasswordInput
                    id="password_confirmation"
                    class="mt-1 block w-full"
                    v-model="form.password_confirmation"
                    required
                    autocomplete="new-password"
                />
                <InputError class="mt-2" :message="form.errors.password_confirmation" />
            </div>

            <div class="pt-2">
                <PrimaryButton
                    class="w-full justify-center py-3 text-sm shadow-sm hover:shadow-md"
                    :class="{ 'opacity-25': form.processing }"
                    :disabled="form.processing"
                >
                    Create account
                </PrimaryButton>
            </div>

            <div class="mt-6 text-center text-sm text-gray-500">
                Already registered?
                <Link
                    :href="route('login')"
                    class="font-semibold text-noun-green hover:text-noun-dark transition ml-1"
                >
                    Sign in
                </Link>
            </div>
        </form>

        <Modal :show="confirmingDetails" @close="closeModal">
            <div class="p-6">
                <h2 class="text-lg font-bold text-gray-900">
                    Confirm Your Details
                </h2>

                <p class="mt-2 text-sm text-gray-600">
                    Are you sure you want to proceed with these details? <strong class="text-red-600">Your admission letter and certificate will carry these exact names.</strong>
                </p>

                <div class="mt-4 space-y-2 bg-gray-50 p-4 rounded-lg text-sm text-gray-800 border border-gray-100">
                    <div><span class="font-bold w-24 inline-block text-gray-500">First Name:</span> <span class="font-bold">{{ form.first_name }}</span></div>
                    <div v-if="form.middle_name"><span class="font-bold w-24 inline-block text-gray-500">Middle Name:</span> <span class="font-bold">{{ form.middle_name }}</span></div>
                    <div><span class="font-bold w-24 inline-block text-gray-500">Last Name:</span> <span class="font-bold">{{ form.last_name }}</span></div>
                    <div><span class="font-bold w-24 inline-block text-gray-500">Email:</span> <span class="font-bold">{{ form.email }}</span></div>
                    <div><span class="font-bold w-24 inline-block text-gray-500">Phone:</span> <span class="font-bold">{{ form.phone }}</span></div>
                </div>

                <div class="mt-6 flex justify-end">
                    <SecondaryButton @click="closeModal">
                        Cancel, let me edit
                    </SecondaryButton>

                    <PrimaryButton
                        class="ms-3 !bg-noun-green hover:!bg-noun-dark"
                        :class="{ 'opacity-25': form.processing }"
                        :disabled="form.processing"
                        @click="confirmAndRegister"
                    >
                        Proceed & Create Account
                    </PrimaryButton>
                </div>
            </div>
        </Modal>
    </GuestLayout>
</template>

