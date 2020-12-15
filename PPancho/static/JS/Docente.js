function validar(form){
	var cad=validaridDocente(form.idDocente.value);
    cad+=validariCedula(form.cedula.value);

    if(cad!=''){
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
       return true; 
    }
}


function validaridDocente(cad){
	var patron=/\d{8}/;
    if(patron.test(cad)){
        return '';
    }
    else{
        return "El id debe ser de 8 digitos <br>";
    }
}

function validariCedula(cad){
    var patron=/\d{8}/;
    if(patron.test(cad)){
        return '';
    }
    else{
        return "La cedula debe llevar 8 digitos <br>";
    }
}
