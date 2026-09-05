<x-mail::message>
# Application Successfully Submitted

Dear **{{ $application->user->first_name }}**,

This email is to officially confirm that we have successfully received your application for the **{{ $application->programme->name }}** programme at NOUN Business School.

Your application fee payment was successful, and your file has now been forwarded to the Admissions Committee for academic review.

<x-mail::panel>
### Your Application Details
**Programme:** {{ $application->programme->name }}  
**Application Number:** {{ $application->application_number }}  
**Current Status:** Under Review
</x-mail::panel>

### What Happens Next?
Our admissions committee reviews applications on a rolling basis. You can expect a status update on your application within **3 to 5 business days**.

You can track the live status of your application at any time by logging into your student dashboard.

<x-mail::button :url="route('dashboard')" color="primary">
Track Application Status
</x-mail::button>

We will notify you via email as soon as a final decision has been made. Thank you for choosing NOUN Business School.

Best regards,<br>
**Admissions Office**<br>
NOUN Business School
</x-mail::message>
