with open('resources/js/Pages/Student/Results.vue', 'r') as f:
    content = f.read()

# Update props
target_props = """const props = defineProps({
    resultsBySession: { type: Array, default: () => [] },
    cgpa: Number,
    cumulativeCredits: Number
});"""
replacement_props = """const props = defineProps({
    resultsBySession: { type: Array, default: () => [] },
    cgpa: Number,
    cumulativeCredits: Number,
    hasAnyGrades: { type: Boolean, default: false }
});"""

if target_props in content:
    content = content.replace(target_props, replacement_props)
    
# Update v-if
target_vif = """                <a v-if="resultsBySession && resultsBySession.length > 0" :href="route('student.results.download')" target="_blank" class="inline-flex items-center gap-2 bg-noun-green hover:bg-noun-dark text-white px-4 py-2 rounded-lg font-semibold transition-colors duration-200 shadow-sm text-sm">"""
replacement_vif = """                <a v-if="hasAnyGrades" :href="route('student.results.download')" target="_blank" class="inline-flex items-center gap-2 bg-noun-green hover:bg-noun-dark text-white px-4 py-2 rounded-lg font-semibold transition-colors duration-200 shadow-sm text-sm">"""

if target_vif in content:
    content = content.replace(target_vif, replacement_vif)
    
with open('resources/js/Pages/Student/Results.vue', 'w') as f:
    f.write(content)
print("Patched Results.vue props and v-if")
