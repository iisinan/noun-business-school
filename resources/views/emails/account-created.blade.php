<x-mail::message>
# Welcome to NOUN Business School

Dear {{ $user->first_name }},

Thank you for registering an account on the NOUN Business School portal. Your account has been created successfully.

You can now log in to the portal to begin your application process.

<x-mail::button :url="route('login')">
Log in to your Dashboard
</x-mail::button>

If you have any questions, please contact our support team.

Best regards,<br>
**NOUN Business School Admissions Team**
</x-mail::message>
