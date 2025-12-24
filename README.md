# KIT SHINE – Glamour Portátil ✨

Proyecto individual del curso de **Desarrollo Web**, desarrollado a lo largo del semestre.  
La aplicación **KIT SHINE** simula una tienda virtual de accesorios de belleza que integran maquillaje en miniatura, permitiendo a las usuarias explorar productos, realizar pedidos, gestionar un carrito de compras y registrar opiniones.


## Descripción general

KIT SHINE es una aplicación web que integra tecnologías del frontend y backend para simular un proceso real de compra en línea. El sistema incluye validaciones de formularios, persistencia temporal de datos mediante `localStorage`, almacenamiento de información en una base de datos MySQL y un servidor HTTP desarrollado en Python.



## Tecnologías utilizadas

- **HTML5** – Estructura del contenido
- **CSS3** – Diseño y estilos personalizados
- **JavaScript** – Lógica del lado del cliente, validaciones y carrito
- **Python 3** – Servidor HTTP (WSGI)
- **MySQL** – Base de datos relacional
- **WAMP Server** – Gestión de MySQL
- **Git & GitHub** – Control de versiones

---

## 📂 Estructura del proyecto

proyecto_individual/
│
├── css/
│ └── estilos.css
│
├── js/
│ ├── carrito.js
│ └── validaciones.js
|  └── cuenta.js
|  └── catalogo.js
│
├── images/
│ └── logo.jpeg, etc.
│
├── index.html
├── catalogo.html
├── carrito.html
├── pedidos.html
├── opiniones.html
├── contacto.html
├── cuenta.html
│
├── server.py
└── README.md

yaml
Copiar código

---

## Requisitos previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

- Python 3.x
- WAMP Server (MySQL activo)
- Navegador web (Chrome, Edge o Firefox)
- Git (opcional, para clonar el repositorio)

---

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Aleyda1530/Proyecto_KIT-SHINE.git
Ingresar a la carpeta del proyecto:

bash
Copiar código
cd proyecto_individual
Ejecutar el servidor en Python:

bash
Copiar código
python server.py
Abrir el navegador y acceder a:

arduino
Copiar código
http://localhost:8000
Base de datos (MySQL)
La aplicación utiliza una base de datos MySQL gestionada con WAMP Server para almacenar la información enviada desde los formularios.

Tablas principales
pedidos

nombre, apellido, dni, dirección, correo, producto, método de pago, comentarios

opiniones

nombre, apellido, correo, calificación, comentario

contacto

nombre, apellido, correo, tema, mensaje

⚠️ La conexión a la base de datos se realiza en modo local como parte del entorno de desarrollo.

Funcionalidades principales
Navegación completa entre páginas

Catálogo de productos

Carrito de compras con localStorage

Validación de formularios con JavaScript

Generación de boleta de pago (simulada)

Envío de formularios mediante POST

Almacenamiento de datos en MySQL

Servidor HTTP propio en Python

Trabajo futuro
Implementar autenticación de usuarios

Generar boletas reales en formato PDF

Envío automático de correos

Panel administrativo

Despliegue en un servidor en la nube

