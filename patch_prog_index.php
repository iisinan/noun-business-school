<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue';
$content = file_get_contents($file);

$search = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <button class="inline-flex items-center gap-1 text-noun-green hover:text-noun-dark font-semibold transition">
                                        Edit
                                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                                        </svg>
                                    </button>
                                </td>
VUE;

$replace = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap text-sm">
                                    <Link :href="route('admin.programmes.show', prog.id)" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm">
                                        Manage
                                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </Link>
                                </td>
VUE;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Index.vue\n";
