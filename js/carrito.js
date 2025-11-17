// Recuperamos el carrito desde localStorage.
// Si no existe, se crea un arreglo vacío.
var carrito = JSON.parse(localStorage.getItem("carrito"));
if (carrito === null) {
    carrito = [];
}

// Selección de elementos HTML
var tabla = document.getElementById("tabla-carrito");
var items = document.getElementById("carrito-items");
var totalMontoEl = document.getElementById("total-monto");
var totalDiv = document.getElementById("carrito-total");
var vacioMsg = document.getElementById("carrito-vacio");


// FUNCIÓN PARA MOSTRAR EL CARRITO EN LA TABLA

function mostrarCarrito() {

    // Si el carrito está vacío
    if (carrito.length === 0) {
        tabla.classList.add("oculto");
        totalDiv.classList.add("oculto");
        vacioMsg.classList.remove("oculto");
        return;
    }

    // Si tiene productos
    tabla.classList.remove("oculto");
    totalDiv.classList.remove("oculto");
    vacioMsg.classList.add("oculto");

    // Limpiamos la tabla antes de dibujarla de nuevo
    items.innerHTML = "";

    var total = 0;

    // Recorremos cada producto del carrito
    for (var i = 0; i < carrito.length; i++) {

        var producto = carrito[i];
        var subtotal = producto.precio * producto.cantidad;
        total += subtotal;

        // Agregamos filas a la tabla
        items.innerHTML +=
            "<tr>" +
                "<td>" + producto.nombre + "</td>" +
                "<td>" + producto.cantidad + "</td>" +
                "<td>S/ " + producto.precio.toFixed(2) + "</td>" +
                "<td>S/ " + subtotal.toFixed(2) + "</td>" +
                "<td><button onclick='eliminarProducto(" + i + ")'>X</button></td>" +
            "</tr>";
    }

    // Actualizamos el total en la página
    totalMontoEl.textContent = total.toFixed(2);
}


// FUNCIÓN PARA ELIMINAR UN PRODUCTO DEL CARRITO

function eliminarProducto(indice) {

    // Quitamos 1 elemento en la posición indicada
    carrito.splice(indice, 1);

    // Guardamos el carrito actualizado
    localStorage.setItem("carrito", JSON.stringify(carrito));

    // Actualizamos la tabla
    mostrarCarrito();
}


// FINALIZAR COMPRA

function finalizarCompra() {
    alert("¡Tu pedido está listo! Ahora puedes ver tu boleta en la sección 'Cuenta'.");
    window.location.href = "cuenta.html";
}


// Al entrar a la página, mostramos el carrito automáticamente
mostrarCarrito();