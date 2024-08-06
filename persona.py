#ver platillo.py para ver los comentarios de las funcioens
import sqlite3
from pydantic import BaseModel
class Persona(BaseModel):
    cedula : str
    nombre : str
    apellidos : str
    correo : str
    telefono : str
    def nueva(self, cedula, nombre, apellidos, correo,telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo= correo
        self.telefono= telefono
    def guardaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Persona(cedula,nombre,apellidos,correo,telefono) VALUES (
        '{self.cedula}', 
        '{self.nombre}', 
        '{self.apellidos}', 
        '{self.correo}' ,
        '{self.telefono}')'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Persona WHERE cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''UPDATE Persona SET nombre= 
        '{self.nombre}' , apellidos=
        '{self.apellidos}' , correo =
        '{self.correo}' , telefono =
        '{self.telefono}' where cedula = {self.cedula}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM persona'):
            objetoInterno = Persona(cedula= fila[0], apellidos = fila[2],
                                    correo= fila[3],
                                    nombre= fila[1],
                                    telefono = fila[4])
            listaDevolver.append(objetoInterno)
        return listaDevolver

        