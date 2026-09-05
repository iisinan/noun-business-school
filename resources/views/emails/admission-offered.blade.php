<x-mail::message>
# Congratulations! You've been Admitted.

Dear **{{ $application->user->first_name }}**,

We are delighted to inform you that you have been offered provisional admission into the **{{ $application->programme->name }}** programme at NOUN Business School!

Your academic record and professional background deeply impressed our Admissions Committee, and we are confident that you will be a valuable addition to our esteemed academic community.

<x-mail::panel>
**Your Admission Details:**
- **Application Number:** {{ $application->application_number }}
- **Programme of Study:** {{ $application->programme->name }}
</x-mail::panel>

### Next Steps
To secure your placement, please log in to your portal dashboard to download your official **Admission Letter** and proceed to pay your **Acceptance Fee**.

<x-mail::button :url="route('dashboard')" color="success">
Accept Offer & View Dashboard
</x-mail::button>

Congratulations once again! We look forward to welcoming you to the NOUN Business School family.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
