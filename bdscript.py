import sqlite3
con = sqlite3.connect('restaurante.db')
cur = con.cursor()

def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS Persona (
     cedula TEXT PRIMARY KEY,
     nombre TEXT,
     apellidos TEXT,
     correo TEXT,
     telefono TEXT
     );""")
    con.commit()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Reservacion (
     mesa TEXT,
     hora REAL,
     reservadoPor TEXT,
     CONSTRAINT fk_reservacion_persona FOREIGN KEY (reservadoPor)
     REFERENCES Persona (cedula)
     );""")
    con.commit()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Platillo (
     identificador TEXT PRIMARY KEY,
     nombre TEXT,
     precioxUnidad REAL
     );""")
    con.commit()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Factura (
     identificador TEXT PRIMARY KEY,
     fecha TEXT,
     montoTotal REAL,
     cantidadHoras REAL,
     reservacionAtendida TEXT,
     clienteFactura TEXT,
     CONSTRAINT fk_factura_reservacion FOREIGN KEY (reservacionAtendida)
     REFERENCES Reservacion (mesa),
     CONSTRAINT fk_factura_persona FOREIGN KEY (clienteFactura)
     REFERENCES Persona (cedula)
                
     );""")
    con.commit()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Factura_Platillos (
     identificadorFactura TEXT ,
     identificadorPlatillo TEXT,
     CONSTRAINT fk_factura_Factura_Platillos FOREIGN KEY (identificadorFactura)
     REFERENCES Factura (identificador)
     CONSTRAINT fk_Platillos_Factura_Platillos FOREIGN KEY (identificadorPlatillo)
     REFERENCES Platillo (identificador)
     );""")
    con.commit()
    
    con.close()