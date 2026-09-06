with open('app/Http/Controllers/Student/DashboardController.php', 'r') as f:
    content = f.read()

target = "return $pdf->stream('results-'.$application->application_number.'.pdf');"
replacement = "$safeAppNumber = str_replace(['/', '\\\\'], '-', $application->application_number);\n        return $pdf->stream('results-'.$safeAppNumber.'.pdf');"

if target in content:
    content = content.replace(target, replacement)
    with open('app/Http/Controllers/Student/DashboardController.php', 'w') as f:
        f.write(content)
    print("Patched PDF filename")
else:
    print("Target not found")
