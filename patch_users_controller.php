<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/UsersController.php';
$content = file_get_contents($file);

$destroyMethod = <<<PHP
    public function destroy(User \$user)
    {
        // Don't allow super admin to delete themselves
        if (auth()->id() === \$user->id) {
            return back()->with('error', 'You cannot delete yourself.');
        }

        \$user->delete();

        return redirect()->route('admin.users.index')->with('success', 'User deleted successfully.');
    }
}
PHP;

$content = preg_replace('/}\s*$/', "\n$destroyMethod\n", $content);
file_put_contents($file, $content);
echo "Patched UsersController\n";
