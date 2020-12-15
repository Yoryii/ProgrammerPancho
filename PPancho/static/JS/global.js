function eliminarCategoria(id,nombre){
    if(confirm('¿Estás seguro de eliminar la categoría '+nombre+'?'))
        location.href='/categorias/delete/'+id;
}