from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey, CHAR, Date, Time
db=SQLAlchemy()

class Carrera(db.Model):
    __tablename__='Carreras'
    idCarrera=Column(Integer, primary_key=True)
    nombre=Column(String, unique=True)
    siglas=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        carrera=self.consultaIndividual()
        db.session.delete(carrera)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idCarrera)

class Usuario(db.Model):
    __tablename__='Usuarios'
    idUsuario=Column(Integer, primary_key=True)
    nombre=Column(String)
    sexo=Column(CHAR)
    telefono=Column(String)
    email=Column(String, unique=True)
    estatus=Column(String)
    tipo=Column(CHAR)
    contraseña=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usuario=self.consultaIndividual()
        db.session.delete(usuario)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idUsuario)

class Docente(db.Model):
    __tablename__='Docentes'
    idDocente=Column(Integer, primary_key=True)
    idUsuario=Column(Integer, ForeignKey('Usuarios.idUsuario'), unique=True)
    escolaridad=Column(String)
    especialidad=Column(String)
    cedula=Column(String, unique=True)
    idCarrera=Column(Integer, ForeignKey('Carreras.idCarrera'), unique=True)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        docente=self.consultaIndividual()
        db.session.delete(docente)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idDocente)

class Categoria(db.Model):
    __tablename__='Categorias'
    idCategoria=Column(Integer, primary_key=True)
    nombre=Column(String, unique=True)
    limiteSemestre=Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        categoria=self.consultaIndividual()
        db.session.delete(categoria)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idCategoria)

class Alumno(db.Model):
    __tablename__='Alumnos'
    noControl=Column(Integer, primary_key=True)
    idUsuario=Column(Integer, ForeignKey('Usuarios.idUsuario'), unique=True)
    idCarrera=Column(Integer, ForeignKey('Carreras.idCarrera'), unique=True)
    semestre=Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        alumno=self.consultaIndividual()
        db.session.delete(alumno)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.noControl)

class Equipo(db.Model):
    __tablename__='Equipos'
    idEquipo=Column(Integer, primary_key=True)
    asesor=Column(Integer, ForeignKey('Docentes.idDocente'), unique=True)
    integrante1=Column(Integer, ForeignKey('Alumnos.noControl'), unique=True)
    integrante2 = Column(Integer, ForeignKey('Alumnos.noControl'), unique=True)
    integrante3 = Column(Integer, ForeignKey('Alumnos.noControl'), unique=True)
    nombre=Column(String, unique=True)
    idCategoria=Column(Integer, ForeignKey('Categorias.idCategoria'), unique=True)
    puntos=Column(Integer)
    problemasResueltos=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        equipo=self.consultaIndividual()
        db.session.delete(equipo)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idEquipo)

class Edicion(db.Model):
    __tablename__='Ediciones'
    idEdicion=Column(Integer, primary_key=True)
    nombre=Column(String, unique=True)
    fechaRegistro=Column(Date)
    fechaEvento=Column(Date)
    horaInicio=Column(Time)
    horaFin=Column(Time)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        edicion=self.consultaIndividual()
        db.session.delete(edicion)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idEdicion)

class Problema(db.Model):
    __tablename__='Problemas'
    idProblema=Column(Integer, primary_key=True)
    nombre=Column(String, unique=True)
    puntos=Column(Integer)
    tiempoMax=Column(String)
    descripcion=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        problema=self.consultaIndividual()
        db.session.delete(problema)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idProblema)

class ProblemaResuelto(db.Model):
    __tablename__='ProblemasResueltos'
    idProblemaR=Column(Integer, primary_key=True)
    idEquipo = Column(Integer, ForeignKey('Equipos.idEquipo'))
    tiempoEjecucion=Column(String)
    puntos=Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        problemaResuelto=self.consultaIndividual()
        db.session.delete(problemaResuelto)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idProblemaR)

class ProblemaAPublicar(db.Model):
    __tablename__='ProblemasAPublicar'
    idProblemaAP=Column(Integer, primary_key=True)
    idEdicion=Column(Integer, ForeignKey('Ediciones.idEdicion'))
    idCategoria=Column(Integer, ForeignKey('Categorias.idCategoria'))
    colorGlobo=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        problemaAPublicar=self.consultaIndividual()
        db.session.delete(problemaAPublicar)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idProblemaAP)