<x-mail::message>
# Verify Your Email Address

Dear **{{ $firstName }}**,

Thank you for creating an account with NOUN Business School! You're almost there. To complete your account setup and begin your application, please verify your email address by clicking the button below.

<x-mail::button :url="$url" color="primary">
Verify Email Address
</x-mail::button>

<x-mail::panel>
### Security Note
This verification link will expire in **{{ $expireMinutes }} minutes**. If you need a new link, you can request one by logging into the portal and clicking **"Resend Verification Email"**.

*If you did not create an account at NOUN Business School, you can safely ignore this email — no further action is required.*
</x-mail::panel>

### What happens after you verify?
1. You'll be taken directly to the **application form**.
2. Fill in your personal details, academic background, and upload documents.
3. Submit your application and pay the processing fee.

If you have any questions or encounter technical issues, please contact our support team at [admissions@noun.edu.ng](mailto:admissions@noun.edu.ng).

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
