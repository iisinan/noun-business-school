<x-mail::message>
# Welcome to NOUN Business School!

Dear **{{ $user->first_name }}**,

Thank you for creating an account on the NOUN Business School Portal. Your account has been registered successfully, and your journey towards academic excellence begins now.

### Getting Started with Your Application
You can now log in to the portal to fill out your application. Before you begin, please ensure you have the following documents ready in PDF or Image format:
- A recent Passport Photograph (Max 2MB)
- Your O-Level Results (WAEC/NECO/NABTEB)
- Your Degree Certificate or Statement of Result
- Your NYSC Certificate or Exemption Letter (if applicable)

<x-mail::button :url="route('login')" color="primary">
Start Your Application
</x-mail::button>

If you encounter any technical issues or have questions regarding the requirements, please do not hesitate to contact our admissions support team.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
