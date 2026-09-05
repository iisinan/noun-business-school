<x-mail::message>
# Application Successfully Submitted

Dear **{{ $application->user->first_name }}**,

This email is to confirm that we have successfully received your application for the **{{ $application->programme->name }}** programme at NOUN Business School.

Your application fee payment was successful, and your application has now been forwarded to the Admissions Committee for review.

<x-mail::panel>
**Application Details:**
- **Programme:** {{ $application->programme->name }}
- **Application Number:** {{ $application->application_number }}
- **Status:** Under Review
</x-mail::panel>

You can track the live status of your application at any time by logging into your dashboard.

<x-mail::button :url="route('dashboard')" color="primary">
Track Application Status
</x-mail::button>

We will notify you via email as soon as a final decision has been made. Thank you for choosing NOUN Business School.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
