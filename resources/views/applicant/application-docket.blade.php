<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Docket - {{ $application->application_number }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @media print {
            body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            .no-print { display: none !important; }
            .page-break { page-break-before: always; }
        }
        .noun-green { color: #006600; }
        .bg-noun-green { background-color: #006600; }
    </style>
</head>
<body class="bg-gray-100 font-sans text-gray-800 text-sm">
    <div class="max-w-4xl mx-auto bg-white p-10 md:p-12 my-10 shadow-xl print:shadow-none print:m-0 print:p-8">
        
        <!-- Header -->
        <div class="flex flex-col items-center border-b-4 border-[#006600] pb-6 mb-8 text-center">
            <img src="/nbs-logo.png" alt="NOUN Logo" class="h-20 w-auto object-contain mb-3" onerror="this.src='https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/National_Open_University_of_Nigeria_logo.png/220px-National_Open_University_of_Nigeria_logo.png'">
            <h1 class="text-2xl font-black noun-green uppercase tracking-wide">National Open University of Nigeria</h1>
            <h2 class="text-lg font-bold text-gray-700">Business School (NBS)</h2>
            <p class="text-xs text-gray-500 mt-1">Application Summary (Docket)</p>
        </div>

        <div class="flex justify-between items-start mb-6">
            <div>
                <h3 class="font-bold text-xl">{{ $application->programme->name }}</h3>
                @if($application->specialisation)
                <p class="text-gray-600 font-semibold">Specialisation: {{ $application->specialisation->name }}</p>
                @endif
                <div class="mt-4">
                    <p class="text-xs text-gray-500 uppercase">Application No</p>
                    <p class="font-bold text-lg font-mono">{{ $application->application_number }}</p>
                    <p class="text-xs mt-1">Submitted: {{ $application->created_at->format('M j, Y') }}</p>
                </div>
            </div>
            <div class="text-right">
                @if(isset($application->personal_info['passport_photograph_path']))
                <div class="h-32 w-32 border border-gray-300 p-1 bg-white ml-auto">
                    <img src="{{ \Illuminate\Support\Facades\Storage::disk('s3')->url($application->personal_info['passport_photograph_path']) }}" class="h-full w-full object-cover" alt="Passport">
                </div>
                @else
                <div class="h-32 w-32 border border-gray-300 p-1 bg-gray-50 ml-auto flex items-center justify-center text-xs text-gray-400 text-center">
                    Passport<br>Photograph
                </div>
                @endif
            </div>
        </div>

        <!-- Section 1: Personal Info -->
        <div class="mb-8">
            <h4 class="bg-gray-200 text-gray-800 font-bold px-4 py-2 uppercase text-xs tracking-wider mb-4 border-l-4 border-[#006600]">1. Personal Information</h4>
            <div class="grid grid-cols-2 gap-y-4 gap-x-8 px-4">
                <div><span class="text-gray-500 text-xs block">Full Name</span><span class="font-semibold">{{ $application->personal_info['full_name'] ?? $application->user->first_name . ' ' . $application->user->last_name }}</span></div>
                <div><span class="text-gray-500 text-xs block">Email Address</span><span class="font-semibold">{{ $application->user->email }}</span></div>
                <div><span class="text-gray-500 text-xs block">Phone Number</span><span class="font-semibold">{{ $application->personal_info['phone'] ?? 'N/A' }}</span></div>
                <div><span class="text-gray-500 text-xs block">Date of Birth</span><span class="font-semibold">{{ $application->personal_info['dob'] ?? 'N/A' }}</span></div>
                <div><span class="text-gray-500 text-xs block">Gender</span><span class="font-semibold">{{ $application->personal_info['gender'] === 'M' ? 'Male' : 'Female' }}</span></div>
                <div><span class="text-gray-500 text-xs block">Marital Status</span><span class="font-semibold">{{ $application->personal_info['marital_status'] ?? 'N/A' }}</span></div>
                <div><span class="text-gray-500 text-xs block">Nationality</span><span class="font-semibold">{{ $application->personal_info['nationality'] ?? 'N/A' }}</span></div>
                <div><span class="text-gray-500 text-xs block">State of Origin</span><span class="font-semibold">{{ $application->personal_info['state_of_origin'] ?? 'N/A' }}</span></div>
                <div class="col-span-2"><span class="text-gray-500 text-xs block">Residential Address</span><span class="font-semibold">{{ $application->personal_info['address'] ?? 'N/A' }}</span></div>
            </div>
        </div>

        <!-- Section 2: Academic Background -->
        <div class="mb-8">
            <h4 class="bg-gray-200 text-gray-800 font-bold px-4 py-2 uppercase text-xs tracking-wider mb-4 border-l-4 border-[#006600]">2. Academic Background</h4>
            @if(is_array($application->academic_background) && count($application->academic_background) > 0)
                <div class="px-4">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b-2 border-gray-300">
                                <th class="py-2 text-xs text-gray-500">Institution</th>
                                <th class="py-2 text-xs text-gray-500">Qualification</th>
                                <th class="py-2 text-xs text-gray-500">Course of Study</th>
                                <th class="py-2 text-xs text-gray-500">Grade</th>
                                <th class="py-2 text-xs text-gray-500">Year</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach($application->academic_background as $edu)
                            <tr class="border-b border-gray-100">
                                <td class="py-2 font-semibold">{{ $edu['institution'] }}</td>
                                <td class="py-2">{{ $edu['qualification'] }}</td>
                                <td class="py-2">{{ $edu['course_of_study'] }}</td>
                                <td class="py-2">{{ $edu['grade'] }}</td>
                                <td class="py-2">{{ $edu['graduation_year'] }}</td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
            @else
                <p class="px-4 text-gray-500 italic">No academic records provided.</p>
            @endif
        </div>

        <!-- Section 3: OLevel Results -->
        <div class="mb-8">
            <h4 class="bg-gray-200 text-gray-800 font-bold px-4 py-2 uppercase text-xs tracking-wider mb-4 border-l-4 border-[#006600]">3. O'Level Results</h4>
            @if(is_array($application->olevel_results) && count($application->olevel_results) > 0)
                <div class="px-4 grid grid-cols-2 gap-8">
                    @foreach($application->olevel_results as $sitting)
                        <div>
                            <p class="font-bold border-b pb-1 mb-2">{{ $sitting['exam_type'] ?? '' }} ({{ $sitting['exam_year'] ?? '' }}) - No: {{ $sitting['exam_number'] ?? '' }}</p>
                            <table class="w-full text-sm">
                                <tbody>
                                    @foreach($sitting['subjects'] as $sub)
                                        @if(!empty($sub['name']) && !empty($sub['grade']))
                                        <tr>
                                            <td class="py-1">{{ $sub['name'] }}</td>
                                            <td class="py-1 font-bold text-right">{{ $sub['grade'] }}</td>
                                        </tr>
                                        @endif
                                    @endforeach
                                </tbody>
                            </table>
                        </div>
                    @endforeach
                </div>
            @else
                <p class="px-4 text-gray-500 italic">Not required/provided for this programme.</p>
            @endif
        </div>

        <!-- Section 4: Employment History -->
        <div class="mb-8">
            <h4 class="bg-gray-200 text-gray-800 font-bold px-4 py-2 uppercase text-xs tracking-wider mb-4 border-l-4 border-[#006600]">4. Employment Details</h4>
            @if(is_array($application->employment_info))
                <div class="grid grid-cols-3 gap-4 px-4">
                    <div><span class="text-gray-500 text-xs block">Organisation</span><span class="font-semibold">{{ $application->employment_info['organisation'] ?? 'N/A' }}</span></div>
                    <div><span class="text-gray-500 text-xs block">Job Title</span><span class="font-semibold">{{ $application->employment_info['job_title'] ?? 'N/A' }}</span></div>
                    <div><span class="text-gray-500 text-xs block">Years of Exp.</span><span class="font-semibold">{{ $application->employment_info['years_experience'] ?? 'N/A' }} Years</span></div>
                </div>
            @else
                <p class="px-4 text-gray-500 italic">Not required/provided for this programme.</p>
            @endif
        </div>

        <!-- Declaration -->
        <div class="mt-12 border-t pt-8">
            <h4 class="font-bold mb-2">Applicant's Declaration</h4>
            <p class="text-xs text-justify text-gray-600 mb-6">I hereby declare that all the information provided in this application form is true and correct to the best of my knowledge. I understand that any false information or falsified documents will lead to automatic disqualification and withdrawal of admission offer at any time it is discovered.</p>
            

        </div>

        <!-- Print Action -->
        <div class="mt-16 text-center no-print">
            <button onclick="window.print()" class="bg-[#006600] hover:bg-green-700 text-white font-bold py-2.5 px-6 rounded shadow transition-colors flex items-center gap-2 mx-auto">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                Print Docket
            </button>
        </div>
    </div>
</body>
</html>
