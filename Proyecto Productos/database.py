 # database.py
import sqlite3

DB_NAME = "productos.db"

def obtener_conexion():
    """Retorna una conexión a la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_db():
    """Crea las tablas si no existen."""
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
    """Retorna el número total de categorías."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM categorias")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def obtener_categorias_db():
    """Retorna una lista de todas las categorías."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM categorias ORDER BY nombre")
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def agregar_categoria_db(nombre):
    """Agrega una nueva categoría a la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

def modificar_categoria_db(id_cat, nuevo_nombre):
    """Modifica el nombre de una categoría."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE categorias SET nombre = ? WHERE id = ?", (nuevo_nombre, id_cat))
    conn.commit()
    conn.close()

def contar_productos_en_categoria_db(id_cat):
    """Retorna cuántos productos pertenecen a una categoría."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos WHERE categoria_id = ?", (id_cat,))
    total = cursor.fetchone()[0]
    conn.close()
    return total

def eliminar_categoria_db(id_cat):
    """Elimina una categoría de la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = ?", (id_cat,))
    conn.commit()
    conn.close()

def obtener_productos_db():
    """Retorna una lista de todos los productos con sus categorías."""
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
    """Agrega un nuevo producto a la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, categoria_id, precio) VALUES (?, ?, ?)",
                   (nombre, cat_id, precio))
    conn.commit()
    conn.close()

def buscar_productos_db(termino):
    """Busca productos por un término en su nombre."""
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
    """Elimina un producto de la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    conn.commit()
    conn.close()

def modificar_producto_db(id_prod, campo_a_modificar, nuevo_valor):
    """
    Modifica un campo específico de un producto en la base de datos.
    
    Args:
        id_prod (int): El ID del producto a modificar.
        campo_a_modificar (str): El nombre de la columna a cambiar ('nombre', 'categoria_id', 'precio').
        nuevo_valor: El nuevo valor para el campo.
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