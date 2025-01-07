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
function addToCart(productName, productPrice, productImage) {
    var cartContainer = document.getElementById('cart-container');
    var newCartItem = `
        <div class="card p-4">
            <div class="row">
                <div class="col-md-5 col-11 mx-auto bg-light d-flex justify-content-center align-items-center shadow product_img">
                    <img src="${productImage}" class="img-fluid" alt="cart img">
                </div>
                <div class="col-md-7 col-11 mx-auto px-4 mt-2">
                    <div class="row">
                        <div class="col-6 card-title">
                            <h1 class="mb-4 product_name text-light noto-serif-ahom-regular">${productName}</h1>
                            <p class="mb-2 text-light">Price: ${productPrice}</p>
                            <p class="mb-2 text-light">Size:</p>
                            <p class="mb-3 text-light" id="quantity-display">Quantity: 1</p>
                        </div>
                        <div class="col-6">
                            <ul class="pagination justify-content-end set_quantity">
                                <li class="page-item">
                                    <button class="page-link" onclick="decreaseNumber('textbox')">
                                        <i class="fas fa-minus"></i>
                                    </button>
                                </li>
                                <li class="page-item">
                                    <input type="text" class="page-link" value="1" id="textbox" readonly>
                                </li>
                                <li class="page-item">
                                    <button class="page-link" onclick="increaseNumber('textbox')">
                                        <i class="fas fa-plus"></i>
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="row d-flex justify-content-end">
                        <button class="delete_cart">
                            <svg viewBox="0 0 15 17.5" height="17.5" width="15" xmlns="http://www.w3.org/2000/svg" class="icon">
                                <path transform="translate(-2.5 -1.25)" d="M15,18.75H5A1.251,1.251,0,0,1,3.75,17.5V5H2.5V3.75h15V5H16.25V17.5A1.251,1.251,0,0,1,15,18.75ZM5,5V17.5H15V5Zm7.5,10H11.25V7.5H12.5V15ZM8.75,15H7.5V7.5H8.75V15ZM12.5,2.5h-5V1.25h5V2.5Z" id="Fill"></path>
                            </svg>
                        </button>
                        <div class="checkbox checkbox-wrapper-12">
                            <div class="cbx">
                                <input type="checkbox" id="cbx-12">
                                <label for="cbx-12"></label>
                                <svg fill="none" viewBox="0 0 15 14" height="14" width="15">
                                    <path d="M2 8.36364L6.23077 12L13 2"></path>
                                </svg>
                            </div>
                            <svg version="1.1" xmlns="http://www.w3.org/2000/svg">
                                <defs>
                                    <filter id="goo-12">
                                        <feGaussianBlur result="blur" stdDeviation="4" in="SourceGraphic"></feGaussianBlur>
                                        <feColorMatrix result="goo-12" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -7" mode="matrix" in="blur"></feColorMatrix>
                                        <feBlend in2="goo-12" in="SourceGraphic"></feBlend>
                                    </filter>
                                </defs>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <hr />
    `;
    cartContainer.innerHTML += newCartItem;
    alert('Add to cart success');
}