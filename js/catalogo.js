
// CATALOGO – AGREGAR PRODUCTOS AL CARRITO


// Cargar carrito desde localStorage o crear uno vacío
var carrito = JSON.parse(localStorage.getItem("carrito"));
if (carrito === null) {
    carrito = [];
}

// Agregar un producto
function agregarAlCarrito(nombre, precio) {
    var existe = false;

    for (var i = 0; i < carrito.length; i++) {
        if (carrito[i].nombre === nombre) {
            carrito[i].cantidad++;
            existe = true;
            break;
        }
    }

    if (!existe) {
        carrito.push({
            nombre: nombre,
            precio: precio,
            cantidad: 1
        });
    }

    localStorage.setItem("carrito", JSON.stringify(carrito));

    alert("Producto añadido al carrito");
}