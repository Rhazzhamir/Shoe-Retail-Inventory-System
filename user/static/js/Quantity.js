function updateQuantityDisplay(value) {
    document.getElementById('quantity-display').innerText = 'Quantity: ' + value;
}

function increaseNumber(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    element.value = value;
    updateQuantityDisplay(value);
}

function decreaseNumber(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value, 10);
    value = isNaN(value) ? 0 : value;
    value = value > 0 ? value - 1 : 0;
    element.value = value;
    updateQuantityDisplay(value);
}
