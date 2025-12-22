// CUENTA – MOSTRAR BOLETA DESDE EL CARRITO

var carrito = JSON.parse(localStorage.getItem("carrito")) || [];
var boletaItems = document.getElementById("boleta-items");
var boletaTotal = document.getElementById("boleta-total");

function cargarBoleta() {

    boletaItems.innerHTML = "";
    var total = 0;

    if (carrito.length === 0) {
        boletaItems.innerHTML =
            "<tr><td colspan='4'>No hay productos en la boleta.</td></tr>";
        return;
    }

    for (var i = 0; i < carrito.length; i++) {
        var p = carrito[i];
        var subtotal = p.precio * p.cantidad;
        total += subtotal;

        boletaItems.innerHTML +=
            "<tr>" +
                "<td>" + p.nombre + "</td>" +
                "<td>" + p.cantidad + "</td>" +
                "<td>S/ " + p.precio.toFixed(2) + "</td>" +
                "<td>S/ " + subtotal.toFixed(2) + "</td>" +
            "</tr>";
    }

    boletaTotal.textContent = total.toFixed(2);
}

// Cargar boleta al abrir la página
cargarBoleta();