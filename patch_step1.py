with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = "const totalSteps = 4;"
replacement = """const totalSteps = 4;

const passportPreview = ref(null);
const submitLoader = ref({ active: false, text: '' });

const handlePassportUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
        if (file.size > 2 * 1024 * 1024) {
            alert('Passport photograph must be less than 2MB.');
            e.target.value = '';
            return;
        }
        form.passport_photograph = file;
        passportPreview.value = URL.createObjectURL(file);
    } else {
        form.passport_photograph = null;
        passportPreview.value = null;
    }
};"""

content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
