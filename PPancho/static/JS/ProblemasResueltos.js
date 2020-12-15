function validar(form){
    var cad = validarPuntos(form.puntos.value);
    cad+= validarTiempo(form.tiempoMax.value);

    if (cad!='') {
        document.getElementById("notificaciones").innerHTML='<p>'+cad+'</p>';
        return false;
    } else {
        return true;
    }
}

function validarPuntos(puntos){
    if (puntos<0 || puntos>10) {
        return 'El rango de los puntos de 0 a 10 !!';
    } else {
        return '';
    }
}

function validarTiempo(tiempoMax){
    if (tiempoMax < 15 || tiempoMax > 30) {
        return 'El rango del tiempo estimado es de 15 a 30 minutos'
    } else {
        return ''
    }
}