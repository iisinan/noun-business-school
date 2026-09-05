<script setup>
import { computed } from 'vue';
import { Link } from '@inertiajs/vue3';

const props = defineProps({
    href: {
        type: String,
        required: true,
    },
    active: {
        type: Boolean,
    },
});

const classes = computed(() =>
    props.active
        ? 'inline-flex items-center px-3 py-2 rounded-md text-sm font-semibold text-white bg-noun-green transition duration-150 ease-in-out'
        : 'inline-flex items-center px-3 py-2 rounded-md text-sm font-medium text-green-200 hover:text-white hover:bg-noun-green transition duration-150 ease-in-out',
);
</script>

<template>
    <Link :href="href" :class="classes">
        <slot />
    </Link>
</template>
