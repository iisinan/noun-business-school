<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Courses/Index.vue';
$content = file_get_contents($file);
$content = str_replace(
    '<th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Level & Semester</th>',
    '<th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Type</th>' . "\n" . '                                <th class="px-6 py-3 text-left text-xs font-semibold text-gray-500 uppercase tracking-wider">Level & Semester</th>',
    $content
);
$content = str_replace(
    '<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>',
    '<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ course.units }} Units</td>' . "\n" . '                                <td class="px-6 py-4 whitespace-nowrap">' . "\n" . '                                    <span v-if="course.type" class="px-2 py-1 text-xs font-bold rounded uppercase" :class="course.type === \'Core\' ? \'bg-indigo-100 text-indigo-700\' : \'bg-gray-100 text-gray-600\'">{{ course.type }}</span>' . "\n" . '                                </td>',
    $content
);
$content = str_replace('<td colspan="5"', '<td colspan="6"', $content);
file_put_contents($file, $content);
echo "Patched Course Index\n";
