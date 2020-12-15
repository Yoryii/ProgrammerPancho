function validar(form){
    var cad=validarLimite(form.limiteSemestre.value);
    if(cad!=''){
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
       return true; 
       return true; 
    }
}

function validarLimite(limite){
    if(limite > 8 || limite < 1){
        return 'El semestre límite debe estar en el rango 1 - 8';
    } else {
        return '';
    }
}

