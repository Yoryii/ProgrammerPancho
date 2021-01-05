from flask import Flask, render_template, request, redirect, url_for, abort
from modelo.models import db
from modelo.models import Categoria, Carrera, Alumno, Usuario, Docente
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#db=SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://programmerpancho_user:hola.123@localhost/ProgrammerPancho'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#Rutas de acceso al sistema
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/login')
def login():
    usuario = 'Yoryii'
    return render_template('principal.html', user = usuario)

#Fin de rutas de acceso al sistema

@app.route('/principal')
def principal():
    return render_template('principal.html')

#CRUD Categorias
@app.route('/categorias/new')
def nuevaCategoria():
    return render_template('Categorias/creaciónCategoria.html')
@app.route('/categorias/save', methods=['POST'])
def agregarCategoria():
    try:
        c=Categoria()
        c.nombre=request.form['nombre']
        c.limiteSemestre=request.form['limiteSemestre']
        c.insertar()
        return redirect(url_for('consultarCategoria'))
    except:
        abort(500)
@app.route('/categorias')
def consultarCategoria():
    c=Categoria()
    categorias=c.consultaGeneral()
    return render_template('Categorias/consultaCategorias.html', categorias=categorias)
@app.route('/categorias/edit/<int:id>')
def editarCategoria(id):
    c=Categoria()
    c.idCategoria=id
    categoria=c.consultaIndividual()
    return render_template('Categorias/editarCategoria.html', categoria=categoria)
@app.route('/categorias/modificar',methods=['POST'])
def modificarCategorias():
    c = Categoria()
    c.idCategoria=request.form['idCategoria']
    c.nombre = request.form['nombre']
    c.limiteSemestre = request.form['limiteSemestre']
    c.actualizar()
    return redirect(url_for('consultarCategoria'))
@app.route('/categorias/delete/<int:id>')
def eliminarCategoria(id):
    c=Categoria()
    c.idCategoria=id
    c.eliminar()
    return redirect(url_for("consultarCategoria"))
#Fin CRUD Categorias

#CRUD Docentes
@app.route('/docentes/new')
def nuevoDocente():
    return render_template('Docentes/altaDocentes.html')
@app.route('/docentes/save', methods=['POST'])
def agregarDocente():
    try:
        d=Docente()
        d.idUsuario=request.form['idUsuario']
        d.escolaridad=request.form['escolaridad']
        d.especialidad=request.form['especialidad']
        d.cedula=request.form['cedula']
        d.idCarrera=request.form['idCarrera']
        d.insertar()
        return redirect(url_for('consultarDocente'))
    except:
        abort(500)
@app.route('/docentes')
def consultarDocente():
    d=Docente()
    docentes=d.consultaGeneral()
    return render_template('Docentes/consultaDocentes.html', docentes=docentes)
@app.route('/docentes/edit/<int:id>')
def editarDocente(id):
    d=Docente()
    d.idDocente=id
    docente=d.consultaIndividual()
    return render_template('Docentes/editarDocentes.html', docente=docente)
@app.route('/docentes/modificar',methods=['POST'])
def modificarDocentes():
    d=Docente()
    d.idDocente=request.form['idDocente']
    d.idUsuario = request.form['idUsuario']
    d.escolaridad = request.form['escolaridad']
    d.especialidad = request.form['especialidad']
    d.cedula = request.form['cedula']
    d.idCarrera = request.form['idCarrera']
    d.actualizar()
    return redirect(url_for('consultarDocente'))
@app.route('/docentes/delete/<int:id>')
def eliminarDocente(id):
    d=Docente()
    d.idDocente=id
    d.eliminar()
    return redirect(url_for("consultarDocente"))
#Fin CRUD Docentes

#CRUD Usuarios
@app.route('/usuarios/new')
def nuevoUsuario():
    return render_template('Usuarios/altaUsuarios.html')
@app.route('/usuarios/save', methods=['POST'])
def agregarUsuario():
    try:
        u=Usuario()
        u.nombre=request.form['nombre']
        u.sexo=request.form['sexo']
        u.telefono=request.form['telefono']
        u.email=request.form['email']
        u.estatus=request.form['estatus']
        u.tipo=request.form['tipo']
        u.contraseña=request.form['contraseña']
        u.insertar()
        return redirect(url_for('consultarUsuario'))
    except:
        abort(500)
