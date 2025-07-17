 # database.py
"""
Módulo de Acceso a Datos (Data Access Layer). 🗃️

Este script centraliza todas las interacciones con la base de datos SQLite.
Es responsable de establecer la conexión, crear el esquema inicial de la base
de datos y proporcionar funciones para realizar todas las operaciones CRUD
(Crear, Leer, Actualizar, Eliminar) en las tablas `categorias` y `productos`.

El uso de este módulo abstrae la lógica SQL del resto de la aplicación,
permitiendo que otros módulos (como `productos.py` o `categorias.py`)
operen con los datos sin necesidad de conocer los detalles de la implementación
de la base de datos.
"""
import sqlite3

DB_NAME = "productos.db"

def obtener_conexion():
    """
    Establece y retorna una conexión a la base de datos.
    Args:
        Esta función no recibe parámetros.
 
    """
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_db():
    """
    Crea las tablas `categorias` y `productos` si no existen.

    Args:
        Esta función no recibe parámetros.

  
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            precio INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE RESTRICT
        )
    """)
    conn.commit()
    conn.close()

def contar_categorias_db():
    """
    Cuenta y retorna el número total de categorías en la base de datos.

    Args:
        Esta función no recibe parámetros.

    Retorna:
        int: El número total de filas en la tabla `categorias`.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM categorias")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def obtener_categorias_db():
    """
    Retorna una lista de todas las categorías, ordenadas por nombre.

    Args:
        Esta función no recibe parámetros.

    Retorna:
          una lista de tuplas, donde cada tupla representa una
        categoría con el formato `(id, nombre)`.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM categorias ORDER BY nombre")
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def agregar_categoria_db(nombre):
    """
    Agrega una nueva categoría a la tabla `categorias`.

    Args:
        nombre (str): El nombre de la categoría a insertar.

     La función no devuelve ningún valor.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def modificar_categoria_db(id_cat, nuevo_nombre):
    """
    Modifica el nombre de una categoría existente, identificada por su ID.

    Args:
        id_cat (int): El ID de la categoría que se desea modificar.
        nuevo_nombre (str): El nuevo nombre para la categoría.
    
    La función no devuelve ningún valor.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE categorias SET nombre = ? WHERE id = ?", (nuevo_nombre, id_cat))
    conn.commit()
    conn.close()

def contar_productos_en_categoria_db(id_cat):
    """
    Retorna cuántos productos están asociados a una categoría específica.

    Args:
        id_cat (int): El ID de la categoría a consultar.

    Returns:
        int: El número de productos que pertenecen a la categoría dada.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE categoria_id = ?", (id_cat,))
    total = cursor.fetchone()[0]
    conn.close()
    return total

def eliminar_categoria_db(id_cat):
    """
    Elimina una categoría de la base de datos, identificada por su ID.

    Nota: Esta operación fallará con una excepción `sqlite3.IntegrityError`
    si la categoría tiene productos asociados, debido a la restricción
    `ON DELETE RESTRICT` definida en el esquema.

    Args:
        id_cat (int): El ID de la categoría a eliminar.

    La función no devuelve ningún valor.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (id_cat,))
    conn.commit()
    conn.close()

def obtener_productos_db():
    """
    Retorna una lista de todos los productos con el nombre de su categoría.

    Realiza un JOIN entre las tablas `productos` y `categorias` para incluir
    el nombre de la categoría en lugar de su ID.

    Args:
        Esta función no recibe parámetros.

    Retorna:
        una lista de tuplas, donde cada tupla representa un
        producto con el formato `(id_producto, nombre_producto, nombre_categoria, precio)`.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        SELECT p.id, p.nombre, c.nombre, p.precio FROM productos p
        JOIN categorias c ON p.categoria_id = c.id ORDER BY p.nombre
    """
    cursor.execute(sql)
    productos = cursor.fetchall()
    conn.close()
    return productos

def agregar_producto_db(nombre, cat_id, precio):
    """
    Agrega un nuevo producto a la tabla `productos`.

    Args:
        nombre (str): El nombre del producto.
        cat_id (int): El ID de la categoría a la que pertenece el producto.
        precio (int): El precio del producto.

    La función no devuelve ningún valor.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, categoria_id, precio) VALUES (?, ?, ?)",
                   (nombre, cat_id, precio))
    conn.commit()
    conn.close()

def buscar_productos_db(termino):
    """
    Busca productos cuyo nombre contenga un término de búsqueda.

    La búsqueda no distingue entre mayúsculas y minúsculas.

    Args:
        termino (str): El texto a buscar dentro del nombre de los productos.

    Retorna:
       una lista de tuplas con los productos encontrados.
        Cada tupla tiene el formato `(nombre_producto, nombre_categoria, precio)`.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = """
        SELECT p.nombre, c.nombre, p.precio FROM productos p
        JOIN categorias c ON p.categoria_id = c.id WHERE lower(p.nombre) LIKE ?
    """
    cursor.execute(sql, (f'%{termino}%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def eliminar_producto_db(id_prod):
    """
    Elimina un producto de la base de datos, identificado por su ID.

    Args:
        id_prod (int): El ID del producto a eliminar.

    La función no devuelve ningún valor.
    """
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conn.commit()
    conn.close()

def modificar_producto_db(id_prod, campo_a_modificar, nuevo_valor):
    """
    Modifica un campo específico de un producto en la base de datos.

    Utiliza una lista blanca de campos permitidos (`nombre`, `categoria_id`, `precio`)
    para construir la consulta SQL, previniendo así ataques de
    inyección SQL.

    Args:
        id_prod (int): El ID del producto a modificar.
        campo_a_modificar (str): El nombre de la columna a cambiar.
        nuevo_valor: El nuevo valor para el campo especificado.

    La función no devuelve ningún valor.

    Devuelve
        ValueError: Si el `campo_a_modificar` no está en la lista de
        campos permitidos.
    """
    # Lista blanca de campos permitidos para evitar inyección SQL
    campos_permitidos = ['nombre', 'categoria_id', 'precio']
    if campo_a_modificar not in campos_permitidos:
        # Esto es una medida de seguridad, no debería ocurrir en el flujo normal
        raise ValueError("Campo no válido para modificar")

    sql = f"UPDATE productos SET {campo_a_modificar} = ? WHERE id = ?"
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(sql, (nuevo_valor, id_prod))
    conn.commit()
    conn.close()