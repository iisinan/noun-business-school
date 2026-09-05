<?php
$files = [
    '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Programmes/Index.vue',
    '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Courses/Index.vue'
];

$tabsHtml = <<<HTML
        <div class="py-8">
            <div class="mx-auto w-full sm:px-6 lg:px-8">
                <!-- Inner Curriculum Tabs -->
                <div class="mb-6 border-b border-gray-200">
                    <nav class="-mb-px flex space-x-8" aria-label="Tabs">
                        <Link 
                            :href="route('admin.programmes.index')" 
                            :class="[route().current('admin.programmes.*') ? 'border-noun-green text-noun-green' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300', 'whitespace-nowrap py-4 px-1 border-b-2 font-bold text-sm transition']"
                        >
                            Programmes
                        </Link>
                        <Link 
                            :href="route('admin.courses.index')" 
                            :class="[route().current('admin.courses.*') ? 'border-noun-green text-noun-green' : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300', 'whitespace-nowrap py-4 px-1 border-b-2 font-bold text-sm transition']"
                        >
                            Course Bank
                        </Link>
                    </nav>
                </div>
HTML;

foreach ($files as $file) {
    $content = file_get_contents($file);
    // Remove "Manage Programmes" / "Manage Courses" title from header slot, replace with "Curriculum"
    $content = preg_replace('/<template #header>\s*<h2 class="text-xl font-semibold leading-tight text-gray-800">.*?<\/h2>\s*<\/template>/s', 
        "<template #header>\n            <h2 class=\"text-xl font-semibold leading-tight text-gray-800\">Curriculum Management</h2>\n        </template>", 
        $content);

    // Replace `<div class="py-8">\n            <div class="mx-auto w-full sm:px-6 lg:px-8">` with tabs
    $content = str_replace(
        "<div class=\"py-8\">\n            <div class=\"mx-auto w-full sm:px-6 lg:px-8\">", 
        $tabsHtml, 
        $content
    );
    file_put_contents($file, $content);
}
echo "Patched both files.\n";
