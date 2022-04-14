let orderNum = 0;

if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
}

function validateID(restID) {
    console.log(restID)
    fetch("http://localhost:5000/validate", {
    method: "POST",
    headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin':'*'},
    body: JSON.stringify({
        "RestaurantID": parseInt(restID),
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

function makeOrder(){
    orderNum += 1;
    var tableNum = form.tableNum.data;
    fetch('http://localhost:5000/createOrder',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            "OrderNum": orderNum,
            "TableNum": tableNum
        })
    }).catch(err => {
        console.log(err)
    })
}