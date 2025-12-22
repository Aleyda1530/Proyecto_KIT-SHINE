// VALIDACIONES DE FORMULARIOS – KIT SHINE

// CONTACTO
function validarContacto() {
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var correo = document.getElementById("correo").value.trim();
    var mensaje = document.getElementById("mensaje").value.trim();

    if (nombre === "" || apellido === "" || correo === "" || mensaje === "") {
        alert("Por favor completa todos los campos obligatorios.");
        return false;
    }

    if (!correo.includes("@")) {
        alert("Ingresa un correo válido.");
        return false;
    }

    return true;
}


// PEDIDOS
function validarPedido() {
    var nombre = document.getElementById("ped-nombre").value.trim();
    var apellido = document.getElementById("ped-apellido").value.trim();
    var dni = document.getElementById("dni").value.trim();
    var direccion = document.getElementById("direccion").value.trim();
    var correo = document.getElementById("ped-correo").value.trim();
    var producto = document.getElementById("ped-producto").value;
    var pago = document.getElementById("ped-pago").value;

    if (
        nombre === "" ||
        apellido === "" ||
        dni === "" ||
        direccion === "" ||
        correo === "" ||
        producto === "" ||
        pago === ""
    ) {
        alert("Por favor completa todos los campos obligatorios.");
        return false;
    }

    if (dni.length !== 8 || isNaN(dni)) {
        alert("El DNI debe contener exactamente 8 números.");
        return false;
    }

    if (!correo.includes("@")) {
        alert("Ingresa un correo electrónico válido.");
        return false;
    }

    if (direccion.length < 10) {
        alert("La dirección es demasiado corta.");
        return false;
    }

    return true;
}


// OPINIONES
function validarOpinion() {
    var nombre = document.getElementById("op-nombre").value.trim();
    var apellido = document.getElementById("op-apellido").value.trim();
    var calificacion = document.getElementById("op-calificacion").value;
    var comentario = document.getElementById("op-comentario").value.trim();

    if (nombre === "" || apellido === "" || calificacion === "" || comentario === "") {
        alert("Por favor completa todos los campos obligatorios.");
        return false;
    }

    if (comentario.length < 10) {
        alert("La reseña debe tener al menos 10 caracteres.");
        return false;
    }

    return true;
}