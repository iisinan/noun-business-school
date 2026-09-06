file_path = '/Users/sinan/Herd/Business School/resources/views/applicant/application-docket.blade.php'
with open(file_path, 'r') as f:
    content = f.read()

search = """        <div class="flex justify-between items-end mb-6">
            <div>
                <h3 class="font-bold text-xl">{{ $application->programme->name }}</h3>
                @if($application->specialisation)
                <p class="text-gray-600 font-semibold">Specialisation: {{ $application->specialisation->name }}</p>
                @endif
            </div>
            <div class="text-right">
                <p class="text-xs text-gray-500 uppercase">Application No</p>
                <p class="font-bold text-lg font-mono">{{ $application->application_number }}</p>
                <p class="text-xs mt-1">Submitted: {{ $application->created_at->format('M j, Y') }}</p>
            </div>
        </div>"""

replace = """        <div class="flex justify-between items-start mb-6">
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
        </div>"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched Docket")
else:
    print("Search block not found")
