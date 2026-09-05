import re

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'r') as f:
    content = f.read()

docket_method = """    /**
     * Generate the Application Docket (Printable HTML).
     */
    public function docket(Request $request)
    {
        $application = $request->user()->applications()->with(['programme', 'specialisation', 'academicSession'])->latest()->firstOrFail();
        return view('applicant.application-docket', compact('application'));
    }

    /**
     * Generate the Admission Letter (Printable HTML).
     */"""
content = content.replace("    /**\n     * Generate the Admission Letter (Printable HTML).\n     */", docket_method)

with open('app/Http/Controllers/Applicant/ApplicationController.php', 'w') as f:
    f.write(content)

