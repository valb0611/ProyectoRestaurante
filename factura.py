#ver platillo.py para ver los comentarios de las funcioens
import sqlite3
import facturaPlatillo
from pydantic import BaseModel
class Factura(BaseModel):
    identificador:str
    fecha:str
    montoTotal:float
    cantidadHoras:int
    
    clienteFactura: str



    def nueva(self, identificador,fecha,montoTotal,cantidadHoras,clienteFactura):
        self.identificador = identificador
        self.fecha= fecha
        self.montoTotal = montoTotal
        self.cantidadHoras= cantidadHoras
        self.clienteFactura = clienteFactura
  

    def guardaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura(identificador,fecha,montoTotal,cantidadHoras,clienteFactura) VALUES (
        '{self.identificador}', 
        '{self.fecha}',
        {self.montoTotal}, 
        {self.cantidadHoras},
        '{self.clienteFactura}'
        )'''
        cur.execute(sql)
        con.commit()
        con.close()
    def eliminaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''DELETE FROM Factura WHERE identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()
    def actualizaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''UPDATE Factura SET fecha= 
        {self.fecha} , montoTotal=
        {self.montoTotal}, cantidadHoras=
        {self.cantidadHoras}, clienteFactura= {self.clienteFactura}  where identificador = {self.identificador}'''
        cur.execute(sql)
        con.commit()
        con.close()

    def seleccionatodoenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute('SELECT * FROM Factura'):
            objetoInterno = Factura( identificador = fila[0],fecha= fila[1],montoTotal = fila[2],
            cantidadHoras= fila[3], clienteFactura= fila[5])
            objetoFacturaPlatillos = facturaPlatillo.Factura_Platillos(identificadorFactura=objetoInterno.identificador,identificadorPlatillo='')
            #objetoInterno.listaderepuestos = objetoFacturaPlatillos.seleccionatodoenBDxFactura()
            listaDevolver.append(objetoInterno)
        return listaDevolver
   