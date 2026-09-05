<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Programmes.vue';
$content = file_get_contents($file);

// Replace the max-w classes to remove extra spaces at ends
$content = str_replace('max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8', 'w-full max-w-[140rem] mx-auto px-4 sm:px-6 lg:px-10 xl:px-14', $content);

// Replace grid classes to reduce card sizes (more columns = smaller cards)
$content = str_replace('grid sm:grid-cols-2 xl:grid-cols-3 gap-5', 'grid sm:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-5 gap-4', $content);

// Reduce padding inside the cards
$content = str_replace('class="relative bg-white border border-gray-100 rounded-2xl p-4 sm:p-5', 'class="relative bg-white border border-gray-100 rounded-2xl p-3 sm:p-4', $content);

// Make icon slightly smaller
$content = str_replace('w-10 h-10 rounded-xl bg-noun-green/8', 'w-8 h-8 rounded-lg bg-noun-green/8', $content);
$content = str_replace('class="w-5 h-5 text-noun-green"', 'class="w-4 h-4 text-noun-green"', $content);

// Shrink header text inside the card slightly
$content = str_replace('text-base font-bold text-noun-dark mb-3', 'text-sm font-bold text-noun-dark mb-2', $content);

// Shrink meta pills margin
$content = str_replace('class="flex flex-wrap gap-2 mb-4"', 'class="flex flex-wrap gap-1.5 mb-3"', $content);

file_put_contents($file, $content);
echo "Patched Programmes.vue layout\n";
