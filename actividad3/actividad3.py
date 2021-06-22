from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_integrantes = [{'item_id': 1, 'matricula': 918762132, 'nombre': 'Juan', 'edad': 21, 'APaterno':'Cruz', 'AMaterno':'Vazquez', 'correo': 'juan123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 2, 'matricula': 918762318, 'nombre': 'Pedro', 'edad': 21, 'APaterno':'Demeza', 'AMaterno':'Rodriguez', 'correo': 'pedro123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 3, 'matricula': 918762321, 'nombre': 'Maria', 'edad': 20, 'APaterno':'Ruiz', 'AMaterno':'Najera', 'correo': 'maria123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 4, 'matricula': 918762322, 'nombre': 'Carla', 'edad': 20, 'APaterno':'Aguilar', 'AMaterno':'Perez', 'correo': 'carla123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 5, 'matricula': 91810534, 'nombre': 'Guillermo', 'edad': 20, 'APaterno':'Ramires', 'AMaterno':'Benitez', 'correo': 'guille23@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 6, 'matricula': 91876232, 'nombre': 'Eleazar', 'edad': 22, 'APaterno':'Moreno', 'AMaterno':'Diaz', 'correo': 'eli@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 7, 'matricula': 91876231, 'nombre': 'Alan', 'edad': 21, 'APaterno':'Gomez', 'AMaterno':'Sanchez', 'correo': 'alan123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 8, 'matricula': 91876277, 'nombre': 'DanielD', 'edad': 21, 'APaterno':'Morales', 'AMaterno':'Duran', 'correo': 'dany123@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 9, 'matricula': 91876233, 'nombre': 'Rodan', 'edad': 22, 'APaterno':'Gonzales', 'AMaterno':'Leon', 'correo': 'rodan33@mgail.com','telefono':'9191907766','carrera':'RIyC'},
                     {'item_id': 10, 'matricula': 91876299, 'nombre': 'Alberto', 'edad': 23, 'APaterno':'Dominguez', 'AMaterno':'Lopez', 'correo': 'alberto123@mgail.com','telefono':'9191907766','carrera':'RIyC'}]

@app.get("/integrante/")
async def leer_integrante (item_id: int):
    for diccionario in lista_integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
            <html>
            <head>
                <title>{diccionario.get('nombre')}</title>
            <head>
            <body>
                <h3>Sitio personal</h3>
                <ul>
                    <li>Matricula: {diccionario.get('nombre')}</li>
                    <li>Nombre: {diccionario.get('matricula')}</li>
                    <li>Edad: {diccionario.get('edad')}</li>
                    <li>Apellido Paterno: {diccionario.get('APaterno')}</li>
                    <li>Apellido Materno: {diccionario.get('AMaterno')}</li>
                    <li>Correo: {diccionario.get('correo')}</li>
                    <li>Teléfono: {diccionario.get('telefono')}</li>
                    <li>Carrera: {diccionario.get('carrera')}</li>
                </ul>
            </body>
            </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontró eñ registro"