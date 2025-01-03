function increaseNumber(textboxId) {
    console.log("Increasing number");
    var textbox = document.getElementById(textboxId);
    var currentValue = parseInt(textbox.value);
    textbox.value = currentValue + 1;
}

function decreaseNumber(textboxId) {
    console.log("Decreasing number");
    var textbox = document.getElementById(textboxId);
    var currentValue = parseInt(textbox.value);
    if (currentValue > 0) {
        textbox.value = currentValue - 1;
    }
}

