<?php
$file = '/Users/sinan/Herd/Business School/app/Models/CourseRegistration.php';
$content = file_get_contents($file);
$content = str_replace("'academic_session_id',", "'academic_session_id', 'semester',", $content);
file_put_contents($file, $content);
echo "Patched Model\n";
