with open('resources/views/applicant/application-docket.blade.php', 'r') as f:
    content = f.read()

target = """            <div class="flex justify-between mt-10 px-10">
                <div class="text-center w-48">
                    <div class="border-b border-black mb-2"></div>
                    <span class="text-xs font-bold">Applicant's Signature</span>
                </div>
                <div class="text-center w-32">
                    <div class="border-b border-black mb-2"></div>
                    <span class="text-xs font-bold">Date</span>
                </div>
            </div>"""

content = content.replace(target, "")

with open('resources/views/applicant/application-docket.blade.php', 'w') as f:
    f.write(content)
