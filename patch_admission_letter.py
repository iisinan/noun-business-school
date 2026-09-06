file_path = '/Users/sinan/Herd/Business School/resources/views/applicant/admission-letter.blade.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        <!-- Addressee -->
        <div class="mb-8">
            <p class="font-bold text-lg">{{ $application->user->first_name }} {{ $application->user->last_name }}</p>
            <p>{{ $application->personal_info['address'] ?? 'Applicant Address' }}</p>
            <p>{{ $application->personal_info['state_of_origin'] ?? '' }}, {{ $application->personal_info['nationality'] ?? '' }}</p>
        </div>"""

replace = """        <!-- Addressee & Passport -->
        <div class="mb-8 flex justify-between items-start">
            <div>
                <p class="font-bold text-lg">{{ $application->user->first_name }} {{ $application->user->last_name }}</p>
                <p>{{ $application->personal_info['address'] ?? 'Applicant Address' }}</p>
                <p>{{ $application->personal_info['state_of_origin'] ?? '' }}, {{ $application->personal_info['nationality'] ?? '' }}</p>
            </div>
            @if(isset($application->personal_info['passport_photograph_path']))
            <div class="h-28 w-28 border-2 border-[#006600] p-1 bg-white shrink-0">
                <img src="{{ \Illuminate\Support\Facades\Storage::disk('s3')->url($application->personal_info['passport_photograph_path']) }}" class="h-full w-full object-cover" alt="Passport">
            </div>
            @endif
        </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Admission Letter")
else:
    print("Search block not found")
