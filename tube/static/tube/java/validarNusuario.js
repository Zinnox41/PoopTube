$(document).ready(function(){
  $("#error").hide(); //ocultarfeederror
  $("#formulario_CrearUsuario").submit(function(){
    var mensaje = "Revisa los siguientes detalles en el formulario";
    //Usuario
    if($("#nombreu").val().trim().length == 0){
      mensaje = mensaje + "<br>USUARIO" + " <br>-No ingreso usuario";
    }
    
    //Correo
    if($("#correo").val().trim().length == 0){
      mensaje = mensaje + "<br>email:" + "<br>No ingreso su correo electronico";
    }
    //Contraseña
    if ($("#contra").val() != $("#ccontra").val()) {
      mensaje = mensaje + "<br>CONTRASEÑA:" + "<br>-Las contraseñas deben ser iguales";
    }
    if ($("#contra").val().trim().length == 0) {
      mensaje = mensaje + "<br>-La contraseña no debe estar vacia";
    }
   
    //Terminos
    if ($("#checko").is(':not(:checked)')) {
    }
    if(mensaje != "Revisa los siguientes detalles en el formulario"){
      $("#error").html(mensaje);
      $("#error").show();
      event.preventDefault();
    }
  });
});