with open('resources/js/Pages/Student/Statement.vue', 'r') as f:
    content = f.read()

target = """            <!-- Signatures -->
            <div class="relative z-10 grid grid-cols-2 gap-12 mt-20 pt-10">
                <div class="text-center">
                    <div class="border-b border-gray-400 w-48 mx-auto mb-2"></div>
                    <p class="text-xs font-bold text-gray-600 uppercase">Bursary Stamp & Signature</p>
                    <p class="text-[10px] text-gray-400 mt-1">Official Verification</p>
                </div>
                <div class="text-center">
                    <div class="border-b border-gray-400 w-48 mx-auto mb-2"></div>
                    <p class="text-xs font-bold text-gray-600 uppercase">Student Signature</p>
                    <p class="text-[10px] text-gray-400 mt-1">Date: ________________</p>
                </div>
            </div>"""

content = content.replace(target, "")

with open('resources/js/Pages/Student/Statement.vue', 'w') as f:
    f.write(content)
