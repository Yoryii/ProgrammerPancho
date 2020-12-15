function validar(form){
    var cad = validarfechReg(form.fechar.value);
    cad+= validarfechEven(form.fechae.value);

    if (cad!='') {
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    } else {
        return true;
    }
}


function validarfechReg(fechar){
    var f = new Date();
    var fecha = fechar.value
    if (Date.parse(fecha) < Date.parse(f)) {
        return 'La fecha debe ser mayor a la fecha actual'
    } else {
        
    }
}

function validarfechEven(fechae){

}