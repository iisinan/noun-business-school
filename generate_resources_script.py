with open('resources/js/Pages/Resources.vue', 'r') as f:
    resources = f.read()

# We need to replace the <script setup> to add reactivity and data
script_start = resources.find('<script setup>')
script_end = resources.find('</script>') + len('</script>')

new_script = """<script setup>
import { Head, Link } from '@inertiajs/vue3';
import { ref } from 'vue';

const documentResources = ref([
    {
        id: 'brochure',
        title: 'Official Course Brochure (2026/2027)',
        category: 'Admissions',
        description: 'Comprehensive breakdown of all 28 MBA and DBA specialisation tracks, course units, and faculty profiles for the upcoming academic year. This guide contains everything you need to know about our executive programmes.',
        fileSize: '4.2 MB',
        pages: 34,
        updatedAt: 'August 2026',
        previewImage: 'https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=800&q=80',
        downloadUrl: '#',
    },
    {
        id: 'handbook',
        title: 'Student Handbook',
        category: 'Student Life',
        description: 'Policies, procedures, grading rubrics, and the code of conduct for all enrolled candidates in NOUN Business School.',
        fileSize: '1.8 MB',
        pages: 120,
        updatedAt: 'January 2026',
        previewImage: 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800&q=80',
        downloadUrl: '#',
    },
    {
        id: 'calendar',
        title: 'Academic Calendar',
        category: 'Administration',
        description: 'Important dates for the current academic session including residency periods, examination windows, and holidays.',
        fileSize: '0.5 MB',
        pages: 2,
        updatedAt: 'September 2026',
        previewImage: 'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&q=80',
        downloadUrl: '#',
    },
    {
        id: 'timetable',
        title: 'Lecture Timetable - Fall Semester',
        category: 'Academics',
        description: 'Detailed schedule for physical residencies and online live sessions for all MBA and DBA cohorts.',
        fileSize: '1.1 MB',
        pages: 5,
        updatedAt: 'August 2026',
        previewImage: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80',
        downloadUrl: '#',
    }
]);

const selectedResource = ref(documentResources.value[0]);
</script>"""

resources = resources.replace(resources[script_start:script_end], new_script)

# Now we replace the "Key Downloads" section with the new split-pane design.
old_downloads_start = resources.find('<!-- Key Downloads -->')
old_downloads_end = resources.find('<!-- Portals & Digital Resources -->')

new_downloads_html = """<!-- Interactive Document Viewer -->
            <section class="py-16 relative bg-gray-50 border-b border-gray-200">
                <div class="max-w-[90rem] mx-auto px-4 sm:px-6 lg:px-8">
                    
                    <div class="flex flex-col lg:flex-row gap-8 bg-white rounded-3xl shadow-[0_8px_30px_rgba(0,0,0,0.04)] border border-gray-100 overflow-hidden min-h-[600px]" v-reveal>
                        
                        <!-- Left Side: List of Resources -->
                        <div class="w-full lg:w-1/3 bg-gray-50/50 border-r border-gray-100 flex flex-col">
                            <div class="p-6 border-b border-gray-100 bg-white">
                                <h3 class="text-xl font-bold text-noun-dark">Document Library</h3>
                                <p class="text-sm text-gray-500 mt-1">Select a document to preview</p>
                            </div>
                            
                            <div class="flex-grow overflow-y-auto p-4 space-y-2 h-[500px]">
                                <button 
                                    v-for="doc in documentResources" 
                                    :key="doc.id"
                                    @click="selectedResource = doc"
                                    class="w-full text-left p-4 rounded-2xl transition-all duration-300 border group"
                                    :class="selectedResource.id === doc.id ? 'bg-noun-green/10 border-noun-green/30 shadow-sm' : 'bg-white border-transparent hover:border-gray-200 hover:bg-gray-50'"
                                >
                                    <div class="flex items-start gap-4">
                                        <div class="w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0 transition-colors"
                                             :class="selectedResource.id === doc.id ? 'bg-noun-green text-white' : 'bg-gray-100 text-gray-400 group-hover:bg-gray-200 group-hover:text-noun-dark'">
                                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                                        </div>
                                        <div>
                                            <div class="text-xs font-bold uppercase tracking-wider mb-1" :class="selectedResource.id === doc.id ? 'text-noun-green' : 'text-gray-400'">{{ doc.category }}</div>
                                            <h4 class="font-bold text-sm leading-tight transition-colors" :class="selectedResource.id === doc.id ? 'text-noun-dark' : 'text-gray-600 group-hover:text-noun-dark'">{{ doc.title }}</h4>
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </div>

                        <!-- Right Side: Preview & Download -->
                        <div class="w-full lg:w-2/3 p-8 lg:p-12 flex flex-col bg-white">
                            <div class="flex flex-col md:flex-row gap-8 h-full">
                                
                                <!-- Document Preview Image -->
                                <div class="w-full md:w-1/2 flex flex-col items-center justify-center bg-gray-100 rounded-2xl overflow-hidden relative shadow-inner border border-gray-200 group">
                                    <!-- A mock preview frame -->
                                    <img :src="selectedResource.previewImage" :alt="selectedResource.title" class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-500 mix-blend-multiply" />
                                    <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-noun-dark/20 backdrop-blur-[2px]">
                                        <div class="bg-white/90 text-noun-dark px-4 py-2 rounded-full font-bold text-sm shadow-lg flex items-center gap-2">
                                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                                            Preview
                                        </div>
                                    </div>
                                </div>

                                <!-- Document Details & Actions -->
                                <div class="w-full md:w-1/2 flex flex-col">
                                    <div class="inline-block bg-noun-yellow/20 text-noun-dark text-xs font-bold tracking-widest uppercase mb-4 px-3 py-1 rounded-full self-start">{{ selectedResource.category }}</div>
                                    <h2 class="text-3xl font-extrabold text-noun-dark mb-4 leading-tight">{{ selectedResource.title }}</h2>
                                    <p class="text-gray-600 mb-8 text-base leading-relaxed">{{ selectedResource.description }}</p>
                                    
                                    <div class="bg-gray-50 rounded-xl p-5 mb-8 border border-gray-100">
                                        <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">Document Information</h4>
                                        <div class="grid grid-cols-2 gap-4">
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">File Size</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.fileSize }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Pages</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.pages }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Last Updated</span>
                                                <span class="font-bold text-noun-dark">{{ selectedResource.updatedAt }}</span>
                                            </div>
                                            <div>
                                                <span class="block text-xs text-gray-500 mb-1">Format</span>
                                                <span class="font-bold text-noun-dark">PDF</span>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="mt-auto pt-4 flex flex-col sm:flex-row gap-4">
                                        <a :href="selectedResource.downloadUrl" class="flex-1 bg-noun-green text-white px-6 py-4 rounded-xl hover:bg-noun-dark font-bold text-center transition-all duration-300 shadow-[0_4px_15px_rgba(0,102,0,0.2)] hover:shadow-[0_8px_25px_rgba(0,102,0,0.3)] hover:-translate-y-0.5 flex items-center justify-center gap-2">
                                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                                            Download Document
                                        </a>
                                    </div>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>
            </section>

            """

resources = resources.replace(resources[old_downloads_start:old_downloads_end], new_downloads_html)

with open('resources/js/Pages/Resources.vue', 'w') as f:
    f.write(resources)

print("Split pane added to Resources.vue")
