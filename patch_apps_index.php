<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Applications/Index.vue';
$content = file_get_contents($file);

// Replace script setup
$scriptSearch = <<<VUE
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link } from '@inertiajs/vue3';

defineProps({
    applications: Object
});
VUE;

$scriptReplace = <<<VUE
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';
import { ref, watch } from 'vue';

const props = defineProps({
    applications: Object,
    programmes: Array,
    filters: Object,
});

const search = ref(props.filters?.search || '');
const status = ref(props.filters?.status || '');
const programme_id = ref(props.filters?.programme_id || '');

let timeout = null;
watch([search, status, programme_id], ([newSearch, newStatus, newProgramme]) => {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => {
        router.get(
            route('admin.applications.index'),
            { search: newSearch, status: newStatus, programme_id: newProgramme },
            { preserveState: true, preserveScroll: true, replace: true }
        );
    }, 300);
});
VUE;
$content = str_replace($scriptSearch, $scriptReplace, $content);

// Replace the header area
$headerSearch = <<<VUE
                    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">All Applications</h3>
                            <span class="text-sm text-gray-500">{{ applications.total }} total</span>
                        </div>
                        <a :href="route('admin.applications.export')" class="inline-flex items-center gap-2 bg-white border border-gray-300 text-gray-700 px-4 py-2 rounded-lg text-sm font-semibold hover:bg-gray-50 transition shadow-sm">
                            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                            </svg>
                            Export CSV
                        </a>
                    </div>
VUE;

$headerReplace = <<<VUE
                    <div class="px-6 py-4 border-b border-gray-100 flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div>
                            <h3 class="text-base font-semibold text-gray-900">All Applications</h3>
                            <span class="text-sm text-gray-500">{{ applications.total }} total</span>
                        </div>
                        <div class="flex flex-col sm:flex-row items-center gap-3">
                            <input
                                v-model="search"
                                type="text"
                                placeholder="Search applicant..."
                                class="w-full sm:w-48 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green"
                            />
                            <select v-model="status" class="w-full sm:w-40 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green">
                                <option value="">All Statuses</option>
                                <option value="DRAFT">Draft</option>
                                <option value="SUBMITTED">Submitted</option>
                                <option value="UNDER REVIEW">Under Review</option>
                                <option value="SHORTLISTED">Shortlisted</option>
                                <option value="SCREENING">Screening</option>
                                <option value="RECOMMENDED">Recommended</option>
                                <option value="ADMITTED">Admitted</option>
                                <option value="REJECTED">Rejected</option>
                                <option value="ENROLLED">Enrolled</option>
                            </select>
                            <select v-model="programme_id" class="w-full sm:w-48 text-sm border-gray-300 rounded-lg focus:ring-noun-green focus:border-noun-green">
                                <option value="">All Programmes</option>
                                <option v-for="prog in programmes" :key="prog.id" :value="prog.id">{{ prog.name }}</option>
                            </select>
                            <a :href="route('admin.applications.export')" class="shrink-0 inline-flex items-center gap-2 bg-white border border-gray-300 text-gray-700 px-4 py-2 rounded-lg text-sm font-semibold hover:bg-gray-50 transition shadow-sm">
                                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                                </svg>
                                Export CSV
                            </a>
                        </div>
                    </div>
VUE;

$content = str_replace($headerSearch, $headerReplace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue\n";
