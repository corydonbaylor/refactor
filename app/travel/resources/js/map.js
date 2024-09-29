document.addEventListener('DOMContentLoaded', () => {
    const countriesToColor = ['Angola', 'Hungary', 'United States', 'Canada', 'Spain', 'Portugal']; // Add desired country names here
    const svgObject = document.getElementById('world-map');

    // Wait for the object to load
    svgObject.addEventListener('load', () => {
        colorCountries(countriesToColor);
    });
});

function colorCountries(countryNames) {
    const svgObject = document.getElementById('world-map');
    const svgDoc = svgObject.contentDocument; // Access the SVG document
    
    if (!svgDoc) {
        console.error("SVG document is not accessible.");
        return;
    }

    const countries = svgDoc.getElementsByTagName('path'); // Get all path elements
    console.log(countries); // This should now log the paths

    Array.from(countries).forEach(country => {
        // Reset to transparent
        country.style.fill = 'transparent';
        // Check if the country should be colored based on its class name
        if (countryNames.includes(country.classList[0])) {
            country.style.fill = '#fef0cc'; // Change to desired color
        }
    });
}