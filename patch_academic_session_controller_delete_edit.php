<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Admin/AcademicSessionController.php';
$content = file_get_contents($file);

$additions = <<<PHP

    public function update(Request \$request, AcademicSession \$session)
    {
        \$request->validate([
            'name' => 'required|string|unique:academic_sessions,name,' . \$session->id,
        ]);

        \$session->update(['name' => \$request->name]);
        return redirect()->route('admin.sessions.index')->with('success', 'Session updated successfully.');
    }

    public function destroy(AcademicSession \$session)
    {
        if (\$session->is_active) {
            return back()->with('error', 'Cannot delete the currently active session.');
        }

        if (\$session->applications()->count() > 0) {
            return back()->with('error', 'Cannot delete a session that already has applications attached to it.');
        }

        \$session->delete();
        return redirect()->route('admin.sessions.index')->with('success', 'Session deleted successfully.');
    }
}
PHP;

$content = preg_replace('/\}\s*$/', $additions, $content);
file_put_contents($file, $content);
echo "Patched AcademicSessionController\n";
