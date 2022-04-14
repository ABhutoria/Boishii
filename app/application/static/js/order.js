// Adapted from: https://github.com/WebDevSimplified/Introduction-to-Web-Development/blob/master/Introduction%20to%20JavaScript/Lesson%201/store.js

if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    var removeOrderItemButtons = document.getElementsByClassName('btn-danger')
    for (var i = 0; i < removeOrderItemButtons.length; i++) {
        var button = removeOrderItemButtons[i]
        button.addEventListener('click', removeOrderItem)
    }

    var quantityInputs = document.getElementsByClassName('order-quantity-input')
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i]
        input.addEventListener('change', quantityChanged)
    }

    // for adding when user clicks item, add to order list
    var addToOrderButtons = document.getElementsByClassName('card')
    for (var i = 0; i < addToOrderButtons.length; i++) {
        var button = addToOrderButtons[i]
        button.addEventListener('click', addToCartClicked)
    }

    document.getElementsByClassName('btn-purchase')[0].addEventListener('click', purchaseClicked)
}

function purchaseClicked() {
    alert('Thank you for your purchase')
    var orderItems = document.getElementsByClassName('order-items')[0]
    while (orderItems.hasChildNodes()) {
        orderItems.removeChild(orderItems.firstChild)
    }
    updateOrderTotal()
}

function removeOrderItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateOrderTotal()
}

function quantityChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateOrderTotal()
}

function addToOrderClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var title = shopItem.getElementsByClassName('card-content')[0].innerText
    // var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    // var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    addItemToOrder(title, NULL, NULL)
    updateOrderTotal()
}

function addItemToOrder(title, price, imageSrc) {
    var orderRow = document.createElement('div')
    orderRow.classList.add('order-row')
    var orderItems = document.getElementsByClassName('order-items')[0]
    var orderItemNames = orderItems.getElementsByClassName('order-item-title')
    for (var i = 0; i < orderItemNames.length; i++) {
        if (orderItemNames[i].innerText == title) {
            alert('This item is already added to the cart')
            return
        }
    }
    var cartRowContents = `
        <div class="order-item order-column">
            <img class="order-item-image" src="${imageSrc}" width="100" height="100">
            <span class="order-item-title">${title}</span>
        </div>
        <span class="order-price order-column">${price}</span>
        <div class="order-quantity order-column">
            <input class="order-quantity-input" type="number" value="1">
            <button class="btn btn-danger" type="button">REMOVE</button>
        </div>`
    orderRow.innerHTML = orderRowContents
    orderItems.append(orderRow)
    orderRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeOrderItem)
    orderRow.getElementsByClassName('order-quantity-input')[0].addEventListener('change', quantityChanged)
}

function updateOrderTotal() {
    var orderItemContainer = document.getElementsByClassName('order-items')[0]
    var orderRows = cartItemContainer.getElementsByClassName('order-row')
    var total = 0
    for (var i = 0; i < orderRows.length; i++) {
        var orderRow = orderRows[i]
        var priceElement = orderRow.getElementsByClassName('order-price')[0]
        var quantityElement = cartRow.getElementsByClassName('order-quantity-input')[0]
        var price = parseFloat(priceElement.innerText.replace('$', ''))
        var quantity = quantityElement.value
        total = total + (price * quantity)
    }
    total = Math.round(total * 100) / 100
    document.getElementsByClassName('order-total-price')[0].innerText = '$' + total
}


//Adapted from: https://codesandbox.io/s/agitated-tu-97n1i?file=/index.js
function toggleMobileMenu(menu) {
    menu.classList.toggle('open');
}


// function retrieveMenuItem(item){




// }