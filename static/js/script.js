document.addEventListener('DOMContentLoaded', function () {
    const selectElement = document.getElementById('category-select');
    selectElement.addEventListener('change', function () {
        document.getElementById('category-filter-form').submit();
    });
});