from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
import persona
import platillo
import factura
import facturaPlatillo
import bdscript

# Crear una instancia de FastAPI
app = FastAPI()

# Crear las tablas en la base de datos
bdscript.create_tables()

# Ruta raíz que devuelve el archivo HTML principal
@app.get("/")
async def root():
    return FileResponse('index.html')

# Ruta para devolver una imagen específica (sideFoto.jpg)
@app.get("/sidePic")
async def root():
    return FileResponse("Fotos/sideFoto.jpg")

# Ruta para devolver otra imagen específica (sideFoto2.jpg)
@app.get("/sidePic2")
async def root():
    return FileResponse("Fotos/sideFoto2.jpg")

# Ruta para devolver una imagen de fondo (fondo2.jpg)
@app.get("/fondo2")
async def root():
    return FileResponse("Fotos/fondo2.jpg")

# Ruta para devolver una imagen de pasta (fotoPasta1.png)
@app.get("/foto1")
async def root():
    return FileResponse("Fotos/fotoPasta1.png")

# Ruta para devolver una imagen de Facebook (facebook.png)
@app.get("/facebook")
async def root():
    return FileResponse("Fotos/facebook.png")

# Ruta para devolver una imagen de Instagram (instagram.png)
@app.get("/instagram")
async def root():
    return FileResponse("Fotos/instagram.png")

# Ruta para devolver una imagen de TikTok (tik-tok.png)
@app.get("/tik-tok")
async def root():
    return FileResponse("Fotos/tik-tok.png")

# Ruta para modificar (crear) una persona en la base de datos
@app.put("/persona")
async def root(item: persona.Persona):
    objetoPersona = persona.Persona(cedula=item.cedula, nombre=item.nombre, apellidos=item.apellidos,
                                    correo=item.correo, telefono=item.telefono)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta para obtener todas las personas de la base de datos
@app.get("/persona")
async def root():
    objetoPersona = persona.Persona(cedula='', nombre='', apellidos='',
                                    correo='', telefono='')
    return objetoPersona.seleccionatodoenBD()

# Ruta para eliminar una persona de la base de datos
@app.delete("/persona")
async def root(item: persona.Persona):
    print(item)
    objetoPersona = persona.Persona(cedula=item.cedula, nombre='', apellidos='',
                                    correo='', telefono='')
    objetoPersona.eliminaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta para actualizar una persona en la base de datos
@app.post("/persona")
async def root(item: persona.Persona):
    print(item)
    objetoPersona = persona.Persona(cedula=item.cedula, nombre=item.nombre, apellidos=item.apellidos,
                                    correo=item.correo, telefono=item.telefono)
    objetoPersona.actualizaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta que devuelve un archivo HTML para la vista de personas
@app.get("/personaHTML")
async def root():
    return FileResponse("persona.html")

# Ruta para modificar (crear) un platillo en la base de datos
@app.put("/platillo")
async def root(item: platillo.Platillo):
    objetoPersona = platillo.Platillo(identificador=item.identificador, 
                                    nombre=item.nombre, precioxUnidad=item.precioxUnidad)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta para obtener todos los platillos de la base de datos
@app.get("/platillo")
async def root():
    objetoPersona = platillo.Platillo(identificador='', nombre='', precioxUnidad=0)
    return objetoPersona.seleccionatodoenBD()

# Ruta para eliminar un platillo de la base de datos
@app.delete("/platillo")
async def root(item: platillo.Platillo):
    print(item)
    objetoPersona = platillo.Platillo(identificador=item.identificador, nombre='', precioxUnidad=0)
    objetoPersona.eliminaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta para actualizar un platillo en la base de datos
@app.post("/platillo")
async def root(item: platillo.Platillo):
    print(item)
    objetoPersona = platillo.Platillo(identificador=item.identificador, nombre=item.nombre, precioxUnidad=item.precioxUnidad)
    objetoPersona.actualizaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta que devuelve un archivo HTML para la vista de platillos
@app.get("/platilloHTML")
async def root():
    return FileResponse("platillo.html")

# Ruta para modificar (crear) una factura en la base de datos
@app.put("/factura")
async def root(item: factura.Factura):
    objetoPersona = factura.Factura(identificador=item.identificador, fecha=item.fecha, montoTotal=item.montoTotal,
                                    cantidadHoras=item.cantidadHoras, clienteFactura=item.clienteFactura)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBD()

# Ruta para obtener todas las facturas de la base de datos
@app.get("/factura")
async def root():
    objetoPersona = factura.Factura(identificador='', fecha='', montoTotal=0, cantidadHoras=0, clienteFactura='')
    return objetoPersona.seleccionatodoenBD()

# Ruta para modificar (crear) una relación entre factura y platillo en la base de datos
@app.put("/facturaPlatillo")
async def root(item: facturaPlatillo.Factura_Platillos):
    objetoPersona = facturaPlatillo.Factura_Platillos(identificadorFactura=item.identificadorFactura,
                                                     identificadorPlatillo=item.identificadorPlatillo)
    objetoPersona.guardaenBD()
    return objetoPersona.seleccionatodoenBDxFactura()

# Ruta para obtener la relación entre factura y platillo por identificador de factura
@app.get("/facturaplatilloxfactura")
async def root(item: facturaPlatillo.Factura_Platillos):
    objetoPersona = facturaPlatillo.Factura_Platillos(identificadorFactura=item.identificadorFactura, identificadorPlatillo='')
    return objetoPersona.seleccionatodoenBDxFactura()

# Ruta que devuelve un archivo HTML para la vista de facturas
@app.get("/facturaHTML")
async def root():
    return FileResponse("factura.html")
