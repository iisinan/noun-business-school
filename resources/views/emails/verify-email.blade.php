<x-mail::message>
{{-- Greeting --}}
<div style="text-align:center; padding: 8px 0 24px;">
    <div style="display:inline-block; background:#f0fdf4; border-radius:16px; padding:14px 16px; margin-bottom:16px;">
        <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlPSIjMDA2NjAwIiBzdHJva2Utd2lkdGg9IjEuOCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMyA4bDcuODkgNS4yNmEyIDIgMCAwMDIuMjIgMEwyMSA4TTUgMTloMTRhMiAyIDAgMDAyLTJWN2EyIDIgMCAwMC0yLTJINWEyIDIgMCAwMC0yIDJ2MTBhMiAyIDAgMDAyIDJ6Ii8+PC9zdmc+" width="32" height="32" alt="Email" style="display:block;">
    </div>
    <h1 style="margin:0; font-size:22px; font-weight:800; color:#111827; letter-spacing:-0.3px;">Verify your email address</h1>
    <p style="margin:8px 0 0; font-size:15px; color:#6b7280; line-height:1.5;">You're almost there! One quick step to activate your<br><strong style="color:#111827;">NOUN Business School</strong> account.</p>
</div>

---

**Hello {{ $notifiable->first_name }},**

Thank you for registering with NOUN Business School. To complete your account setup and begin your application, please verify your email address by clicking the button below.

<x-mail::button :url="$url" color="primary">
✉️ &nbsp; Verify Email Address
</x-mail::button>

---

{{-- Security note --}}
<x-mail::panel>
🔒 &nbsp;**Security note:** This verification link will expire in **{{ $expireMinutes }} minutes**. If you need a new link, visit the portal and click **"Resend Verification Email"**.

If you did not create an account at NOUN Business School, you can safely ignore this email — no action is required.
</x-mail::panel>

---

{{-- What's next --}}
**What happens after you verify?**

1. You'll be taken directly to the **application form**
2. Fill in your personal details, academic background, and upload documents
3. Submit your application and pay the processing fee

If you have any questions, please contact us at [admissions@noun.edu.ng](mailto:admissions@noun.edu.ng).

**The NOUN Business School Admissions Team**

</x-mail::message>
