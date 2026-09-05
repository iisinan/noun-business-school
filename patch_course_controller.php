<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/CourseController.php';
$content = file_get_contents($file);
$content = str_replace("'title' => 'required|string|max:255',", "'title' => 'required|string|max:255',\n            'type' => 'required|string|in:Core,Elective',", $content);
file_put_contents($file, $content);
echo "Patched CourseController\n";
