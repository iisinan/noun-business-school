<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue';
$content = file_get_contents($file);

// Add import { ref } from 'vue';
if (strpos($content, "import { ref } from 'vue';") === false) {
    $content = str_replace("import { Head, Link, router } from '@inertiajs/vue3';", "import { Head, Link, router } from '@inertiajs/vue3';\nimport { ref } from 'vue';", $content);
}

// Add the expandedProgrammes logic right before defineProps
$logic = <<<VUE
const expandedProgrammes = ref([]);

const toggleExpand = (id) => {
    const index = expandedProgrammes.value.indexOf(id);
    if (index > -1) {
        expandedProgrammes.value.splice(index, 1);
    } else {
        expandedProgrammes.value.push(id);
    }
};

defineProps({
VUE;

if (strpos($content, "const expandedProgrammes = ref") === false) {
    $content = str_replace("defineProps({", $logic, $content);
}

file_put_contents($file, $content);
echo "Patched successfully\n";