@app.route('/usuarios')
def consultarUsuario():
    u=Usuario()
    usuarios=u.consultaGeneral()
    return render_template('Usuarios/consultaUsuarios.html', usuarios=usuarios)
@app.route('/usuarios/edit/<int:id>')
def editarUsuario(id):
    u=Usuario()
    u.idUsuario=id
    usuario=u.consultaIndividual()
    return render_template('Usuarios/editarUsuarios.html', usuario=usuario)
@app.route('/usuarios/modificar',methods=['POST'])
def modificarUsuarios():
    u=Usuario()
    u.idUsuario=request.form['idUsuario']
    u.nombre = request.form['nombre']
    u.sexo = request.form['sexo']
    u.telefono=request.form['telefono']
    u.email = request.form['email']
    u.estatus = request.form['estatus']
    u.tipo = request.form['tipo']
    u.contraseña = request.form['contraseña']
    u.actualizar()
    return redirect(url_for('consultarUsuario'))
@app.route('/usuarios/delete/<int:id>')
def eliminarUsuario(id):
    u=Usuario()
    u.idUsuario=id
    u.eliminar()
    return redirect(url_for("consultarUsuario"))
#Fin CRUD Usuarios

#CRUD Alumnos
@app.route('/alumnos/new')
def nuevoAlumno():
    return render_template('Alumnos/altaAlumno.html')
@app.route('/alumnos/save', methods=['POST'])
def agregarAlumno():
    try:
        a=Alumno()
        a.noControl=request.form['noControl']
        a.idUsuario=request.form['idUsuario']
        a.idCarrera=request.form['idCarrera']
        a.semestre=request.form['semestre']
        a.insertar()
        return redirect(url_for('consultarAlumno'))
    except:
        abort(500)
@app.route('/alumnos')
def consultarAlumno():
    a=Alumno()
    alumnos=a.consultaGeneral()
    return render_template('Alumnos/consultaAlumnos.html', alumnos=alumnos)
@app.route('/alumnos/edit/<int:id>')
def editarAlumno(id):
    a=Alumno()
    a.noControl=id
    alumno=a.consultaIndividual()
    return render_template('Alumnos/editarAlumno.html', alumno=alumno)
@app.route('/alumnos/modificar',methods=['POST'])
def modificarAlumnos():
    a=Alumno()
    a.noControl = request.form['noControl']
    a.idUsuario = request.form['idUsuario']
    a.idCarrera = request.form['idCarrera']
    a.semestre = request.form['semestre']
    a.actualizar()
    return redirect(url_for('consultarAlumno'))
@app.route('/alumnos/delete/<int:id>')
def eliminarAlumno(id):
    a=Alumno()
    a.noControl=id
    a.eliminar()
    return redirect(url_for("consultarAlumno"))
#Fin CRUD Alumnos

#CRUD Carreras
@app.route('/carreras/new')
def nuevaCarrera():
    return render_template('Carreras/altaCarreras.html')
@app.route('/carreras/save', methods=['POST'])
def agregarCarrera():
    try:
        c=Carrera()
        c.nombre=request.form['nombre']
        c.siglas=request.form['siglas']
        c.insertar()
        return redirect(url_for('consultarCarrera'))
    except:
        abort(500)
@app.route('/carreras')
def consultarCarrera():
    c=Carrera()
    carreras=c.consultaGeneral()
    return render_template('Carreras/consultaCarreras.html', carreras=carreras)
@app.route('/carreras/edit/<int:id>')
def editarCarrera(id):
    c=Carrera()
    c.idCarrera=id
    carrera=c.consultaIndividual()
    return render_template('Carreras/editarCarreras.html', carrera=carrera)
@app.route('/carreras/modificar',methods=['POST'])
def modificarCarrera():
    c = Carrera()
    c.idCarrera=request.form['idCarrera']
    c.nombre = request.form['nombre']
    c.siglas = request.form['siglas']
    c.actualizar()
    return redirect(url_for('consultarCarrera'))
@app.route('/carreras/delete/<int:id>')
def eliminarCarrera(id):
    c=Carrera()
    c.idCarrera=id
    c.eliminar()
    return redirect(url_for("consultarCarrera"))
#Fin CRUD Carreras

#Cambio de páginas de error
@app.errorhandler(404)
def error_404(e):
    return render_template('Errores/error_404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('Errores/error_500.html'), 500

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)