function toggleHelpBox() {
    const chatBox = document.getElementById("chatBox");
    chatBox.style.display = chatBox.style.display === "block" ? "none" : "block";
}

function handleChatSubmit(event) {
    event.preventDefault(); // Prevent form submission
    const input = event.target.querySelector("input");
    console.log("User message:", input.value);
    input.value = ""; // Clear input field
}