<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue';
$content = file_get_contents($file);

// Ensure we import router
$scriptSearch = <<<VUE
<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link } from '@inertiajs/vue3';
VUE;

$scriptReplace = <<<VUE
<script setup>
import AdminLayout from '@/Layouts/AdminLayout.vue';
import { Head, Link, router } from '@inertiajs/vue3';

const toggleStatus = (id, currentStatus) => {
    const action = currentStatus ? 'suspend' : 'activate';
    if (confirm(`Are you sure you want to \${action} this programme?`)) {
        router.patch(route('admin.programmes.toggle-status', id), {}, {
            preserveScroll: true
        });
    }
};
VUE;

$content = str_replace($scriptSearch, $scriptReplace, $content);

$tableSearch = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full bg-green-100 text-noun-dark">Active</span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm">
                                        Manage
                                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </Link>
                                </td>
VUE;

$tableReplace = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2.5 py-1 inline-flex text-xs font-semibold rounded-full"
                                          :class="prog.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                        {{ prog.is_active ? 'Active' : 'Suspended' }}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <div class="flex items-center gap-2">
                                        <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm">
                                            Manage
                                            <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                            </svg>
                                        </Link>
                                        <button @click="toggleStatus(prog.id, prog.is_active)" class="inline-flex items-center gap-1.5 px-3 py-1.5 font-semibold text-xs rounded-lg transition shadow-sm border"
                                                :class="prog.is_active ? 'bg-white border-red-200 text-red-600 hover:bg-red-50' : 'bg-white border-green-200 text-green-600 hover:bg-green-50'">
                                            {{ prog.is_active ? 'Suspend' : 'Activate' }}
                                        </button>
                                    </div>
                                </td>
VUE;

$content = str_replace($tableSearch, $tableReplace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue table\n";
