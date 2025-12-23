# server.py
# Autora: Aleyda Quispe

from wsgiref.simple_server import make_server
from urllib.parse import unquote
import os

BASE_DIR = os.path.dirname(__file__)

def app(environ, start_response):
    metodo = environ["REQUEST_METHOD"]
    path = unquote(environ["PATH_INFO"])

    # MANEJO DE GET
    if metodo == "GET":

        # Ruta raíz
        if path == "/":
            path = "/index.html"

        archivo = os.path.join(BASE_DIR, path.lstrip("/"))

        if os.path.isfile(archivo):
            # Detectar tipo de archivo
            if archivo.endswith(".html"):
                content_type = "text/html; charset=utf-8"
            elif archivo.endswith(".css"):
                content_type = "text/css; charset=utf-8"
            elif archivo.endswith(".jpeg") or archivo.endswith(".jpg"):
                content_type = "image/jpeg"
            elif archivo.endswith(".png"):
                content_type = "image/png"
            elif archivo.endswith(".js"):
                content_type = "application/javascript; charset=utf-8"
            else:
                content_type = "application/octet-stream"

            with open(archivo, "rb") as f:
                contenido = f.read()

            start_response("200 OK", [("Content-Type", content_type)])
            return [contenido]

        # Archivo no encontrado
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Archivo no encontrado"]
    
    # MANEJO DE POST (SIMULADO)
    if metodo == "POST":
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
        return [b"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Formulario enviado</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Formulario enviado correctamente</h2>
            <p>Esta es una simulaci&oacute;n del proyecto KIT SHINE.</p>
            <a href="/index.html">Volver al inicio</a>
        </body>
        </html>
        """]
    # MÉTODO NO SOPORTADO
    start_response("405 Method Not Allowed", [("Content-Type", "text/plain")])
    return [b"Metodo no permitido"]


# ARRANQUE DEL SERVIDOR
server = make_server("localhost", 8000, app)
print("Servidor activo en http://localhost:8000")
server.serve_forever()