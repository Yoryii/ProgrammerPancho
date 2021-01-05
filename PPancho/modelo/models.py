from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey, CHAR
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