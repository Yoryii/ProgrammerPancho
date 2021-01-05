function validar(form){
	var cad=validaridUsuario(form.idUsuario.value);
	cad+=validarTelefono(form.telefono.value);

	if(cad!=''){
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    }
    else{
       return true; 
    }
}

function validarTelefono(cad){
	var ban=false;
	if (cad.length==12){
		var pat=/\d{3}-\d{3}-\d{4}/;
		if(pat.test(cad)){
			return '';
		}
		else{
			return 'El n�mero no cumple ###-###-#### <br>';
		}
	}
	else{
		return 'El n�mero debe tener 12 caracteres. <br>';
	}
}



