// app/static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    // Show the initial message
    const intro = document.getElementById("intro");
    const message = document.getElementById("message");
    const moreContent = document.getElementById("more-content");

    // After 2 seconds, hide the intro and show the message
    setTimeout(() => {
        intro.classList.add("hidden"); // Hide intro immediately
        message.classList.remove("hidden"); // Show message
        message.classList.add("fadeIn"); // Fade in effect for message
    }, 1000);

    // After another 3 seconds, hide the message and show more content
    setTimeout(() => {
        message.classList.add("hidden"); // Hide message immediately
        moreContent.classList.remove("hidden"); // Show more content
        moreContent.classList.add("fadeIn"); // Fade in effect for more content
    }, 3000); // Adjust timing as needed

    // Show more content when scrolling down
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) { // Adjust the scroll threshold as needed
            moreContent.classList.add("fadeIn");
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const icons = document.querySelectorAll('.icon-container i');

    icons.forEach((icon, index) => {
        // Add the blue class when the icon fades in
        setTimeout(() => {
            icon.classList.add('blue'); // Turn icon blue
            setTimeout(() => {
                icon.classList.remove('blue'); // Revert back to black after 500ms
            }, 200); // Adjust timing as needed
        }, index * 190 + 4000); // Adjust timing based on your delay settings
    });
});