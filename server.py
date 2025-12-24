# server.py
# Autora: Aleyda Quispe

from wsgiref.simple_server import make_server
from urllib.parse import unquote
import mysql.connector
import os

BASE_DIR = os.path.dirname(__file__)

# CONEXIÓN A MYSQL (WAMP)
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",   
        database="kit_shine"
    )

def app(environ, start_response):
    metodo = environ["REQUEST_METHOD"]
    path = unquote(environ["PATH_INFO"])

    # GET 
    if metodo == "GET":

        if path == "/":
            path = "/index.html"

        archivo = os.path.join(BASE_DIR, path.lstrip("/"))

        if os.path.isfile(archivo):
            if archivo.endswith(".html"):
                content_type = "text/html; charset=utf-8"
            elif archivo.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif archivo.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            elif archivo.endswith(".png"):
                content_type = "image/png"
            elif archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
                content_type = "image/jpeg"
            else:
                content_type = "application/octet-stream"

            with open(archivo, "rb") as f:
                contenido = f.read()

            start_response("200 OK", [("Content-Type", content_type)])
            return [contenido]

        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Archivo no encontrado"]

    #  POST 
    if metodo == "POST":
        try:
            size = int(environ.get("CONTENT_LENGTH", 0))
        except:
            size = 0

        datos = environ["wsgi.input"].read(size).decode()
        params = dict(x.split("=") for x in datos.split("&"))

        conn = conectar_bd()
        cursor = conn.cursor()

        # PEDIDOS
        if path == "/pedidos":
            sql = """
            INSERT INTO pedidos
            (nombre, apellido, dni, direccion, correo, producto, pago, comentarios)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
            valores = (
                params.get("nombre"),
                params.get("apellido"),
                params.get("dni"),
                params.get("direccion"),
                params.get("correo"),
                params.get("producto"),
                params.get("pago"),
                params.get("comentarios")
            )
            cursor.execute(sql, valores)

        # OPINIONES
        elif path == "/opiniones":
            sql = """
            INSERT INTO opiniones
            (nombre, apellido, correo, calificacion, comentario)
            VALUES (%s,%s,%s,%s,%s)
            """
            valores = (
                params.get("nombre"),
                params.get("apellido"),
                params.get("correo"),
                params.get("calificacion"),
                params.get("comentario")
            )
            cursor.execute(sql, valores)

        # CONTACTO
        elif path == "/contacto":
            sql = """
            INSERT INTO contactos
            (nombre, apellido, correo, tema, mensaje)
            VALUES (%s,%s,%s,%s,%s)
            """
            valores = (
                params.get("nombre"),
                params.get("apellido"),
                params.get("correo"),
                params.get("tema"),
                params.get("mensaje")
            )
            cursor.execute(sql, valores)

        conn.commit()
        cursor.close()
        conn.close()

        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
        return [b"""
        <h2 style='text-align:center;margin-top:50px'>
        Datos guardados correctamente en MySQL
        </h2>
        <p style='text-align:center'><a href='/index.html'>Volver</a></p>
        """]

    start_response("405 Method Not Allowed", [("Content-Type", "text/plain")])
    return [b"Metodo no permitido"]

# SERVIDOR
server = make_server("localhost", 8000, app)
print("Servidor activo en http://localhost:8000")
server.serve_forever()