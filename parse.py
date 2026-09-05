import json
import re

with open('brochure.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

data = {
    'programmes': {
        'GDBA': {
            'name': 'Graduate Diploma in Business Administration',
            'type': 'GDBA',
            'description': 'Foundation pathway into the MBA/MPA programme.',
            'specialisations': {},
            'foundational_core': [],
            'requirements': [
                {'desc': 'First Degree (any discipline) from a recognised university with a minimum of Third Class, or HND with a minimum of Lower Credit.', 'is_doc': False},
                {'desc': 'Five (5) credits in WAEC/NECO/GCE O\'Level (or equivalent), including English Language and Mathematics, at not more than two sittings.', 'is_doc': False},
                {'desc': 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc': True},
                {'desc': 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc': True},
                {'desc': 'Current Curriculum Vitae / Resume.', 'is_doc': True},
                {'desc': 'Two (2) professional or academic reference letters.', 'is_doc': True},
                {'desc': 'Statement of Purpose (500–1,000 words).', 'is_doc': True},
            ]
        },
        'MBA': {
            'name': 'Master of Business Administration',
            'type': 'MBA',
            'description': 'Two-year graduate management qualification.',
            'specialisations': {},
            'foundational_core': [
                {'code': 'MBA 701', 'title': 'Managerial Economics', 'units': 3},
                {'code': 'MBA 702', 'title': 'Financial Accounting & Reporting', 'units': 3},
                {'code': 'MBA 703', 'title': 'Organisational Behaviour & Leadership', 'units': 3},
                {'code': 'MBA 704', 'title': 'Marketing Management', 'units': 3},
                {'code': 'MBA 705', 'title': 'Quantitative Methods & Business Statistics', 'units': 3},
                {'code': 'MBA 706', 'title': 'Strategic Management', 'units': 3},
                {'code': 'MBA 707', 'title': 'Business Research Methods', 'units': 3},
                {'code': 'MBA 708', 'title': 'Corporate Finance', 'units': 3},
            ],
            'requirements': [
                {'desc': 'Bachelor\'s degree (minimum Second Class Lower) from a recognised university in any discipline, or HND (minimum Upper Credit).', 'is_doc': False},
                {'desc': 'Five (5) credits in WAEC/NECO/GCE O\'Level (or equivalent), including English Language and Mathematics, at not more than two sittings.', 'is_doc': False},
                {'desc': 'A minimum of two (2) years post-qualification work experience.', 'is_doc': False},
                {'desc': 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc': True},
                {'desc': 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc': True},
                {'desc': 'Current Curriculum Vitae / Resume.', 'is_doc': True},
                {'desc': 'Two (2) professional or academic reference letters.', 'is_doc': True},
                {'desc': 'Statement of Purpose (500–1,000 words).', 'is_doc': True},
            ]
        },
        'DBA': {
            'name': 'Doctor of Business Administration',
            'type': 'DBA',
            'description': 'Practitioner-research doctoral degree spanning three years.',
            'specialisations': {},
            'foundational_core': [
                {'code': 'DBA 811', 'title': 'Advanced Philosophy of Management Science & Epistemology of Business Research', 'units': 3},
                {'code': 'DBA 812', 'title': 'Advanced Quantitative Research Methods', 'units': 3},
                {'code': 'DBA 813', 'title': 'Advanced Qualitative & Mixed-Methods Research', 'units': 3},
                {'code': 'DBA 814', 'title': 'Strategic Theory & Organisational Design', 'units': 3},
                {'code': 'DBA 815', 'title': 'Global Business Environment & Comparative Management', 'units': 3},
                {'code': 'DBA 816', 'title': 'Applied Econometrics for Managers', 'units': 3},
                {'code': 'DBA 817', 'title': 'Ethics, Governance & Corporate Responsibility', 'units': 3},
                {'code': 'DBA 818', 'title': 'Doctoral Seminar & Research Proposal Development', 'units': 3},
            ],
            'requirements': [
                {'desc': 'Master\'s degree (MBA or relevant Master\'s, minimum CGPA of 3.5 on a 5-point scale or equivalent) from a recognised university.', 'is_doc': False},
                {'desc': 'Minimum of five (5) years senior-level management or professional experience.', 'is_doc': False},
                {'desc': 'Research concept note aligned to one of the specialisation tracks.', 'is_doc': True},
                {'desc': 'Certified copies of academic transcripts and certificates from previously attended institutions.', 'is_doc': True},
                {'desc': 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc': True},
                {'desc': 'Current Curriculum Vitae / Resume.', 'is_doc': True},
                {'desc': 'Two (2) professional or academic reference letters.', 'is_doc': True},
            ]
        },
        'Certificate': {
            'name': 'Executive Certificate Programmes',
            'type': 'Certificate',
            'description': 'Short, modular, non-degree qualifications.',
            'specialisations': {},
            'foundational_core': [],
            'requirements': [
                {'desc': 'OND/HND/First Degree or relevant professional/work experience.', 'is_doc': False},
                {'desc': 'Current Curriculum Vitae / Resume.', 'is_doc': True},
                {'desc': 'Valid means of identification (National ID, International Passport, or Driver\'s Licence).', 'is_doc': True},
            ]
        }
    }
}

current_spec = None
current_section = None

in_body = False

for line in lines:
    if 'Foundational Core — Semester 1' in line:
        in_body = True
        
    if not in_body:
        continue

    # MBA Specialisation header
    mba_match = re.match(r'^2\.(\d+)\s+(MBA|MPA) in (.*)', line)
    if mba_match:
        name = mba_match.group(3).strip()
        # Clean up name if it has TOC dots
        name = re.sub(r'[\.…]+\s*\d*$', '', name).strip()
        
        if name not in data['programmes']['MBA']['specialisations']:
            data['programmes']['MBA']['specialisations'][name] = {'name': name, 'type': mba_match.group(2).strip(), 'description': '', 'courses': [], 'electives': []}
        current_spec = data['programmes']['MBA']['specialisations'][name]
        current_section = 'spec_desc'
        continue

    # DBA Specialisation header
    dba_match = re.match(r'^3\.(\d+)\s+(DBA|DPA) in (.*)', line)
    if dba_match:
        name = dba_match.group(3).strip()
        name = re.sub(r'[\.…]+\s*\d*$', '', name).strip()
        
        if name not in data['programmes']['DBA']['specialisations']:
            data['programmes']['DBA']['specialisations'][name] = {'name': name, 'type': dba_match.group(2).strip(), 'description': '', 'courses': [], 'electives': []}
        current_spec = data['programmes']['DBA']['specialisations'][name]
        current_section = 'spec_desc'
        continue

    if current_spec:
        if line.startswith('Programme Structure'):
            current_section = 'core_courses'
            continue
        if line.startswith('Electives'):
            current_section = 'elective_courses'
            continue
        if line.startswith('Capstone Project') or line.startswith('Applied Doctoral Research'):
            current_section = 'capstone'
            continue

        course_match = re.match(r'^([A-Z]{3}-[A-Z]{3}\s*\d{3})\s+(.*?)\s+(\d+)$', line)
        if course_match:
            course = {
                'code': course_match.group(1).strip(),
                'title': course_match.group(2).strip(),
                'units': int(course_match.group(3).strip())
            }
            if current_section == 'core_courses':
                if course not in current_spec['courses']:
                    current_spec['courses'].append(course)
            elif current_section == 'elective_courses':
                if course not in current_spec['electives']:
                    current_spec['electives'].append(course)

certs = ['Data Analytics', 'FinTech', 'ESG Reporting', 'Project Management', 'Public Procurement', 'Entrepreneurship', 'Healthcare Administration', 'Digital Marketing']
for cert in certs:
    data['programmes']['Certificate']['specialisations'][cert] = {
        'name': cert,
        'type': 'Certificate',
        'description': '',
        'courses': [],
        'electives': []
    }

# Convert dict to list
for p_key in data['programmes']:
    data['programmes'][p_key]['specialisations'] = list(data['programmes'][p_key]['specialisations'].values())

# Hardcode GDBA Courses
data['programmes']['GDBA']['foundational_core'] = [
    {'code': 'GDBA 501', 'title': 'Principles of Management', 'units': 3},
    {'code': 'GDBA 502', 'title': 'Principles of Economics for Managers', 'units': 3},
    {'code': 'GDBA 503', 'title': 'Financial Accounting I', 'units': 3},
    {'code': 'GDBA 504', 'title': 'Business Communication & Report Writing', 'units': 3},
    {'code': 'GDBA 505', 'title': 'Principles of Marketing', 'units': 3},
    {'code': 'GDBA 506', 'title': 'Business Mathematics & Statistics', 'units': 3},
    {'code': 'GDBA 507', 'title': 'Business Law', 'units': 3},
    {'code': 'GDBA 521', 'title': 'Organisational Behaviour', 'units': 3},
    {'code': 'GDBA 522', 'title': 'Financial Accounting II', 'units': 3},
    {'code': 'GDBA 523', 'title': 'Human Resource Management', 'units': 3},
    {'code': 'GDBA 524', 'title': 'Introduction to Strategic Management', 'units': 3},
    {'code': 'GDBA 525', 'title': 'Information Systems for Business', 'units': 3},
    {'code': 'GDBA 526', 'title': 'Entrepreneurship Development', 'units': 3},
    {'code': 'GDBA 600', 'title': 'Bridging Project (Directed Study)', 'units': 2},
]

with open('database/seeders/brochure_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"MBA Specs parsed: {len(data['programmes']['MBA']['specialisations'])}")
print(f"DBA Specs parsed: {len(data['programmes']['DBA']['specialisations'])}")
