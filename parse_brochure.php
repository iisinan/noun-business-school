<?php

$content = file_get_contents('brochure.txt');
$lines = explode("\n", $content);

$data = [
    'programmes' => [],
];

$currentProgramme = null;
$currentSpec = null;
$currentSection = null;

$mbaCore = [
    ['code' => 'MBA 701', 'title' => 'Managerial Economics', 'units' => 3],
    ['code' => 'MBA 702', 'title' => 'Financial Accounting & Reporting', 'units' => 3],
    ['code' => 'MBA 703', 'title' => 'Organisational Behaviour & Leadership', 'units' => 3],
    ['code' => 'MBA 704', 'title' => 'Marketing Management', 'units' => 3],
    ['code' => 'MBA 705', 'title' => 'Quantitative Methods & Business Statistics', 'units' => 3],
    ['code' => 'MBA 706', 'title' => 'Strategic Management', 'units' => 3],
    ['code' => 'MBA 707', 'title' => 'Business Research Methods', 'units' => 3],
    ['code' => 'MBA 708', 'title' => 'Corporate Finance', 'units' => 3],
];

$dbaCore = [
    ['code' => 'DBA 811', 'title' => 'Advanced Philosophy of Management Science & Epistemology of Business Research', 'units' => 3],
    ['code' => 'DBA 812', 'title' => 'Advanced Quantitative Research Methods', 'units' => 3],
    ['code' => 'DBA 813', 'title' => 'Advanced Qualitative & Mixed-Methods Research', 'units' => 3],
    ['code' => 'DBA 814', 'title' => 'Strategic Theory & Organisational Design', 'units' => 3],
    ['code' => 'DBA 815', 'title' => 'Global Business Environment & Comparative Management', 'units' => 3],
    ['code' => 'DBA 816', 'title' => 'Applied Econometrics for Managers', 'units' => 3],
    ['code' => 'DBA 817', 'title' => 'Ethics, Governance & Corporate Responsibility', 'units' => 3],
    ['code' => 'DBA 818', 'title' => 'Doctoral Seminar & Research Proposal Development', 'units' => 3],
];

