function guardar() {
    let n = document.getElementById("nombre").value
    let p = parseFloat(document.getElementById("precio").value)
    let s = parseInt(document.getElementById("stock").value)
    let i = document.getElementById("imagen").value


    let habitacion = {
        nombre: n,
        precio: p,
        stock: s,
        imagen: i
    }
    let url = "http://localhost:5000/habitaciones"
    var options = {
        body: JSON.stringify(habitacion),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./habitaciones.html";  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}

function Volver() {
  
    let url = "http://localhost:5000/habitaciones"
    var options = {
        body: JSON.stringify(habitacion),
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("volver")
            alert("volver")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../templates/habitaciones.html";  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al volver" )
            console.error(err);
        })
}