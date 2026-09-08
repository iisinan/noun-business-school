<x-mail::message>
# Reference Request: {{ $referee->application->user->full_name }}

Dear {{ $referee->name }},

You have been listed as a referee for **{{ $referee->application->user->full_name }}**, who is applying for the **{{ $referee->application->programme->name }}** at NOUN Business School.

Please click the secure button below to provide your professional or academic reference.

<x-mail::button :url="route('referee.form', $referee->token)">
Submit Reference
</x-mail::button>

Your prompt response will help us evaluate the applicant's suitability for the programme.

Thank you,<br>
**NOUN Business School Admissions Team**
</x-mail::message>
