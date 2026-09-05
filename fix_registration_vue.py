import re

with open('resources/js/Pages/Student/Registration.vue', 'r') as f:
    content = f.read()

# Add layout imports and template wrap
target_script = """<script setup>
import { ref, computed } from 'vue';"""

replacement_script = """<script setup>
import { ref, computed } from 'vue';
import { Head } from '@inertiajs/vue3';
import StudentLayout from '@/Layouts/StudentLayout.vue';"""

content = content.replace(target_script, replacement_script)

target_template = """<template>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start relative">"""

replacement_template = """<template>
    <Head title="Course Registration" />
    <StudentLayout>
        <template #header>
            <h2 class="text-xl font-bold leading-tight text-noun-dark">Course Registration</h2>
        </template>
        
        <div class="py-8 px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start relative">"""

content = content.replace(target_template, replacement_template)

content += """
            </div>
        </div>
    </StudentLayout>
</template>"""

with open('resources/js/Pages/Student/Registration.vue', 'w') as f:
    f.write(content)

