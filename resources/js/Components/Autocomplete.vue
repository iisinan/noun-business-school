<template>
  <div class="relative" ref="container">
    <div class="relative">
        <input 
            type="text" 
            :class="[baseClass, errorClass]" 
            v-model="query"
            @focus="isOpen = true"
            @input="handleInput"
            :placeholder="placeholder"
        />
        <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
            <svg class="h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
        </div>
    </div>
    
    <ul v-if="isOpen && filteredOptions.length > 0" class="absolute z-50 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
      <li 
        v-for="(option, index) in filteredOptions" 
        :key="index" 
        @mousedown.prevent="selectOption(option)"
        class="text-gray-900 cursor-pointer select-none relative py-2 pl-3 pr-3 hover:bg-noun-green hover:text-white transition-colors"
      >
        <span class="block truncate">{{ option }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';

const props = defineProps({
    modelValue: { type: String, default: '' },
    options: { type: Array, required: true },
    placeholder: { type: String, default: '' },
    errorClass: { type: String, default: 'border-gray-300' }
});

const emit = defineEmits(['update:modelValue']);

const query = ref(props.modelValue);
const isOpen = ref(false);
const container = ref(null);

const baseClass = "block w-full rounded-lg sm:text-sm shadow-sm focus:border-noun-green focus:ring-noun-green pl-3 pr-10";

const filteredOptions = computed(() => {
    if (!query.value) return props.options;
    return props.options.filter(option => 
        option.toLowerCase().includes(query.value.toLowerCase())
    );
});

const handleInput = () => {
    isOpen.value = true;
    emit('update:modelValue', query.value);
};

const selectOption = (option) => {
    query.value = option;
    emit('update:modelValue', option);
    isOpen.value = false;
};

// Sync from parent if modelValue changes externally
watch(() => props.modelValue, (newVal) => {
    if (newVal !== query.value) {
        query.value = newVal;
    }
});

const handleClickOutside = (event) => {
    if (container.value && !container.value.contains(event.target)) {
        isOpen.value = false;
    }
};

onMounted(() => {
    document.addEventListener('mousedown', handleClickOutside);
});

onUnmounted(() => {
    document.removeEventListener('mousedown', handleClickOutside);
});
</script>
