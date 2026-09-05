<x-mail::message>
# Welcome to NOUN Business School!

Dear **{{ $user->first_name }}**,

Thank you for creating an account on the NOUN Business School Portal. Your account has been registered successfully and your journey towards academic excellence begins now.

You can now log in to the portal to fill out your application, submit your documents, and track your admission status.

<x-mail::button :url="route('login')" color="primary">
Access Your Dashboard
</x-mail::button>

If you encounter any issues during the application process, please do not hesitate to contact our admissions support team.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
