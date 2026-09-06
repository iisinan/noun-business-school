<x-mail::layout>
{{-- Header --}}
<x-slot:header>
<x-mail::header :url="config('app.url')">
{{ config('app.name') }}
</x-mail::header>
</x-slot:header>

{{-- Body --}}
{!! $slot !!}

{{-- Subcopy --}}
@isset($subcopy)
<x-slot:subcopy>
<x-mail::subcopy>
{!! $subcopy !!}
</x-mail::subcopy>
</x-slot:subcopy>
@endisset

{{-- Footer --}}
<x-slot:footer>
<x-mail::footer>
<div style="text-align: center; color: #a1a1aa; font-size: 12px; line-height: 1.5;">
    <strong>NOUN Business School</strong><br>
    Plot 91 Cadastral Zone, Nnamdi Azikiwe Expressway, Jabi, Abuja, Nigeria.<br>
    <a href="mailto:admissions@noun.edu.ng" style="color: #006600; text-decoration: underline;">admissions@noun.edu.ng</a> | 
    <a href="{{ config('app.url') }}" style="color: #006600; text-decoration: underline;">{{ config('app.url') }}</a><br><br>
    © {{ date('Y') }} {{ config('app.name') }}. All rights reserved.
</div>
</x-mail::footer>
</x-slot:footer>
</x-mail::layout>
