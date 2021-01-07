from flask import Flask, render_template, request, redirect, url_for, abort
from modelo.models import db
from modelo.models import Categoria, Carrera, Alumno, Usuario, Docente, Equipo, Edicion, Problema, ProblemaResuelto, ProblemaAPublicar
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

#CRUD Problemas a publicar
@app.route('/problemasAPublicar/new')
def nuevoProblemaAPublicar():
    return render_template('ProblemasAPublicar/creacionProblemasAP.html')
@app.route('/problemasAPublicar/save', methods=['POST'])
def agregarProblemaAPublicar():
    try:
        ap=ProblemaAPublicar()
        ap.idProblemaAP=request.form['idProblemaAP']
        ap.idEdicion=request.form['idEdicion']
        ap.idCategoria=request.form['idCategoria']
        ap.colorGlobo=request.form['colorGlobo']
        ap.insertar()
        return redirect(url_for('consultarProblemaAPublicar'))
    except:
        abort(500)
@app.route('/problemasAPublicar')
def consultarProblemaAPublicar():
    ap=ProblemaAPublicar()
    problemasAPublicar=ap.consultaGeneral()
    return render_template('ProblemasAPublicar/consultaProblemasAP.html', problemasAPublicar=problemasAPublicar)
@app.route('/problemasAPublicar/edit/<int:id>')
def editarProblemaAPublicar(id):
    ap=ProblemaAPublicar()
    ap.idProblemaAP=id
    problemaAPublicar=ap.consultaIndividual()
    return render_template('ProblemasAPublicar/editarProblemasAP.html', problemaAPublicar=problemaAPublicar)
@app.route('/problemasAPublicar/modificar',methods=['POST'])
def modificarProblemasAPublicar():
    ap = ProblemaAPublicar()
    ap.idProblemaAP = request.form['idProblemaAP']
    ap.idEdicion = request.form['idEdicion']
    ap.idCategoria = request.form['idCategoria']
    ap.colorGlobo = request.form['colorGlobo']
    ap.actualizar()
    return redirect(url_for('consultarProblemaAPublicar'))
@app.route('/problemasAPublicar/delete/<int:id>')
def eliminarProblemaAPublicar(id):
    ap=ProblemaAPublicar()
    ap.idProblemaAP=id
    ap.eliminar()
    return redirect(url_for("consultarProblemaAPublicar"))
#Fin CRUD Problemas a publicar

#CRUD Problemas resueltos
@app.route('/problemasResueltos/new')
def nuevoProblemaResuelto():
    return render_template('ProblemasResueltos/creacionProblemasR.html')
@app.route('/problemasResueltos/save', methods=['POST'])
def agregarProblemaResuelto():
    try:
        r=ProblemaResuelto()
        r.idProblemaR=request.form['idProblemaR']
        r.idEquipo=request.form['idEquipo']
        r.tiempoEjecucion=request.form['tiempoEjecucion']
        r.puntos=request.form['puntos']
        r.insertar()
        return redirect(url_for('consultarProblemaResuelto'))
    except:
        abort(500)
@app.route('/problemasResueltos')
def consultarProblemaResuelto():
    r=ProblemaResuelto()
    problemasResueltos=r.consultaGeneral()
    return render_template('ProblemasResueltos/consultaProblemasR.html', problemasResueltos=problemasResueltos)
@app.route('/problemasResueltos/edit/<int:id>')
def editarProblemaResuelto(id):
    r=ProblemaResuelto()
    r.idProblemaR=id
    problemaResuelto=r.consultaIndividual()
    return render_template('ProblemasResueltos/editarProblemasR.html', problemaResuelto=problemaResuelto)
@app.route('/problemasResueltos/modificar',methods=['POST'])
def modificarProblemasResueltos():
    r = ProblemaResuelto()
    r.idProblemaR = request.form['idProblemaR']
    r.idEquipo = request.form['idEquipo']
    r.tiempoEjecucion = request.form['tiempoEjecucion']
    r.puntos = request.form['puntos']
    r.actualizar()
    return redirect(url_for('consultarProblemaResuelto'))
@app.route('/problemasResueltos/delete/<int:id>')
def eliminarProblemaResuelto(id):
    r=ProblemaResuelto()
    r.idProblemaR=id
    r.eliminar()
    return redirect(url_for("consultarProblemaResuelto"))
#Fin CRUD Problemas resueltos

#CRUD Problemas
@app.route('/problemas/new')
def nuevoProblema():
    return render_template('Problemas/registrarProblema.html')
@app.route('/problemas/save', methods=['POST'])
def agregarProblema():
    try:
        p=Problema()
        p.nombre=request.form['nombre']
        p.puntos=request.form['puntos']
        p.tiempoMax=request.form['tiempoMax']
        p.descripcion=request.form['descripcion']
        p.insertar()
        return redirect(url_for('consultarProblema'))
    except:
        abort(500)
