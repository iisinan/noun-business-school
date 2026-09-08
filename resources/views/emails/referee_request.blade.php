<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="color-scheme" content="light">
    <title>Reference Request – NOUN Business School</title>
    <style>
        body, body *:not(html):not(style):not(br):not(tr):not(code) {
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        body { background-color: #f4f4f5; color: #3f3f46; margin: 0; padding: 0; width: 100% !important; -webkit-text-size-adjust: none; }
        .wrapper { background-color: #f4f4f5; width: 100%; margin: 0; padding: 0; }
        .content-wrap { max-width: 600px; margin: 0 auto; padding: 32px 16px; }

        /* Header */
        .header { background-color: #004d00; border-radius: 12px 12px 0 0; text-align: center; padding: 32px 24px; }
        .header img { height: 56px; width: auto; margin-bottom: 12px; display: block; margin-left: auto; margin-right: auto; }
        .header h1 { color: #ffffff; font-size: 22px; font-weight: 800; margin: 0; letter-spacing: 1px; text-transform: uppercase; }
        .header p { color: #f2a900; font-size: 13px; margin: 6px 0 0 0; font-weight: 500; }

        /* Body */
        .body-card { background-color: #ffffff; padding: 36px 40px; }
        .body-card h2 { color: #004d00; font-size: 22px; font-weight: 700; margin: 0 0 20px 0; border-bottom: 2px solid #f2a900; padding-bottom: 12px; }
        .body-card p { color: #52525b; font-size: 15px; line-height: 1.7; margin: 0 0 16px 0; }
        .body-card strong { color: #18181b; }

        /* Info Panel */
        .info-panel { background-color: #f0fdf4; border-left: 4px solid #004d00; border-radius: 0 8px 8px 0; padding: 16px 20px; margin: 24px 0; }
        .info-panel p { margin: 0; font-size: 14px; color: #166534; line-height: 1.6; }
        .info-panel p + p { margin-top: 6px; }

        /* Button */
        .btn-wrap { text-align: center; margin: 32px 0; }
        .btn { display: inline-block; background-color: #004d00; color: #ffffff !important; font-size: 15px; font-weight: 700; text-decoration: none; padding: 14px 36px; border-radius: 8px; letter-spacing: 0.3px; }
        .btn:hover { background-color: #003800; }

        /* Footer */
        .footer { background-color: #004d00; border-radius: 0 0 12px 12px; padding: 20px 24px; text-align: center; }
        .footer p { color: #bbf7d0; font-size: 12px; margin: 0; line-height: 1.6; }
        .footer a { color: #f2a900; text-decoration: none; }

        /* Bottom note */
        .bottom-note { text-align: center; padding: 16px 0 4px; }
        .bottom-note p { color: #a1a1aa; font-size: 12px; margin: 0; line-height: 1.6; }

        @media only screen and (max-width: 600px) {
            .body-card { padding: 24px 20px !important; }
        }
    </style>
</head>
<body>
<table class="wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
<tr><td align="center">
<div class="content-wrap">

    <!-- Header -->
    <div class="header">
        <img src="{{ asset('nbs-logo.png') }}" alt="NOUN Business School Logo">
        <h1>NOUN Business School</h1>
        <p>Excellence in Enterprise</p>
    </div>

    <!-- Body -->
    <div class="body-card">
        <h2>Reference Request: {{ $referee->application->user->full_name }}</h2>

        <p>Dear <strong>{{ $referee->name }}</strong>,</p>

        <p>
            You have been listed as a referee for <strong>{{ $referee->application->user->full_name }}</strong>,
            who is applying for the <strong>{{ $referee->application->programme->name }}</strong> programme
            at NOUN Business School.
        </p>

        <p>
            As a referee, your evaluation plays a key role in the admissions process. Please click the secure
            button below to submit your professional or academic reference at your earliest convenience.
        </p>

        <!-- Info Panel -->
        <div class="info-panel">
            <p><strong>Applicant:</strong> {{ $referee->application->user->full_name }}</p>
            <p><strong>Programme:</strong> {{ $referee->application->programme->name }}</p>
            <p><strong>Your Role:</strong> Academic / Professional Referee</p>
        </div>

        <!-- CTA Button -->
        <div class="btn-wrap">
            <a href="{{ route('referee.form', $referee->token) }}" class="btn">Submit Your Reference</a>
        </div>

        <p>
            Your prompt response will help us evaluate the applicant's suitability for the programme.
            This link is unique to you and should not be shared with others.
        </p>

        <p>
            If you have any questions, please reach out to our admissions team at
            <a href="mailto:nounbusinessschool@noun.edu.ng" style="color: #004d00; font-weight: 600;">nounbusinessschool@noun.edu.ng</a>.
        </p>

        <p style="margin-top: 28px;">
            Best regards,<br>
            <strong>NOUN Business School Admissions Team</strong>
        </p>
    </div>

    <!-- Footer -->
    <div class="footer">
        <p>
            &copy; {{ date('Y') }} NOUN Business School. All rights reserved.<br>
            National Open University of Nigeria | <a href="https://www.pricenquote.com">pricenquote.com</a>
        </p>
    </div>

    <!-- Bottom note -->
    <div class="bottom-note">
        <p>
            You received this email because you were listed as a referee for an NBS applicant.<br>
            If this is a mistake, please ignore this email.
        </p>
    </div>

</div>
</td></tr>
</table>
</body>
</html>
