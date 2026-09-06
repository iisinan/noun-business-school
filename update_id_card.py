file_path = '/Users/sinan/Herd/Business School/resources/js/Pages/Student/IdCard.vue'
with open(file_path, 'r') as f:
    content = f.read()

search = """                    <!-- Header -->
                    <div class="text-center pt-3 pb-2 px-2 flex flex-col items-center">
                        <img src="/nbs-logo.png" alt="NOUN Logo" class="h-10 w-auto mb-1 bg-white p-1 rounded-full shadow-sm">
                        <h2 class="text-[9px] font-black text-white leading-tight uppercase tracking-wide">National Open University<br>of Nigeria</h2>
                        <div class="bg-noun-yellow text-noun-dark text-[7px] font-bold px-2 py-0.5 rounded-full mt-1.5 uppercase tracking-widest shadow-sm">"""

replace = """                    <!-- Header -->
                    <div class="text-center pt-3 pb-1.5 px-2 flex flex-col items-center">
                        <img src="/nbs-logo.png" alt="NOUN Logo" class="h-9 w-auto mb-1 bg-white p-1 rounded-full shadow-sm">
                        <h2 class="text-[11px] font-black text-white leading-tight uppercase tracking-widest">NOUN Business School</h2>
                        <h3 class="text-[6px] font-medium text-white/90 leading-tight uppercase tracking-wider mt-0.5">National Open University of Nigeria</h3>
                        <div class="bg-noun-yellow text-noun-dark text-[7px] font-bold px-2 py-0.5 rounded-full mt-1.5 uppercase tracking-widest shadow-sm">"""

if search in content:
    content = content.replace(search, replace)
    with open(file_path, 'w') as f:
        f.write(content)
    print("Patched IdCard.vue")
else:
    print("Search block not found")
