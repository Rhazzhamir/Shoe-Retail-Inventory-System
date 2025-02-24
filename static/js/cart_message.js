document.addEventListener("DOMContentLoaded", function () {
    const messageBox = document.getElementById('cart-message');
    if (messageBox) {
        // Set a timeout to hide the message after 5 seconds
        setTimeout(() => {
            messageBox.style.transition = "opacity 0.5s ease";
            messageBox.style.opacity = "0"; // Fade out the message
            setTimeout(() => {
                messageBox.style.display = "none"; // Remove it from the DOM
            }, 500); // Allow time for the fade-out effect
        }, 5000); // Wait for 5 seconds
    }
});
