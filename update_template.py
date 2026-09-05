import re

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

# Step 1
content = content.replace(
    'v-model="form.programme_id" class="block w-full rounded-lg border-gray-300',
    'v-model="form.programme_id" :class="errorClass(\'programme_id\')" class="block w-full rounded-lg'
)
content = content.replace(
    'v-model="form.specialisation_id" class="block w-full rounded-lg border-gray-300',
    'v-model="form.specialisation_id" :class="errorClass(\'specialisation_id\')" class="block w-full rounded-lg'
)

# Step 2
for field in ['full_name', 'gender', 'marital_status', 'dob', 'nationality', 'nationality_other', 'state_of_origin', 'phone', 'email', 'address']:
    content = content.replace(
        f'v-model="form.personal_info.{field}" class="block w-full rounded-lg border-gray-300',
        f'v-model="form.personal_info.{field}" :class="errorClass(\'{field}\')" class="block w-full rounded-lg'
    )
    # Also handle the readonly ones where readonly is before class
    content = content.replace(
        f'v-model="form.personal_info.{field}" readonly class="block w-full rounded-lg border-gray-300',
        f'v-model="form.personal_info.{field}" readonly :class="errorClass(\'{field}\')" class="block w-full rounded-lg'
    )

# Step 3
content = content.replace('v-model="edu.institution" class="block w-full rounded-lg border-gray-300', 'v-model="edu.institution" :class="errorClass(\'edu_institution_\'+index)" class="block w-full rounded-lg')
content = content.replace('v-model="edu.qualification" class="block w-full rounded-lg border-gray-300', 'v-model="edu.qualification" :class="errorClass(\'edu_qualification_\'+index)" class="block w-full rounded-lg')
content = content.replace('v-model="edu.course_of_study" class="block w-full rounded-lg border-gray-300', 'v-model="edu.course_of_study" :class="errorClass(\'edu_course_\'+index)" class="block w-full rounded-lg')
content = content.replace('v-model="edu.grade" class="block w-full rounded-lg border-gray-300', 'v-model="edu.grade" :class="errorClass(\'edu_grade_\'+index)" class="block w-full rounded-lg')

content = content.replace('v-model="olevel.exam_type" class="block w-full rounded-lg border-gray-300', 'v-model="olevel.exam_type" :class="errorClass(\'olevel_type_\'+index)" class="block w-full rounded-lg')
content = content.replace('v-model="olevel.exam_year" class="block w-full rounded-lg border-gray-300', 'v-model="olevel.exam_year" :class="errorClass(\'olevel_year_\'+index)" class="block w-full rounded-lg')
content = content.replace('v-model="olevel.exam_number" class="block w-full rounded-lg border-gray-300', 'v-model="olevel.exam_number" :class="errorClass(\'olevel_number_\'+index)" class="block w-full rounded-lg')

# Step 4
content = content.replace('v-model="form.employment_info.organisation" class="block w-full rounded-lg border-gray-300', 'v-model="form.employment_info.organisation" :class="errorClass(\'emp_organisation\')" class="block w-full rounded-lg')
content = content.replace('v-model="form.employment_info.job_title" class="block w-full rounded-lg border-gray-300', 'v-model="form.employment_info.job_title" :class="errorClass(\'emp_job_title\')" class="block w-full rounded-lg')
content = content.replace('v-model="form.employment_info.years_experience" class="block w-full rounded-lg border-gray-300', 'v-model="form.employment_info.years_experience" :class="errorClass(\'emp_years\')" class="block w-full rounded-lg')


with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)

