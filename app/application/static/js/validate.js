let orderNum = 0;

function validateID(form) {
    var apiUrl = "http://localhost:5000/validate"
    console.log("HI");
    fetch(apiUrl, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        Name: form.cName.data,
        RestaurantID: parseInt(form.restID.data),
        TableNum: parseInt(form.tableNum.data)
    })
    }).then(data => {
        console.log(data);
        if (data == "True") {
          window.location.replace('http://localhost:5000/order');
        }
    }).catch(err => {
        console.log(err);
      // Do something for an error here
    });

}

function makeOrder(form) {
    orderNum += 1;
    fetch("http://localhost:5000/createOrder", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            "OrderNum" : orderNum,
            "ReceiptNum": 0,
            "TableNum" : form.tableNum
    })
    }).catch(err => {
        console.log(err);
    });
}