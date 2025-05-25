document.querySelectorAll('.sort-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const sortInput = this.querySelector('input[name="sort"]');
        sortInput.value = sortInput.value === 'asc' ? 'desc' : 'asc';
        this.submit();
    });
});