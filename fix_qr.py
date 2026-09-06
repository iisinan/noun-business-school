file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/IdCard.vue'
with open(file_path, 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "api.qrserver.com" in line:
        lines[i] = '                        <img :src="\'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=NBS/\' + application.academic_session_id + \'/\' + String(application.id).padStart(4, \'0\')" alt="QR Code" class="w-16 h-16 mx-auto mb-2 opacity-90">\n'

with open(file_path, 'w') as f:
    f.writelines(lines)
