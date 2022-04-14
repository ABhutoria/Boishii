// fetch("http://localhost:5000/getItem")
// .then(response => {
//     return response.json();
// })
// .then(item => {
//     console.log(item)
// })




fetch('http://localhost:5000/getItem',{
    method: 'GET',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        Name: "Pizza"
})
.then(resp => resp.json())
.then(data => document.body.innerHTML = "<h1>" + data.type + "</h1>")
