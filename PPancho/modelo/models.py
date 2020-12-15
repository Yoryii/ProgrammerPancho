from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, ForeignKey
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

class Alumno(db.Model):
    __tablename__='Alumnos'
    noControl=Column(Integer, primary_key=True)
    idUsuario=Column(Integer, unique=True)
    idCarrera=Column(Integer, unique=True)
    semestre=Column(Integer)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        alumno = self.consultaIndividual()
        db.session.delete(alumno)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.noControl)

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

class Equipo(db.Model):
    __tablename__='Equipos'
    idEquipo=Column(Integer, primary_key=True)
    asesor=Column(Integer, unique=True)
    integrante1=Column(Integer, unique=True)
    integrante2=Column(Integer, unique=True)
    integrante3=Column(Integer, unique=True)
    nombre=Column(String, unique=True)
    idCategoria=Column(Integer, ForeignKey(Categoria.idCategoria))
    puntos=Column(Integer)
    problemasResueltos=Column(String)
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        equipo = self.consultaIndividual()
        db.session.delete(equipo)
        db.session.commit()
    def consultaGeneral(self):
        return self.query.all()
    def consultaIndividual(self):
        return self.query.get(self.idEquipo)

