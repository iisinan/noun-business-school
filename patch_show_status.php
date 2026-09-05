<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Show.vue';
$content = file_get_contents($file);

$search = <<<VUE
                        <div class="flex items-center gap-2 mb-1">
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ programme.type }}</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-blue-100 text-blue-800 uppercase">{{ programme.duration }} Semesters</span>
                        </div>
VUE;

$replace = <<<VUE
                        <div class="flex items-center gap-2 mb-1">
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-noun-dark text-white uppercase">{{ programme.type }}</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md bg-blue-100 text-blue-800 uppercase">{{ programme.duration }} Semesters</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md uppercase"
                                  :class="programme.is_active ? 'bg-green-100 text-noun-dark' : 'bg-red-100 text-red-800'">
                                {{ programme.is_active ? 'Active' : 'Suspended' }}
                            </span>
                        </div>
VUE;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Show.vue\n";
