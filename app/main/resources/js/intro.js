// app/static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    // Show the initial message
    const intro = document.getElementById("intro");
    const message = document.getElementById("message");
    const moreContent = document.getElementById("more-content");

    // After 1.5 seconds, hide the intro and show the message with fade-out and fade-in effects
    setTimeout(() => {
        intro.classList.add("fade-out");
        setTimeout(() => {
            intro.classList.add("hidden");
            message.classList.remove("hidden");
            message.classList.add("fade-in");
        }, 500);
    }, 1000);

    // After another 2 seconds, hide the message and show more content with fade-out and fade-in effects
    setTimeout(() => {
        message.classList.add("fade-out");
        setTimeout(() => {
            message.classList.add("hidden");
            moreContent.classList.remove("hidden");
            moreContent.classList.add("fade-in");
        }, 500);
    }, 3000);

    // Show more content when scrolling down
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) { // Adjust the scroll threshold as needed
            moreContent.classList.add("fade-in");
        }
    });
});
