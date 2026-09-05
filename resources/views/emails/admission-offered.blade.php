<x-mail::message>
# Congratulations! Offer of Admission

Dear {{ $application->user->first_name }},

We are pleased to inform you that you have been offered admission into the **{{ $application->programme->name }}** programme at NOUN Business School.

Your academic record and professional background impressed the admissions committee, and we believe you will be a valuable addition to our academic community.

**Application Number:** {{ $application->application_number }}

To secure your placement, please log in to your dashboard to view your official Admission Letter and proceed to pay your Acceptance Fee.

<x-mail::button :url="route('dashboard')">
Log in to your Dashboard
</x-mail::button>

Congratulations once again, and we look forward to welcoming you to NOUN Business School.

Best regards,<br>
**NOUN Business School Admissions Team**
</x-mail::message>
