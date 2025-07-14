 # categorias.py
import sqlite3
import database as db
import ui

def agregar_nueva_categoria():
    """Orquesta la adición de una nueva categoría, validando la entrada."""
    if db.contar_categorias_db() >= 10:
        ui.mostrar_mensaje_error("Ud ha alcanzado el límite de 10 categorías. Seleccione otra opcion")
        return
    
    # Bucle para asegurar que el nombre no esté vacío
    while True:
        nombre = ui.obtener_input("Ingrese el nombre de la nueva categoría: ")
        if nombre:
            break
        ui.mostrar_mensaje_error("El nombre no puede estar vacío.")

    try:
        db.agregar_categoria_db(nombre)
        ui.mostrar_mensaje_exito(f"Categoría '{nombre}' agregada.")
    except sqlite3.IntegrityError:
        ui.mostrar_mensaje_error(f"La categoría '{nombre}' ya existe.")

def modificar_una_categoria():
    """Orquesta la modificación de una categoría, validando las entradas."""
    categorias = db.obtener_categorias_db()
    if not ui.mostrar_lista_categorias(categorias):
        return
        
    # Bucle para obtener un ID válido
    while True:
        try:
            id_cat_str = ui.obtener_input("Ingrese el ID de la categoría a modificar: ")
            id_cat = int(id_cat_str)
            if id_cat in [c[0] for c in categorias]:
                break # El ID es válido y existe
            else:
                ui.mostrar_mensaje_error("ID no válido. Intente de nuevo.")
        except ValueError:
            ui.mostrar_mensaje_error(" Debe ingresar un ID numérico.")

    # Bucle para obtener un nuevo nombre válido
    while True:
        nuevo_nombre = ui.obtener_input("Ingrese el nuevo nombre: ")
        if nuevo_nombre:
            break
        ui.mostrar_mensaje_error("El nombre no puede estar vacío.")

    try:
        db.modificar_categoria_db(id_cat, nuevo_nombre)
        ui.mostrar_mensaje_exito("Categoría modificada.")
    except sqlite3.IntegrityError:
        ui.mostrar_mensaje_error(f"El nombre '{nuevo_nombre}' ya existe.")

def eliminar_una_categoria():
    """Orquesta la eliminación de una categoría, validando la entrada."""
    categorias = db.obtener_categorias_db()
    if not ui.mostrar_lista_categorias(categorias):
        return
        
    # Bucle para obtener un ID válido
    while True:
        try:
            id_cat_str = ui.obtener_input("Ingrese el ID de la categoría a eliminar: ")
            id_cat = int(id_cat_str)
            if id_cat in [c[0] for c in categorias]:
                break # El ID es válido y existe
            else:
                ui.mostrar_mensaje_error("ID no válido. Intente de nuevo.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un ID numérico.")

    if db.contar_productos_en_categoria_db(id_cat) > 0:
        ui.mostrar_mensaje_error("No se puede eliminar, tiene productos asociados.Seleccione otra opcion")
        return
        
    db.eliminar_categoria_db(id_cat)
    ui.mostrar_mensaje_exito("Categoría eliminada.")

def gestionar_categorias():
    """Bucle principal para la gestión de categorías."""
    while True:
        ui.mostrar_menu_categorias()
        opcion = ui.obtener_input("Seleccione una opción: ")
        if opcion == '1':
            agregar_nueva_categoria()
        elif opcion == '2':
            ui.mostrar_lista_categorias(db.obtener_categorias_db())
        elif opcion == '3':
            modificar_una_categoria()
        elif opcion == '4':
            eliminar_una_categoria()
        elif opcion == '5':
            break
        else:
            ui.mostrar_mensaje_error("Opción inválida.")