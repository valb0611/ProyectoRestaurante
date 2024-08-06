import sqlite3
from pydantic import BaseModel

# Definir la clase Platillo que hereda de BaseModel
class Platillo(BaseModel):
    # Definir los atributos de la clase
    identificador: str
    nombre: str
    precioxUnidad: int
    
    # Método para inicializar un nuevo objeto Platillo
    def nueva(self, identificador, nombre, precioxUnidad):
        self.identificador = identificador
        self.nombre = nombre
        self.precioxUnidad = precioxUnidad
     
    # Método para guardar el objeto Platillo en la base de datos
    def guardaenBD(self):
        # Conectar a la base de datos SQLite
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        
        # Crear la instrucción SQL para insertar un nuevo platillo
        sql = f'''INSERT INTO Platillo(identificador, nombre, precioxUnidad) VALUES (
        '{self.identificador}', 
        '{self.nombre}',
        {self.precioxUnidad})'''
        
        # Ejecutar la instrucción SQL
        cur.execute(sql)
        
        # Confirmar los cambios y cerrar la conexión
        con.commit()
        con.close()
    
    # Método para eliminar el objeto Platillo de la base de datos
    def eliminaenBD(self):
        # Conectar a la base de datos SQLite
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        
        # Crear la instrucción SQL para eliminar un platillo por identificador
        sql = f'''DELETE FROM Platillo WHERE identificador = '{self.identificador}'''
        
        # Ejecutar la instrucción SQL
        cur.execute(sql)
        
        # Confirmar los cambios y cerrar la conexión
        con.commit()
        con.close()
    
    # Método para actualizar un objeto Platillo en la base de datos
    def actualizaenBD(self):
        # Conectar a la base de datos SQLite
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        
        # Crear la instrucción SQL para actualizar un platillo por identificador
        sql = f'''UPDATE Platillo SET nombre = '{self.nombre}', precioxUnidad = {self.precioxUnidad} WHERE identificador = '{self.identificador}'''
        
        # Ejecutar la instrucción SQL
        cur.execute(sql)
        
        # Confirmar los cambios y cerrar la conexión
        con.commit()
        con.close()
    
    # Método para seleccionar todos los platillos de la base de datos
    def seleccionatodoenBD(self):
        # Conectar a la base de datos SQLite
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        
        # Crear una lista para almacenar los objetos Platillo
        listaDevolver = []
        
        # Ejecutar la instrucción SQL para seleccionar todos los platillos
        for fila in cur.execute('SELECT * FROM Platillo'):
            # Crear un nuevo objeto Platillo para cada fila
            objetoInterno = Platillo(identificador=fila[0], 
                                    nombre=fila[1],
                                    precioxUnidad=fila[2])
            # Añadir el objeto Platillo a la lista
            listaDevolver.append(objetoInterno)
        
        # Cerrar la conexión
        con.close()
        
        # Devolver la lista de objetos Platillo
        return listaDevolver
