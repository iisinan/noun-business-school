const fs = require('fs');

let content = fs.readFileSync('resources/js/Pages/Auth/Register.vue', 'utf8');

// Imports
content = content.replace("import PrimaryButton from '@/Components/PrimaryButton.vue';",
`import PrimaryButton from '@/Components/PrimaryButton.vue';
import SecondaryButton from '@/Components/SecondaryButton.vue';
import Modal from '@/Components/Modal.vue';`);

content = content.replace("import { Head, Link, useForm } from '@inertiajs/vue3';",
"import { Head, Link, useForm } from '@inertiajs/vue3';\nimport { ref } from 'vue';");

// Form init
content = content.replace("first_name: '',\n    last_name: '',",
"first_name: '',\n    middle_name: '',\n    last_name: '',");

// submit method
content = content.replace(
`const submit = () => {
    form.post(route('register'), {
        onFinish: () => form.reset('password', 'password_confirmation'),
    });
};`,
`const confirmingDetails = ref(false);

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
};`
);

// Grid change
content = content.replace('<div class="grid grid-cols-2 gap-4">', '<div class="grid grid-cols-1 sm:grid-cols-3 gap-4">');

// Add middle name input
const middleNameHtml = `
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
`;

content = content.replace('                <div>\n                    <InputLabel for="last_name"', middleNameHtml + '\n                <div>\n                    <InputLabel for="last_name"');

// Modal addition
const modalHtml = `
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
`;

content = content.replace('    </GuestLayout>\n</template>', modalHtml);

fs.writeFileSync('resources/js/Pages/Auth/Register.vue', content);
