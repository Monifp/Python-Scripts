# Gestor de Productos en Terminal

Este es un programa de consola para gestionar un inventario de productos y categorías, escrito en Python. Permite realizar operaciones CRUD (Crear, Leer, Modificar, Eliminar) tanto para productos como para categorías.

## Características
- Gestión completa de productos (agregar, modificar, eliminar, buscar, visualizar).
- Gestión completa de categorías (agregar, modificar, eliminar, con un límite de 10).
- Interfaz de usuario colorida en la terminal gracias a `colorama`.
- Persistencia de datos mediante una base de datos SQLite (`productos.db`).
- Código modularizado para fácil mantenimiento.

## Prerrequisitos
- Python 3.x

## Cómo Ejecutarlo
1.  Clona o descarga este repositorio.
2.  Abre una terminal en la carpeta del proyecto.
3.  Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Ejecuta el programa:
    ```bash
    python main.py
    ```