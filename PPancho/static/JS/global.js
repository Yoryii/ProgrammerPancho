function eliminarCategoria(id,nombre){
    if(confirm('¿Estás seguro de eliminar la categoría '+nombre+'?'))
        location.href='/categorias/delete/'+id;
}

function eliminarCarrera(id,nombre){
    if(confirm('¿Estás seguro de eliminar la carrera '+nombre+'?'))
        location.href='/carreras/delete/'+id;
}

function eliminarAlumno(id){
    if(confirm('¿Estás seguro de eliminar el alumno ?'))
        location.href='/alumnos/delete/'+id;
}

function eliminarUsuario(id,nombre){
    if(confirm('¿Estás seguro de eliminar el usuario '+nombre+'?'))
        location.href='/usuarios/delete/'+id;
}

function eliminarDocente(id){
    if(confirm('¿Estás seguro de eliminar al docente?'))
        location.href='/docentes/delete/'+id;
}

function eliminarEquipo(id,nombre){
    if(confirm('¿Estás seguro de eliminar el equipo '+nombre+'?'))
        location.href='/equipos/delete/'+id;
}