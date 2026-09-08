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
        <Head title="Create Account — NOUN Business School" />

        <!-- Heading -->
        <div class="mb-7">
            <div class="inline-flex items-center gap-2 bg-noun-green/10 text-noun-green text-[10px] font-black uppercase tracking-widest px-3 py-1.5 rounded-full mb-3">
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                New Applicant
            </div>
            <h2 class="text-2xl font-black text-gray-900">Create your account</h2>
            <p class="mt-1 text-sm text-gray-500">Begin your application to NOUN Business School</p>
        </div>

        <form @submit.prevent="submit" class="space-y-5">

            <!-- Name row -->
            <div>
                <p class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">Full Name</p>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <div>
                        <InputLabel for="first_name" value="First" class="text-xs" />
                        <TextInput
                            id="first_name"
                            type="text"
                            class="mt-1 block w-full"
                            v-model="form.first_name"
                            required
                            autofocus
                            autocomplete="given-name"
                            placeholder="Ismaila"
                        />
                        <InputError class="mt-1" :message="form.errors.first_name" />
                    </div>
                    <div>
                        <InputLabel for="middle_name" value="Middle" class="text-xs" />
                        <TextInput
                            id="middle_name"
                            type="text"
                            class="mt-1 block w-full"
                            v-model="form.middle_name"
                            autocomplete="additional-name"
                            placeholder="Optional"
                        />
                        <InputError class="mt-1" :message="form.errors.middle_name" />
                    </div>
                    <div>
                        <InputLabel for="last_name" value="Last" class="text-xs" />
                        <TextInput
                            id="last_name"
                            type="text"
                            class="mt-1 block w-full"
                            v-model="form.last_name"
                            required
                            autocomplete="family-name"
                            placeholder="Sinan"
                        />
                        <InputError class="mt-1" :message="form.errors.last_name" />
                    </div>
                </div>
            </div>

            <!-- Phone -->
            <div>
                <InputLabel for="phone" value="Phone Number" />
                <div class="relative mt-1">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                        <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    </div>
                    <TextInput
                        id="phone"
                        type="tel"
                        class="block w-full pl-10"
                        v-model="form.phone"
                        required
                        autocomplete="tel"
                        placeholder="+234 800 000 0000"
                    />
                </div>
                <InputError class="mt-1" :message="form.errors.phone" />
            </div>

            <!-- Email -->
            <div>
                <InputLabel for="email" value="Email Address" />
                <div class="relative mt-1">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none">
                        <svg class="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                    </div>
                    <TextInput
                        id="email"
                        type="email"
                        class="block w-full pl-10"
                        v-model="form.email"
                        required
                        autocomplete="username"
                        placeholder="you@example.com"
                    />
                </div>
                <InputError class="mt-1" :message="form.errors.email" />
            </div>

            <!-- Divider -->
            <div class="flex items-center gap-3">
                <div class="flex-1 h-px bg-gray-100"></div>
                <span class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Security</span>
                <div class="flex-1 h-px bg-gray-100"></div>
            </div>

            <!-- Password -->
            <div>
                <InputLabel for="password" value="Password" />
                <PasswordInput
                    id="password"
                    class="mt-1 block w-full"
                    v-model="form.password"
                    required
                    autocomplete="new-password"
                    placeholder="Min. 8 characters"
                />
                <InputError class="mt-1" :message="form.errors.password" />
            </div>

            <!-- Confirm Password -->
            <div>
                <InputLabel for="password_confirmation" value="Confirm Password" />
                <PasswordInput
                    id="password_confirmation"
                    class="mt-1 block w-full"
                    v-model="form.password_confirmation"
                    required
                    autocomplete="new-password"
                    placeholder="Repeat your password"
                />
                <InputError class="mt-1" :message="form.errors.password_confirmation" />
            </div>

            <!-- Submit -->
            <div class="pt-1">
                <button
                    type="submit"
                    :disabled="form.processing"
                    class="w-full flex items-center justify-center gap-2 bg-noun-green hover:bg-noun-dark text-white font-bold py-3.5 rounded-xl transition-all duration-200 shadow-lg shadow-noun-green/25 hover:shadow-noun-dark/25 disabled:opacity-60 disabled:cursor-not-allowed text-sm"
                >
                    <svg v-if="form.processing" class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                    </svg>
                    <svg v-else class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
                    {{ form.processing ? 'Creating account…' : 'Create Account' }}
                </button>
            </div>

            <!-- Sign in link -->
            <p class="text-center text-sm text-gray-500">
                Already registered?
                <Link :href="route('login')" class="font-bold text-noun-green hover:text-noun-dark transition ml-1">
                    Sign in →
                </Link>
            </p>
        </form>

        <!-- Confirm modal -->
        <Modal :show="confirmingDetails" @close="closeModal">
            <div class="p-6">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-10 h-10 rounded-xl bg-noun-green/10 flex items-center justify-center flex-shrink-0">
                        <svg class="w-5 h-5 text-noun-green" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </div>
                    <div>
                        <h2 class="text-base font-black text-gray-900">Confirm Your Details</h2>
                        <p class="text-xs text-gray-500 mt-0.5">Your certificate will carry these exact names</p>
                    </div>
                </div>

                <div class="bg-amber-50 border border-amber-200 rounded-xl p-3 mb-4">
                    <p class="text-xs text-amber-800 font-semibold">⚠️ Your admission letter and certificate will carry these exact names. Please confirm they are correct.</p>
                </div>

                <div class="space-y-2 bg-gray-50 p-4 rounded-xl text-sm border border-gray-100">
                    <div class="flex justify-between"><span class="text-gray-500 font-semibold">First Name</span><span class="font-bold text-gray-900">{{ form.first_name }}</span></div>
                    <div v-if="form.middle_name" class="flex justify-between"><span class="text-gray-500 font-semibold">Middle Name</span><span class="font-bold text-gray-900">{{ form.middle_name }}</span></div>
                    <div class="flex justify-between"><span class="text-gray-500 font-semibold">Last Name</span><span class="font-bold text-gray-900">{{ form.last_name }}</span></div>
                    <div class="flex justify-between pt-2 border-t border-gray-200"><span class="text-gray-500 font-semibold">Email</span><span class="font-bold text-gray-900 text-xs">{{ form.email }}</span></div>
                    <div class="flex justify-between"><span class="text-gray-500 font-semibold">Phone</span><span class="font-bold text-gray-900">{{ form.phone }}</span></div>
                </div>

                <div class="mt-6 flex gap-3">
                    <SecondaryButton @click="closeModal" class="flex-1 justify-center">
                        ← Edit details
                    </SecondaryButton>
                    <PrimaryButton
                        class="flex-1 justify-center !bg-noun-green hover:!bg-noun-dark"
                        :class="{ 'opacity-25': form.processing }"
                        :disabled="form.processing"
                        @click="confirmAndRegister"
                    >
                        Confirm & Register
                    </PrimaryButton>
                </div>
            </div>
        </Modal>
    </GuestLayout>
</template>
