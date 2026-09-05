with open('resources/js/Pages/Student/Slip.vue', 'r') as f:
    content = f.read()

target = """            <!-- Signatures -->
            <div class="mt-16 pt-8 flex justify-between relative z-10">
                <div class="w-64 text-center">
                    <div class="border-b border-gray-400 mb-2"></div>
                    <p class="text-xs text-gray-600 font-bold uppercase">Student Signature & Date</p>
                </div>
                <div class="w-64 text-center">
                    <div class="border-b border-gray-400 mb-2"></div>
                    <p class="text-xs text-gray-600 font-bold uppercase">Study Centre Director Signature & Stamp</p>
                </div>
            </div>"""

content = content.replace(target, "")

with open('resources/js/Pages/Student/Slip.vue', 'w') as f:
    f.write(content)
