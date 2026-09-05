<?php
$file = '/Users/sinan/Herd/Business School/app/Models/Specialisation.php';
$content = file_get_contents($file);

$search = <<<PHP
class Specialisation extends Model
{
    //
    public function courses()
PHP;

$replace = <<<PHP
class Specialisation extends Model
{
    protected \$guarded = [];

    public function programme()
    {
        return \$this->belongsTo(Programme::class);
    }

    public function courses()
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched Specialisation.php\n";
