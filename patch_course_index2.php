<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Courses/Index.vue';
$content = file_get_contents($file);

// Replace script setup
$scriptSearch = <<<VUE
<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';

const props = defineProps({
    courses: Object,
    filters: Object,
});

const search = ref(props.filters.search || '');

watch(search, (value) => {
    router.get(
        route('admin.courses.index'),
        { search: value },
        { preserveState: true, preserveScroll: true, replace: true }
    );
});
</script>
VUE;

$scriptReplace = <<<VUE
<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';

const props = defineProps({
    courses: Object,
    programmes: Array,
    filters: Object,
});

const search = ref(props.filters?.search || '');
const programme_id = ref(props.filters?.programme_id || '');

watch([search, programme_id], ([newSearch, newProg]) => {
    router.get(
        route('admin.courses.index'),
        { search: newSearch, programme_id: newProg },
        { preserveState: true, preserveScroll: true, replace: true }
    );
});
</script>
VUE;

$content = str_replace($scriptSearch, $scriptReplace, $content);

$headerSearch = <<<VUE
                <div class="bg-white p-4 shadow-sm rounded-xl border border-gray-100 mb-6 flex justify-between items-center">
                    <div class="w-full sm:w-1/3">
                        <input
                            v-model="search"
                            type="text"
                            class="block w-full px-3 py-2 border border-gray-300 rounded-lg bg-white sm:text-sm focus:ring-noun-green focus:border-noun-green"
                            placeholder="Search by course code or title..."
                        >
                    </div>
                    <Link :href="route('admin.courses.create')" class="bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                        + Add Course
                    </Link>
                </div>
VUE;

$headerReplace = <<<VUE
                <div class="bg-white p-4 shadow-sm rounded-xl border border-gray-100 mb-6 flex flex-col md:flex-row justify-between items-center gap-4">
                    <div class="w-full md:w-2/3 flex flex-col sm:flex-row gap-3">
                        <input
                            v-model="search"
                            type="text"
                            class="block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg bg-white sm:text-sm focus:ring-noun-green focus:border-noun-green"
                            placeholder="Search by course code or title..."
                        >
                        <select v-model="programme_id" class="block w-full sm:w-1/2 px-3 py-2 border border-gray-300 rounded-lg bg-white sm:text-sm focus:ring-noun-green focus:border-noun-green">
                            <option value="">All Programmes</option>
                            <option v-for="prog in programmes" :key="prog.id" :value="prog.id">{{ prog.name }}</option>
                        </select>
                    </div>
                    <Link :href="route('admin.courses.create')" class="shrink-0 bg-noun-green text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-noun-dark transition shadow-sm">
                        + Add Course
                    </Link>
                </div>
VUE;

$content = str_replace($headerSearch, $headerReplace, $content);
file_put_contents($file, $content);
echo "Patched Courses/Index.vue\n";
