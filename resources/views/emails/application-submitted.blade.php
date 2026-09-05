<x-mail::message>
# Application Submitted Successfully

Dear {{ $application->user->first_name }},

We have received your application for the **{{ $application->programme->name }}** programme at NOUN Business School.

Your application fee payment was successful, and your application is now under review by the admissions committee.

**Application Number:** {{ $application->application_number }}

You can track the status of your application by logging into your dashboard.

<x-mail::button :url="route('dashboard')">
View Application Status
</x-mail::button>

We will notify you via email as soon as a decision has been made.

Best regards,<br>
**NOUN Business School Admissions Team**
</x-mail::message>
