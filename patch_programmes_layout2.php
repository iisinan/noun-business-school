<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Programmes.vue';
$content = file_get_contents($file);

// Find the hero container
$content = str_replace('w-full max-w-[140rem] mx-auto px-4 sm:px-6 lg:px-10 xl:px-14', 'w-full mx-auto px-2 sm:px-4 lg:px-6', $content);

// In case the hero container has `w-full max-w-[140rem] mx-auto px-4 sm:px-6 lg:px-10 xl:px-14` but it has an extra `w-full` somehow:
$content = str_replace('w-full mx-auto w-full px-2 sm:px-4 lg:px-6', 'w-full mx-auto px-2 sm:px-4 lg:px-6', $content);

file_put_contents($file, $content);
echo "Patched Programmes.vue layout\n";