@app.route('/problemas')
def consultarProblema():
    p=Problema()
    problemas=p.consultaGeneral()
    return render_template('Problemas/consultaProblemas.html', problemas=problemas)
@app.route('/problemas/edit/<int:id>')
def editarProblema(id):
    p=Problema()
    p.idProblema=id
    problema=p.consultaIndividual()
    return render_template('Problemas/editarProblemas.html', problema=problema)
@app.route('/problemas/modificar',methods=['POST'])
def modificarProblemas():
    p=Problema()
    p.idProblema=request.form['idProblema']
    p.nombre = request.form['nombre']
    p.puntos = request.form['puntos']
    p.tiempoMax = request.form['tiempoMax']
    p.descripcion = request.form['descripcion']
    p.actualizar()
    return redirect(url_for('consultarProblema'))
@app.route('/problemas/delete/<int:id>')
def eliminarProblema(id):
    p=Problema()
    p.idProblema=id
    p.eliminar()
    return redirect(url_for("consultarProblema"))
#Fin CRUD Problemas

#CRUD Ediciones
@app.route('/ediciones/new')
def nuevaEdicion():
    return render_template('Ediciones/RegistrarEdicions.html')
@app.route('/ediciones/save', methods=['POST'])
def agregarEdicion():
    try:
        e=Edicion()
        e.nombre=request.form['nombre']
        e.fechaRegistro=request.form['fechaRegistro']
        e.fechaEvento=request.form['fechaEvento']
        e.horaInicio=request.form['horaInicio']
        e.horaFin=request.form['horaFin']
        e.insertar()
        return redirect(url_for('consultarEdicion'))
    except:
        abort(500)
@app.route('/ediciones')
def consultarEdicion():
    e=Edicion()
    ediciones=e.consultaGeneral()
    return render_template('Ediciones/ConsultaEdiciones.html', ediciones=ediciones)
@app.route('/ediciones/edit/<int:id>')
def editarEdicion(id):
    e=Edicion()
    e.idEdicion=id
    edicion=e.consultaIndividual()
    return render_template('Ediciones/EditarEdiciones.html', edicion=edicion)
@app.route('/ediciones/modificar',methods=['POST'])
def modificarEdiciones():
    e = Edicion()
    e.idEdicion=request.form['idEdicion']
    e.nombre = request.form['nombre']
    e.fechaRegistro = request.form['fechaRegistro']
    e.fechaEvento = request.form['fechaEvento']
    e.horaInicio = request.form['horaInicio']
    e.horaFin = request.form['horaFin']
    e.actualizar()
    return redirect(url_for('consultarEdicion'))
@app.route('/ediciones/delete/<int:id>')
def eliminarEdicion(id):
    e=Edicion
    e.idEdicion=id
    e.eliminar()
    return redirect(url_for("consultarEdicion"))
#Fin CRUD Ediciones

#CRUD Equipos
@app.route('/equipos/new')
def nuevoEquipo():
    return render_template('Equipos/creaciónEquipo.html')
@app.route('/equipos/save', methods=['POST'])
def agregarEquipo():
    try:
        e = Equipo()
        e.asesor = request.form['asesor']
        e.integrante1 = request.form['integrante1']
        e.integrante2 = request.form['integrante2']
        e.integrante3 = request.form['integrante3']
        e.nombre = request.form['nombre']
        e.idCategoria = request.form['idCategoria']
        e.puntos = request.form['puntos']
        e.problemasResueltos = request.form['problemasResueltos']
        e.insertar()
        return redirect(url_for('consultarEquipo'))
    except:
        abort(500)
@app.route('/equipos')
def consultarEquipo():
    e=Equipo()
    equipos=e.consultaGeneral()
    return render_template('Equipos/consultaEquipos.html', equipos=equipos)
@app.route('/equipos/edit/<int:id>')
def editarEquipo(id):
    e=Equipo()
    e.idEquipo=id
    equipo=e.consultaIndividual()
    return render_template('Equipos/editarEquipo.html', equipo=equipo)
@app.route('/equipos/modificar',methods=['POST'])
def modificarEquipos():
    e=Equipo()
    e.idEquipo=request.form['idEquipo']
    e.asesor = request.form['asesor']
    e.integrante1 = request.form['integrante1']
    e.integrante2 = request.form['integrante2']
    e.integrante3 = request.form['integrante3']
    e.nombre = request.form['nombre']
    e.idCategoria = request.form['idCategoria']
    e.puntos = request.form['puntos']
    e.problemasResueltos = request.form['problemasResueltos']
    e.actualizar()
    return redirect(url_for('consultarEquipo'))
@app.route('/equipos/delete/<int:id>')
def eliminarEquipo(id):
    e=Equipo()
    e.idEquipo=id
    e.eliminar()
    return redirect(url_for("consultarEquipo"))
#Fin CRUD Equipos

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