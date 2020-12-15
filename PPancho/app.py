from flask import Flask, render_template, request, redirect, url_for, abort
from modelo.models import db
from modelo.models import Alumno, Categoria, Equipo
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

'''Ruta dinamica
@app.route('/eliminarCategoria/<idCategoria>')
def eliminarCategoria(idCategoria):
    return 'Eliminando la categoria ' + idCategoria'''

#CRUD Alumnos
@app.route('/alumnos/new')
def nuevoAlumno():
    return render_template('Alumnos/altaAlumno.html')
@app.route('/alumnos/edit')
def editarAlumno():
    return render_template('Alumnos/editarAlumno.html')
@app.route('/alumnos/delete')
def eliminarAlumno():
    return render_template('Alumnos/eliminarAlumno.html')
@app.route('/alumnos')
def consultarAlumno():
    return render_template('Alumnos/consultaAlumnos.html')
@app.route('/alumnos/save', methods=['POST'])
def agregarAlumno():
    #try:
    a=Alumno()
    a.noControl=request.form['noControl']
    a.idUsuario=request.form['idUsuario']
    a.idCarrera=request.form['idCarrera']
    a.semestre=request.form['semestre']
    a.insertar()
        #return 'Edificio registrado con exito'
    #except:
        #return 'Error al registrar al alumno'

#Fin CRUD Alumnos

#CRUD Equipos
@app.route('/equipos/new')
def nuevoEquipo():
    return render_template('Equipos/creaciónEquipo.html')
@app.route('/equipos/edit')
def editarEquipo():
    return render_template('Equipos/editarEquipo.html')
@app.route('/equipos/delete')
def eliminarEquipo():
    return render_template('Equipos/eliminarEquipo.html')
@app.route('/equipos')
def consultarEquipo():
    return render_template('Equipos/consultaEquipos.html')
@app.route('/equipos/save', methods=['POST'])
def agregarEquipo():
    #try:
    e=Equipo()
    e.asesor=request.form['asesor']
    e.integrante1=request.form['integrante1']
    e.integrante2=request.form['integrante2']
    e.integrante3=request.form['integrante3']
    e.nombre=request.form['nombre']
    e.idCategoria=request.form['idCategoria']
    e.puntos=request.form['puntos']
    e.problemasResueltos=request.form['problemasResueltos']
    e.insertar()
    return 'guardado'
    #3except:
        #return 'error'

#Termina CRUD

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

@app.errorhandler(404)
def error_404(e):
    return render_template('Errores/error_404.html'), 404

@app.errorhandler(500)
def error_500(e):
    return render_template('Errores/error_500.html'), 500

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True)