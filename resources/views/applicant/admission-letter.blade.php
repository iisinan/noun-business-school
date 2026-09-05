<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admission Letter - {{ $application->application_number }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @media print {
            body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            .no-print { display: none !important; }
        }
        .noun-green { color: #006600; }
        .bg-noun-green { background-color: #006600; }
    </style>
</head>
<body class="bg-gray-100 font-sans text-gray-800">
    <div class="max-w-3xl mx-auto bg-white p-10 md:p-16 my-10 shadow-xl print:shadow-none print:m-0 print:p-8">
        
        <!-- Header -->
        <div class="flex items-center justify-between border-b-4 border-[#006600] pb-6 mb-8">
            <div class="flex items-center gap-4">
                <img src="/nbs-logo.png" alt="NOUN Logo" class="h-20 w-auto object-contain" onerror="this.src='https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/National_Open_University_of_Nigeria_logo.png/220px-National_Open_University_of_Nigeria_logo.png'">
                <div>
                    <h1 class="text-2xl font-black noun-green uppercase tracking-wide">National Open University of Nigeria</h1>
                    <h2 class="text-xl font-bold text-gray-700">Business School (NBS)</h2>
                    <p class="text-xs text-gray-500 mt-1">University Village, Plot 91, Cadastral Zone, Nnamdi Azikiwe Expressway, Jabi, Abuja.</p>
                </div>
            </div>
        </div>

        <!-- Meta info -->
        <div class="flex justify-between items-start mb-8 text-sm">
            <div>
                <p><strong>Ref:</strong> NBS/ADM/{{ date('Y') }}/{{ str_pad($application->id, 4, '0', STR_PAD_LEFT) }}</p>
                <p class="mt-1"><strong>Date:</strong> {{ date('F j, Y') }}</p>
            </div>
            <div class="text-right">
                <p><strong>Matriculation No:</strong> NBS/{{ $application->academic_session_id }}/{{ str_pad($application->id, 4, '0', STR_PAD_LEFT) }}</p>
                <p class="mt-1"><strong>Application No:</strong> {{ $application->application_number }}</p>
            </div>
        </div>

        <!-- Addressee -->
        <div class="mb-8">
            <p class="font-bold text-lg">{{ $application->user->first_name }} {{ $application->user->last_name }}</p>
            <p>{{ $application->personal_info['address'] ?? 'Applicant Address' }}</p>
            <p>{{ $application->personal_info['state_of_origin'] ?? '' }}, {{ $application->personal_info['nationality'] ?? '' }}</p>
        </div>

        <!-- Title -->
        <h3 class="text-center font-bold underline text-lg mb-8 uppercase tracking-wide">Provisional Offer of Admission into {{ $application->academicSession->name ?? date('Y').'/'.(date('Y')+1) }} Academic Session</h3>

        <!-- Body -->
        <div class="space-y-4 text-justify leading-relaxed">
            <p>Dear {{ $application->user->first_name }},</p>
            
            <p>I am pleased to inform you that following your application and subsequent screening, you have been offered provisional admission into the NOUN Business School to pursue a programme of study leading to the award of:</p>
            
            <div class="bg-gray-50 p-4 rounded border border-gray-200 text-center my-4 shadow-inner">
                <p class="font-bold text-xl noun-green">{{ $application->programme->name }}</p>
                @if($application->specialisation)
                <p class="font-semibold text-gray-700 mt-1">Specialisation in {{ $application->specialisation->name }}</p>
                @endif
            </div>

            <p>This offer is strictly provisional and is subject to the following conditions:</p>
            <ol class="list-decimal list-outside ml-6 space-y-2">
                <li>That the qualifications and documents presented by you during the application process are genuine and meet the minimum requirements of the University.</li>
                <li>That you complete all registration formalities and pay the prescribed tuition and sundry fees within the stipulated period.</li>
                <li>That you remain of good conduct and abide by all rules and regulations governing students of the National Open University of Nigeria Business School.</li>
            </ol>

            <p>If at any time it is discovered that you do not possess the qualifications you claimed or you are involved in any form of misconduct, this admission will be withdrawn and you may face prosecution.</p>

            <p>Please note that your official Matriculation Number is <strong>NBS/{{ $application->academic_session_id }}/{{ str_pad($application->id, 4, '0', STR_PAD_LEFT) }}</strong>. You are expected to use this number for all subsequent correspondence and transactions with the University.</p>

            <p>Congratulations once again on your admission, and we look forward to welcoming you to the NOUN Business School community.</p>
        </div>

        <!-- Signatory -->
        <div class="mt-16 flex justify-end">
            <div class="text-center">
                <div class="border-b-2 border-gray-800 w-48 mb-2"></div>
                <p class="font-bold text-gray-900">Prof. Samaila Mande</p>
                <p class="text-sm text-gray-600">Dean, NOUN Business School</p>
            </div>
        </div>

        <!-- Print Action -->
        <div class="mt-12 text-center no-print border-t pt-8">
            <button onclick="window.print()" class="bg-[#006600] hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-transform transform hover:scale-105 flex items-center gap-2 mx-auto">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg>
                Print Admission Letter
            </button>
            <p class="text-xs text-gray-400 mt-3">Use your browser's print dialog to save as PDF.</p>
        </div>
    </div>
</body>
</html>
