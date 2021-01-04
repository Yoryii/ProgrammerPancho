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