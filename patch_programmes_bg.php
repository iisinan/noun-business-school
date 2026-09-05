<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Programmes.vue';
$content = file_get_contents($file);

$search = <<<VUE
            <!-- Programmes Directory -->
            <section id="programmes-directory" class="py-16 lg:py-0 relative bg-gray-50/50 lg:flex-grow lg:flex lg:flex-col lg:overflow-hidden w-full">
                <div class="w-full mx-auto px-2 sm:px-4 lg:px-6 lg:h-full lg:flex lg:flex-col lg:overflow-hidden lg:py-10">
VUE;

$replace = <<<VUE
            <!-- Programmes Directory -->
            <section id="programmes-directory" class="py-16 lg:py-0 relative bg-gray-50/80 lg:flex-grow lg:flex lg:flex-col lg:overflow-hidden w-full">
                
                <!-- Decorative Background -->
                <div class="absolute inset-0 z-0 overflow-hidden pointer-events-none">
                    <div class="absolute -top-[30%] -right-[10%] w-[1000px] h-[1000px] bg-noun-green/5 rounded-full blur-[120px]"></div>
                    <div class="absolute top-[40%] -left-[10%] w-[800px] h-[800px] bg-noun-yellow/5 rounded-full blur-[100px]"></div>
                    <div class="absolute -bottom-[20%] right-[20%] w-[600px] h-[600px] bg-noun-green/5 rounded-full blur-[100px]"></div>
                    <div class="absolute inset-0 opacity-[0.4]" style="background-image: radial-gradient(rgba(0, 77, 0, 0.15) 1.5px, transparent 1.5px); background-size: 32px 32px;"></div>
                </div>

                <div class="w-full mx-auto px-2 sm:px-4 lg:px-6 lg:h-full lg:flex lg:flex-col lg:overflow-hidden lg:py-10 relative z-10">
VUE;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Programmes.vue background\n";
