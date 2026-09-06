<?php
$file = '/Users/sinan/Herd/Business School/app/Http/Controllers/Student/DashboardController.php';
$content = file_get_contents($file);

$search = <<<PHP
    }
}
PHP;

$replace = <<<PHP
    }

    public function idCard(Request \$request)
    {
        \$user = \$request->user();
        \$application = \$user->applications()->with(['programme', 'specialisation'])->where('status', 'ENROLLED')->latest()->first();

        if (!\$application) {
            return redirect()->route('dashboard')->with('error', 'No active enrollment found to generate ID card.');
        }

        return Inertia::render('Student/IdCard', [
            'user' => \$user,
            'application' => \$application,
        ]);
    }
}
PHP;

$content = str_replace($search, $replace, $content);
file_put_contents($file, $content);
echo "Patched DashboardController\n";
