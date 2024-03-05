console.log("index.js");

// Function to update URL parameters based on the current state of checkboxes
function updateURLParameters() {
    const searchParams = new URLSearchParams(window.location.search);

    // Group checkboxes by their 'name' attribute and then update search params for each group
    document.querySelectorAll('.filters input[type="checkbox"]').forEach(checkbox => {
        const filterName = checkbox.name; // categories, product_status, etc.
        const selectedValues = Array.from(document.querySelectorAll(`.filters input[type="checkbox"][name="${filterName}"]:checked`))
                                    .map(input => encodeURIComponent(input.value));

        if (selectedValues.length > 0) {
            searchParams.set(filterName, selectedValues.join(','));
        } else {
            searchParams.delete(filterName);
        }
    });

    // Update the URL without reloading the page
    window.history.pushState({}, '', `${location.pathname}?${searchParams}`);
}

// Attach change event listener to each checkbox
document.querySelectorAll('.filters input[type="checkbox"]').forEach(input => {
    input.addEventListener('change', function() {
        console.log("changed", input.name, input.value);
        updateURLParameters(); // Update URL parameters based on the current checkbox states
    });
});
