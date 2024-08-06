import sqlite3

# Conectar a la base de datos
con = sqlite3.connect('restaurante.db')
cur = con.cursor()

# Insertar datos en la tabla Persona
cur.execute("""
INSERT INTO Persona (cedula, nombre, apellidos, correo, telefono)
VALUES ('1234567890', 'Juan', 'Pérez', 'juan.perez@example.com', '555-1234');
""")

# Insertar datos en la tabla Platillo
cur.execute("""
INSERT INTO Platillo (identificador, nombre, precioxUnidad)
VALUES ('P001', 'Tacos', 12.5);
""")

# Confirmar los cambios y cerrar la conexión
con.commit()
con.close()
