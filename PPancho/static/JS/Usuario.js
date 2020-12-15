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



function validaridUsuario(cad){
	var patron=/\d{8}/;
	if (patron.test(cad)){
		return '';
	}
	else{
		return "El id debe tener 8 dígitos <br>";
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
			return 'El número no cumple ###-###-#### <br>';
		}
	}
	else{
		return 'El número debe tener 12 caracteres. <br>';
	}
}



