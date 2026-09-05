<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Programmes.vue';
$content = file_get_contents($file);

$content = str_replace('max-w-[90rem] mx-auto w-full px-4 sm:px-6 lg:px-8', 'w-full mx-auto px-2 sm:px-4 lg:px-6', $content);

file_put_contents($file, $content);
echo "Patched Programmes.vue layout 2\n";
