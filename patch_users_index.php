<?php
$file = '/Users/sinan/Herd/Business School/resources/js/Pages/Admin/Users/Index.vue';
$content = file_get_contents($file);

$scriptSearch = "import { Head, Link, router } from '@inertiajs/vue3';";
$scriptReplace = <<<VUE
import { Head, Link, router } from '@inertiajs/vue3';

const deleteUser = (user) => {
    if (confirm(`Are you sure you want to delete user \${user.first_name} \${user.last_name}? This action cannot be undone.`)) {
        router.delete(route('admin.users.destroy', user.id), {
            preserveScroll: true
        });
    }
};
VUE;

$content = str_replace($scriptSearch, $scriptReplace, $content);

$btnSearch = '<button class="text-red-500 hover:text-red-700 transition font-semibold">Delete</button>';
$btnReplace = '<button @click="deleteUser(user)" class="text-red-500 hover:text-red-700 transition font-semibold">Delete</button>';

$content = str_replace($btnSearch, $btnReplace, $content);
file_put_contents($file, $content);
echo "Patched Users Index.vue\n";