foreach ($lines as $line) {
    $line = trim($line);
    if (empty($line)) continue;

    // Detect Programme Level
    if (preg_match('/^1\.0 Graduate Diploma in Business Administration \(GDBA\)/', $line)) {
        $currentProgramme = [
            'name' => 'Graduate Diploma in Business Administration',
            'type' => 'GDBA',
            'description' => 'Foundation pathway into the MBA/MPA programme.',
            'specialisations' => [],
            'foundational_core' => [],
            'requirements' => [
                ['desc' => 'First Degree (any discipline) from a recognised university with a minimum of Third Class, or HND with a minimum of Lower Credit.', 'is_doc' => false],
                ['desc' => 'Five (5) credits in WAEC/NECO/GCE O\'Level (or equivalent), including English Language and Mathematics, at not more than two sittings.', 'is_doc' => false],
                ['desc' => 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc' => true],
                ['desc' => 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc' => true],
                ['desc' => 'Current Curriculum Vitae / Resume.', 'is_doc' => true],
                ['desc' => 'Two (2) professional or academic reference letters.', 'is_doc' => true],
                ['desc' => 'Statement of Purpose (500–1,000 words).', 'is_doc' => true],
            ]
        ];
        $data['programmes']['GDBA'] = &$currentProgramme;
        continue;
    }

    if (preg_match('/^2\.0 Master of Business Administration \(MBA\/MPA\)/', $line)) {
        $currentProgramme = [
            'name' => 'Master of Business Administration',
            'type' => 'MBA',
            'description' => 'Two-year graduate management qualification.',
            'specialisations' => [],
            'foundational_core' => $mbaCore,
            'requirements' => [
                ['desc' => 'Bachelor\'s degree (minimum Second Class Lower) from a recognised university in any discipline, or HND (minimum Upper Credit).', 'is_doc' => false],
                ['desc' => 'Five (5) credits in WAEC/NECO/GCE O\'Level (or equivalent), including English Language and Mathematics, at not more than two sittings.', 'is_doc' => false],
                ['desc' => 'A minimum of two (2) years post-qualification work experience.', 'is_doc' => false],
                ['desc' => 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc' => true],
                ['desc' => 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc' => true],
                ['desc' => 'Current Curriculum Vitae / Resume.', 'is_doc' => true],
                ['desc' => 'Two (2) professional or academic reference letters.', 'is_doc' => true],
                ['desc' => 'Statement of Purpose (500–1,000 words).', 'is_doc' => true],
            ]
        ];
        $data['programmes']['MBA'] = &$currentProgramme;
        continue;
    }

    if (preg_match('/^3\. Doctor of Business Administration \(DBA\/DPA\)/', $line)) {
        $currentProgramme = [
            'name' => 'Doctor of Business Administration',
            'type' => 'DBA',
            'description' => 'Practitioner-research doctoral degree spanning three years.',
            'specialisations' => [],
            'foundational_core' => $dbaCore,
            'requirements' => [
                ['desc' => 'Master\'s degree (MBA or relevant Master\'s, minimum CGPA of 3.5 on a 5-point scale or equivalent) from a recognised university.', 'is_doc' => false],
                ['desc' => 'Minimum of five (5) years senior-level management or professional experience.', 'is_doc' => false],
                ['desc' => 'Research concept note aligned to one of the specialisation tracks.', 'is_doc' => true],
                ['desc' => 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc' => true],
                ['desc' => 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc' => true],
                ['desc' => 'Current Curriculum Vitae / Resume.', 'is_doc' => true],
                ['desc' => 'Two (2) professional or academic reference letters.', 'is_doc' => true],
            ]
        ];
        $data['programmes']['DBA'] = &$currentProgramme;
        continue;
    }

    if (preg_match('/^4\. Executive Certificate Programmes \(Non-Degree\)/', $line)) {
        $currentProgramme = [
            'name' => 'Executive Certificate Programmes',
            'type' => 'Certificate',
            'description' => 'Short, modular, non-degree qualifications.',
            'specialisations' => [],
            'foundational_core' => [],
            'requirements' => [
                ['desc' => 'OND/HND/First Degree or relevant professional/work experience.', 'is_doc' => false],
                ['desc' => 'Current Curriculum Vitae / Resume.', 'is_doc' => true],
                ['desc' => 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc' => true],
            ]
        ];
        $data['programmes']['Certificate'] = &$currentProgramme;
        continue;
    }

    // Detect Specialisations for MBA
    if (preg_match('/^2\.(\d+)\s+(MBA|MPA) in (.*)/', $line, $matches)) {
        $name = trim($matches[3]);
        $currentSpec = [
            'name' => $name,
            'type' => $matches[2],
            'description' => '',
            'courses' => [],
            'electives' => [],
        ];
        $data['programmes']['MBA']['specialisations'][] = &$currentSpec;
        $currentSection = 'spec_desc';
        continue;
    }

    // Detect Specialisations for DBA
    if (preg_match('/^3\.(\d+)\s+(DBA|DPA) in (.*)/', $line, $matches)) {
        $name = trim($matches[3]);
        $currentSpec = [
            'name' => $name,
            'type' => $matches[2],
            'description' => '',
            'courses' => [],
            'electives' => [],
        ];
        $data['programmes']['DBA']['specialisations'][] = &$currentSpec;
        $currentSection = 'spec_desc';
        continue;
    }

    // Section tracking
    if ($currentSpec) {
        if (preg_match('/^Programme Structure/', $line)) {
            $currentSection = 'core_courses';
            continue;
        }
        if (preg_match('/^Electives/', $line)) {
            $currentSection = 'elective_courses';
            continue;
        }
        if (preg_match('/^Capstone Project/', $line) || preg_match('/^Applied Doctoral Research/', $line)) {
            $currentSection = 'capstone';
            continue;
        }

        // Parse courses
        if (preg_match('/^([A-Z]{3}-[A-Z]{3}\s*\d{3})\s+(.*?)\s+(\d+)$/', $line, $matches)) {
            $course = [
                'code' => trim($matches[1]),
                'title' => trim($matches[2]),
                'units' => (int)$matches[3]
            ];
            if ($currentSection === 'core_courses') {
                $currentSpec['courses'][] = $course;
            } elseif ($currentSection === 'elective_courses') {
                $currentSpec['electives'][] = $course;
            }
        }
    }
}

// Manually add Executive Certificate Specialisations from page 136
if (isset($data['programmes']['Certificate'])) {
    $certs = ['Data Analytics', 'FinTech', 'ESG Reporting', 'Project Management', 'Public Procurement', 'Entrepreneurship', 'Healthcare Administration', 'Digital Marketing'];
    foreach ($certs as $cert) {
        $data['programmes']['Certificate']['specialisations'][] = [
            'name' => $cert,
            'type' => 'Certificate',
            'description' => '',
            'courses' => [],
            'electives' => []
        ];
    }
}

// Hardcode GDBA Courses (Page 10/11)
if (isset($data['programmes']['GDBA'])) {
    $data['programmes']['GDBA']['foundational_core'] = [
        ['code' => 'GDBA 501', 'title' => 'Principles of Management', 'units' => 3],
        ['code' => 'GDBA 502', 'title' => 'Principles of Economics for Managers', 'units' => 3],
        ['code' => 'GDBA 503', 'title' => 'Financial Accounting I', 'units' => 3],
        ['code' => 'GDBA 504', 'title' => 'Business Communication & Report Writing', 'units' => 3],
        ['code' => 'GDBA 505', 'title' => 'Principles of Marketing', 'units' => 3],
        ['code' => 'GDBA 506', 'title' => 'Business Mathematics & Statistics', 'units' => 3],
        ['code' => 'GDBA 507', 'title' => 'Business Law', 'units' => 3],
        ['code' => 'GDBA 521', 'title' => 'Organisational Behaviour', 'units' => 3],
        ['code' => 'GDBA 522', 'title' => 'Financial Accounting II', 'units' => 3],
        ['code' => 'GDBA 523', 'title' => 'Human Resource Management', 'units' => 3],
        ['code' => 'GDBA 524', 'title' => 'Introduction to Strategic Management', 'units' => 3],
        ['code' => 'GDBA 525', 'title' => 'Information Systems for Business', 'units' => 3],
        ['code' => 'GDBA 526', 'title' => 'Entrepreneurship Development', 'units' => 3],
        ['code' => 'GDBA 600', 'title' => 'Bridging Project (Directed Study)', 'units' => 2],
    ];
}

file_put_contents('database/seeders/brochure_data.json', json_encode($data, JSON_PRETTY_PRINT));
echo "Parsed " . count($data['programmes']) . " programmes.\n";
if(isset($data['programmes']['MBA'])) echo "MBA Specs: " . count($data['programmes']['MBA']['specialisations']) . "\n";
if(isset($data['programmes']['DBA'])) echo "DBA Specs: " . count($data['programmes']['DBA']['specialisations']) . "\n";
