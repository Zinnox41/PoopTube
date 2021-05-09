$(document).ready(function () {
    $("#error").hide(); //ocultarfeederror
    $("#formulario_CrearUsuario").submit(function () {
        var mensaje = "Revisa los siguientes detalles en el formulario";
        if ($("#nombreu").val().trim().length == 0) {
            mensaje = mensaje + " / " + " Usuario no debe estar vacio";
        }
        if ($("#correo").val().trim().length == 0) {
            mensaje = mensaje + " / " + " Debe ingresar un correo valido";
        }
        if ($("#correo").val().trim().length == 0) {
            mensaje = mensaje + " / " + " Debe ingresar un correo valido";
        }
        if ($("#contra").val().trim().length == 0) {
            mensaje = mensaje + " / " + " Debe ingresar una contraseña ";
        }
        if ($(contra.value != contra2.value)) {
            mensaje = mensaje + " / " + " Debe ingresar una contraseña ";
        }
        if ($("#contra2").val().trim().length == 0) {
            mensaje = mensaje + " / " + " Contraseña no coincide ";
        }
        if (mensaje != "Revisa los siguientes detalles en el formulario") {
            $("#error").html(mensaje);
            $("#error").show();
            event.preventDefault();
        }
    });
});