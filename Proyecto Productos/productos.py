 # productos.py
import database as db
import ui

def agregar_nuevo_producto():
    """Orquesta la adición de un nuevo producto con validaciones."""
    categorias = db.obtener_categorias_db()
    if not categorias:
        ui.mostrar_mensaje_error("No hay categorías. Agregue una desde 'Gestionar Categorías'.")
        return
        
    print("\nPor favor, elija una categoría:")
    ui.mostrar_lista_seleccion(categorias)
    
    # Bucle para la selección de categoría
    while True:
        try:
            num_cat_str = ui.obtener_input("Seleccione el número de la categoría: ")
            num_cat = int(num_cat_str)
            if 1 <= num_cat <= len(categorias):
                categoria_id = categorias[num_cat - 1][0]
                break
            else:
                ui.mostrar_mensaje_error("Número fuera de rango.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un número.")

    # Bucle para el nombre del producto
    while True:
        nombre = ui.obtener_input("Ingrese el nombre del producto: ")
        if nombre:
            break
        ui.mostrar_mensaje_error("El nombre no puede estar vacío.")

    # Bucle para el precio
    while True:
        try:
            precio_str = ui.obtener_input("Ingrese el precio del producto (entero): ")
            precio = int(precio_str)
            if precio >= 0:
                break
            else:
                ui.mostrar_mensaje_error("El precio no puede ser un número negativo.")
        except ValueError:
            ui.mostrar_mensaje_error("El precio debe ser un número entero.")
        
    db.agregar_producto_db(nombre, categoria_id, precio)
    ui.mostrar_mensaje_exito(f"Producto '{nombre}' agregado.")

def modificar_un_producto():
    """Orquesta la modificación de un producto con validaciones."""
    productos = db.obtener_productos_db()
    if not ui.mostrar_lista_productos(productos):
        return

    # Bucle para obtener un ID de producto válido
    while True:
        try:
            id_prod_str = ui.obtener_input("Ingrese el ID del producto a modificar: ")
            id_prod = int(id_prod_str)
            if id_prod in [p[0] for p in productos]:
                break
            else:
                ui.mostrar_mensaje_error("ID de producto no válido.")
        except ValueError:
            ui.mostrar_mensaje_error("Debe ingresar un ID numérico.")

    while True:
        ui.mostrar_menu_modificar_producto()
        opcion = ui.obtener_input("Seleccione una opción: ")

        if opcion == '1': # Modificar Nombre
            while True:
                nuevo_nombre = ui.obtener_input("Ingrese el nuevo nombre del producto: ")
                if nuevo_nombre:
                    db.modificar_producto_db(id_prod, 'nombre', nuevo_nombre)
                    ui.mostrar_mensaje_exito("Nombre actualizado.")
                    break
                else:
                    ui.mostrar_mensaje_error("El nombre no puede estar vacío.")

        elif opcion == '2': # Modificar Categoría
            categorias = db.obtener_categorias_db()
            print("\nElija la nueva categoría:")
            ui.mostrar_lista_seleccion(categorias)
            while True:
                try:
                    num_cat_str = ui.obtener_input("Seleccione el número de la nueva categoría: ")
                    num_cat = int(num_cat_str)
                    if 1 <= num_cat <= len(categorias):
                        nueva_cat_id = categorias[num_cat - 1][0]
                        db.modificar_producto_db(id_prod, 'categoria_id', nueva_cat_id)
                        ui.mostrar_mensaje_exito("Categoría actualizada.")
                        break
                    else:
                        ui.mostrar_mensaje_error("Número fuera de rango.")
                except ValueError:
                    ui.mostrar_mensaje_error("Debe ingresar un número.")

        elif opcion == '3': # Modificar Precio
            while True:
                try:
                    precio_str = ui.obtener_input("Ingrese el nuevo precio (entero): ")
                    nuevo_precio = int(precio_str)
                    if nuevo_precio >= 0:
                        db.modificar_producto_db(id_prod, 'precio', nuevo_precio)
                        ui.mostrar_mensaje_exito("Precio actualizado.")
                        break
                    else:
                        ui.mostrar_mensaje_error("El precio no puede ser un número negativo.")
                except ValueError:
                    ui.mostrar_mensaje_error("El precio debe ser un número entero.")

        elif opcion == '4':
            ui.mostrar_mensaje_info("Modificación finalizada.")
            break
        else:
            ui.mostrar_mensaje_error("Opción inválida.")

def eliminar_un_producto():
    """Orquesta la eliminación de un producto con validaciones."""
    productos = db.obtener_productos_db()
    if not ui.mostrar_lista_productos(productos):
        return
        
    while True:
        id_prod_str = ui.obtener_input("Ingrese el ID del producto a eliminar (o 'S' para salir): ")
        if id_prod_str.upper() == 'S':
            ui.mostrar_mensaje_info("Operación de eliminación cancelada.")
            return

        try:
            id_prod = int(id_prod_str)
            if id_prod in [p[0] for p in productos]:
                db.eliminar_producto_db(id_prod)
                ui.mostrar_mensaje_exito("Producto eliminado.")
                return
            else:
                ui.mostrar_mensaje_error("ID de producto no válido.")
        except ValueError:
            ui.mostrar_mensaje_error("Entrada no válida. Ingrese un ID numérico o 'S'.")

def buscar_un_producto():
    """Orquesta la búsqueda de productos."""
    termino = ui.obtener_input("Ingrese el nombre del producto a buscar: ")
    resultados = db.buscar_productos_db(termino.lower())
    if not resultados:
        ui.mostrar_mensaje_error(f" No se encontraron productos con el nombre '{termino}'.")
    else:
        ui.mostrar_resultados_busqueda(resultados)

def gestionar_productos():
    """Bucle principal para la gestión de productos."""
    while True:
        ui.mostrar_menu_productos()
        opcion = ui.obtener_input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_nuevo_producto()
        elif opcion == '2':
            modificar_un_producto()
        elif opcion == '3':
            ui.mostrar_lista_productos(db.obtener_productos_db())
        elif opcion == '4':
            buscar_un_producto()
        elif opcion == '5':
            eliminar_un_producto()
        elif opcion == '6':
            break
        else:
            ui.mostrar_mensaje_error(" Opción inválida.")