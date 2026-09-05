<x-mail::message>
# Congratulations! You've been Admitted.

Dear **{{ $application->user->first_name }}**,

We are delighted to inform you that you have been offered provisional admission into the **{{ $application->programme->name }}** programme at NOUN Business School!

Your academic record and professional background deeply impressed our Admissions Committee, and we are confident that you will be a valuable addition to our esteemed academic community.

<x-mail::panel>
### Your Admission Details
**Application Number:** {{ $application->application_number }}  
**Programme of Study:** {{ $application->programme->name }}  
**Session:** {{ $application->academicSession->name ?? 'Current Session' }}
</x-mail::panel>

### Your Next Steps
To secure your placement in the programme, please complete the following steps within the next **14 days**:

1. **Log in to your dashboard** to view and download your official Admission Letter.
2. **Pay your Acceptance Fee** via the secure payment gateway on your dashboard.
3. **Complete your course registration** for the current semester.

<x-mail::button :url="route('dashboard')" color="success">
Accept Offer & View Dashboard
</x-mail::button>

*Note: Failure to pay your acceptance fee before the deadline may result in the forfeiture of your admission.*

Congratulations once again! We look forward to welcoming you to the NOUN Business School family.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
