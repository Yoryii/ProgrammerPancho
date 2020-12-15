function validar(form){
    var cad=validarNControl(form.noControl.value);
    cad+=validarSemestre(form.semestre.value);

    if(cad!=''){
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
       return true; 
    }
}

function validarNControl(cad){
    var patron=/\d{8}/;
    if(patron.test(cad)){
        return '';
    }
    else{
        return "El número de control debe tener 8 dígitos <br>";
    }
}

function validarSemestre(semestre){
    if(semestre > 8 || semestre < 1){
        return 'El semestre límite debe estar en el rango 1 - 8 <br>';
    } else {
        return '';
    }
}