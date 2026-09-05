with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'r') as f:
    content = f.read()

target = """            onError: () => {
                submitLoader.value.active = false;
            }"""
replacement = """            onError: (errors) => {
                submitLoader.value.active = false;
                const serverErrors = Object.values(errors).flat();
                if (serverErrors.length > 0) {
                    validationErrors.value = serverErrors;
                    setTimeout(() => { validationErrors.value = []; }, 8000);
                }
            }"""
content = content.replace(target, replacement)

with open('resources/js/Pages/Applicant/ApplicationForm.vue', 'w') as f:
    f.write(content)
