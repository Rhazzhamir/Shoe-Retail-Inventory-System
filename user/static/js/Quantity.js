function updateQuantityDisplay(value, id) {
    document.getElementById('quantity-display-' + id).innerText = 'Quantity: ' + value;
}

function increaseNumber(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    element.value = value;
    updateQuantityDisplay(value, id.split('-')[1]); // Update the correct display
}

function decreaseNumber(id) {
    var element = document.getElementById(id);
    var value = parseInt(element.value, 10);
    value = isNaN(value) ? 0 : value;
    value = value > 0 ? value - 1 : 0;
    element.value = value;
    updateQuantityDisplay(value, id.split('-')[1]); // Update the correct display
}


document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.cart-checkbox');
    const totalAmountElement = document.getElementById('product_total_amt');

    function updateTotalAmount() {
        let total = 0;

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                const productId = checkbox.getAttribute('data-id');
                const price = parseFloat(checkbox.getAttribute('data-price'));
                const quantityInput = document.getElementById(`textbox-${productId}`);
                const quantity = parseInt(quantityInput.value, 10) || 0;

                total += price * quantity;
            }
        });

        totalAmountElement.textContent = total.toFixed(2);
    }

    // Update total when checkboxes are checked/unchecked
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateTotalAmount);
    });

    // Update total dynamically when quantity changes
    const quantityInputs = document.querySelectorAll('[id^="textbox-"]');
    quantityInputs.forEach(input => {
        input.addEventListener('input', () => {
            const productId = input.getAttribute('data-id');
            const relatedCheckbox = document.querySelector(`.cart-checkbox[data-id="${productId}"]`);

            if (relatedCheckbox.checked) {
                updateTotalAmount();
            }
        });
    });
});

