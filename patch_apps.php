<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Applications/Index.vue';
$content = file_get_contents($file);

// 1. Add ENROLLED to the status badge
$statusSearch = <<<VUE
                                              'bg-green-100 text-noun-dark': app.status === 'ADMITTED',
                                              'bg-gray-100 text-gray-700': app.status === 'STARTED',
                                              'bg-red-100 text-red-800': app.status === 'REJECTED',
                                              'bg-purple-100 text-purple-800': app.status === 'SCREENING',
                                          }">
VUE;
$statusReplace = <<<VUE
                                              'bg-green-100 text-noun-dark': app.status === 'ADMITTED',
                                              'bg-gray-100 text-gray-700': app.status === 'STARTED',
                                              'bg-red-100 text-red-800': app.status === 'REJECTED',
                                              'bg-purple-100 text-purple-800': app.status === 'SCREENING',
                                              'bg-emerald-100 text-emerald-800': app.status === 'ENROLLED',
                                          }">
VUE;
$content = str_replace($statusSearch, $statusReplace, $content);

// 2. Button style for "Review"
$reviewSearch = <<<VUE
                                    <Link
                                        :href="route('admin.applications.show', app.id)"
                                        class="inline-flex items-center gap-1 text-noun-green hover:text-noun-dark font-semibold transition"
                                    >
                                        Review
                                        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </Link>
VUE;
$reviewReplace = <<<VUE
                                    <Link
                                        :href="route('admin.applications.show', app.id)"
                                        class="inline-flex items-center justify-center gap-1.5 px-3 py-1.5 bg-noun-green text-white font-semibold text-xs rounded-lg hover:bg-noun-dark transition shadow-sm"
                                    >
                                        Review
                                        <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                        </svg>
                                    </Link>
VUE;
$content = str_replace($reviewSearch, $reviewReplace, $content);

// 3. Make Application No stand out a bit more
$appNoSearch = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="text-sm font-mono font-medium text-gray-700">{{ app.application_number || '—' }}</span>
                                </td>
VUE;
$appNoReplace = <<<VUE
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="inline-flex items-center px-2.5 py-1 rounded-md bg-gray-100 border border-gray-200 text-xs font-mono font-bold text-gray-700">
                                        {{ app.application_number || '—' }}
                                    </span>
                                </td>
VUE;
$content = str_replace($appNoSearch, $appNoReplace, $content);

file_put_contents($file, $content);
echo "Patched Index.vue\n";
