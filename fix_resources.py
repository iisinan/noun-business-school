with open('resources/js/Pages/Resources.vue', 'r') as f:
    resources = f.read()

# Add the vReveal directive right before </script>
directive = """
const vReveal = {
    mounted: (el, binding) => {
        const delay = binding.value || 0;
        el.classList.add('opacity-0', 'translate-y-8', 'transition-all', 'duration-1000', 'ease-out');
        if (delay) el.style.transitionDelay = `${delay}ms`;
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    el.classList.remove('opacity-0', 'translate-y-8');
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
        
        observer.observe(el);
    }
};
"""

resources = resources.replace('</script>', directive + '\n</script>')

with open('resources/js/Pages/Resources.vue', 'w') as f:
    f.write(resources)

print("Fixed vReveal in Resources.vue")
