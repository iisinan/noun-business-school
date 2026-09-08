<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;
use App\Models\Referee;

class SendRefereeRequestMail extends Mailable
{
    use Queueable, SerializesModels;

    public $referee;

    public function __construct(Referee $referee)
    {
        $this->referee = $referee;
    }

    public function envelope(): Envelope
    {
        return new Envelope(
            subject: 'Reference Request: ' . $this->referee->application->user->full_name . ' - NOUN Business School',
        );
    }

    public function content(): Content
    {
        return new Content(
            view: 'emails.referee_request',
            with: ['referee' => $this->referee],
        );
    }

    public function attachments(): array
    {
        return [];
    }
}
