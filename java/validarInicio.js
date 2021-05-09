$(document).ready(function(){
    $("#error").hide(); //ocultarfeederror
    $("#formulario_IniciarSesion").submit(function(){
      var mensaje = "Revisa los siguientes detalles en el formulario";
      if($("#correo").val().trim().length == 0){
        mensaje = mensaje + " / " + " Debe ingresar un correo valido"
      }
      if($("#contra").val().trim().length == 0){
        mensaje = mensaje + " / " + " Debe ingresar una contraseña: "
      }
      if(mensaje != "Revisa los siguientes detalles en el formulario"){
        $("#error").html(mensaje);
        $("#error").show();
        event.preventDefault();
      }
    });
  });
$(document).ready(function(){

})