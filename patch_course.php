<?php
$file = '/Users/sinan/Herd/Business School/app/Models/Course.php';
$content = file_get_contents($file);
$content = str_replace("'title', 'units',", "'title', 'units', 'type',", $content);
file_put_contents($file, $content);
echo "Patched Course model\n";
