<?php
$files = glob('/Users/sinan/Herd/Business School/database/migrations/*_add_is_suspended_to_courses_table.php');
if (count($files) > 0) {
    $file = $files[0];
    $content = file_get_contents($file);
    $content = str_replace(
        "Schema::table('courses', function (Blueprint \$table) {",
        "Schema::table('courses', function (Blueprint \$table) {\n            \$table->boolean('is_suspended')->default(false)->after('type');",
        $content
    );
    $content = str_replace(
        "Schema::table('courses', function (Blueprint \$table) {\n            //\n        });",
        "Schema::table('courses', function (Blueprint \$table) {\n            \$table->dropColumn('is_suspended');\n        });",
        $content
    );
    file_put_contents($file, $content);
    echo "Patched migration\n";
} else {
    echo "Migration not found\n";
}
