import sqlite3
from pydantic import BaseModel
class Factura_Platillos(BaseModel):
    identificadorFactura:str
    identificadorPlatillo:str
    def nueva(self, identificadorFactura,identificadorPlatillo):
        self.identificadorFactura = identificadorFactura
        self.identificadorPlatillo= identificadorPlatillo

     
    def guardaenBD(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        sql = f'''INSERT INTO Factura_Platillos(identificadorFactura,identificadorPlatillo) VALUES (
        '{self.identificadorFactura}', 
        '{self.identificadorPlatillo}'
        )'''
        cur.execute(sql)
        con.commit()
        con.close()
    def seleccionatodoenBDxFactura(self):
        con = sqlite3.connect('restaurante.db')
        cur = con.cursor()
        listaDevolver=[]
        for fila in cur.execute(f'SELECT * FROM Factura_Platillos where identificadorFactura= {self.identificadorFactura}'):
            objetoInterno =  Factura_Platillos( identificadorFactura = fila[0],identificadorPlatillo= fila[1])
            listaDevolver.append(objetoInterno)
        return listaDevolver