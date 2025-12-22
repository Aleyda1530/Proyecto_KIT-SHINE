# server.py
# Autora: Aleyda Quispe

from wsgiref.simple_server import make_server
from urllib.parse import unquote
import os

BASE_DIR = os.path.dirname(__file__)

def app(environ, start_response):
    metodo = environ["REQUEST_METHOD"]
    path = unquote(environ["PATH_INFO"])

    # Ruta raíz
    if metodo == "GET" and path == "/":
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
        else:
            content_type = "application/octet-stream"

        with open(archivo, "rb") as f:
            contenido = f.read()

        start_response("200 OK", [("Content-Type", content_type)])
        return [contenido]

    # Si no existe
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Archivo no encontrado"]


server = make_server("localhost", 8000, app)
print("Servidor activo en http://localhost:8000")
server.serve_forever()
