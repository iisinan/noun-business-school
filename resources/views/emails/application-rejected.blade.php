<x-mail::message>
# Update on Your Application

Dear **{{ $application->user->first_name }}**,

Thank you for applying to the **{{ $application->programme->name }}** programme at NOUN Business School.

We have carefully reviewed your application, academic background, and credentials. Unfortunately, we regret to inform you that we are unable to offer you admission into the programme at this time.

Please note that our admissions process is highly competitive, and decisions are based on a comprehensive review of all required qualifications against the limited spaces available in the programme.

<x-mail::panel>
**Application Reference:** {{ $application->application_number }}
</x-mail::panel>

We deeply appreciate your interest in NOUN Business School and encourage you to re-apply for future academic sessions once you have gained further experience or qualifications.

We wish you the absolute best in your future academic and professional endeavors.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
