<!DOCTYPE html>
<html>
<head>
    <title>Student Results</title>
    <style>
        body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; color: #333; }
        .header { text-align: center; margin-bottom: 20px; border-bottom: 2px solid #14532d; padding-bottom: 10px; }
        .header h1 { font-size: 24px; color: #14532d; margin: 0 0 5px 0; }
        .header h2 { font-size: 16px; margin: 0; color: #666; }
        .student-info { margin-bottom: 20px; width: 100%; border-collapse: collapse; }
        .student-info td { padding: 5px; border-bottom: 1px solid #eee; }
        .student-info strong { color: #14532d; }
        .session-block { margin-bottom: 20px; page-break-inside: avoid; }
        .session-title { font-size: 14px; font-weight: bold; background-color: #f0fdf4; padding: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px; }
        table.results-table { width: 100%; border-collapse: collapse; margin-bottom: 10px; }
        table.results-table th, table.results-table td { border: 1px solid #ddd; padding: 6px; text-align: left; }
        table.results-table th { background-color: #f8fafc; font-size: 11px; text-transform: uppercase; color: #64748b; }
        .text-center { text-align: center; }
        .font-bold { font-weight: bold; }
        .summary-block { margin-top: 30px; background-color: #14532d; color: #fff; padding: 15px; border-radius: 5px; page-break-inside: avoid; }
        .summary-block table { width: 100%; }
        .summary-block td { font-size: 14px; }
        .grade-badge { display: inline-block; padding: 2px 5px; border-radius: 3px; font-weight: bold; }
    </style>
</head>
<body>

    <div class="header">
        <h1>NOUN Business School</h1>
        <h2>Statement of Results</h2>
    </div>

    <table class="student-info">
        <tr>
            <td width="20%"><strong>Name:</strong></td>
            <td width="30%">{{ $user->name }}</td>
            <td width="20%"><strong>Matric Number:</strong></td>
            <td width="30%">{{ $user->matric_number ?? 'N/A' }}</td>
        </tr>
        <tr>
            <td><strong>Programme:</strong></td>
            <td>{{ $application && $application->programme ? $application->programme->name : 'N/A' }}</td>
            <td><strong>Specialisation:</strong></td>
            <td>{{ $application && $application->specialisation ? $application->specialisation->name : 'N/A' }}</td>
        </tr>
    </table>

    @foreach($resultsBySession as $sessionData)
        <div class="session-block">
            <div class="session-title">
                {{ $sessionData['session']->name }} 
                <span style="float: right;">GPA: {{ number_format($sessionData['gpa'], 2) }} | Credits: {{ $sessionData['session_credits'] }}</span>
            </div>
            
            <table class="results-table">
                <thead>
                    <tr>
                        <th width="15%">Code</th>
                        <th width="45%">Title</th>
                        <th width="10%" class="text-center">Units</th>
                        <th width="15%" class="text-center">Score</th>
                        <th width="15%" class="text-center">Grade</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach($sessionData['registrations'] as $reg)
                        <tr>
                            <td class="font-bold">{{ $reg->course->code }}</td>
                            <td>{{ $reg->course->title }}</td>
                            <td class="text-center">{{ $reg->course->units }}</td>
                            <td class="text-center">{{ $reg->score !== null ? $reg->score : '-' }}</td>
                            <td class="text-center font-bold">
                                {{ $reg->grade ? $reg->grade : 'Pending' }}
                            </td>
                        </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    @endforeach

    <div class="summary-block">
        <table>
            <tr>
                <td><strong>Cumulative Grade Point Average (CGPA):</strong> <span style="font-size: 20px;">{{ number_format($cgpa, 2) }}</span></td>
                <td style="text-align: right;"><strong>Total Credits Earned:</strong> <span style="font-size: 20px;">{{ $cumulativeCredits }}</span></td>
            </tr>
        </table>
    </div>

</body>
</html>
