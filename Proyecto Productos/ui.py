# ui.py
"""
Módulo de Interfaz de Usuario (Presentation Layer). 🎨

Este módulo es el único responsable de toda la interacción con el usuario en la
consola. Centraliza la presentación de menús, listas de datos y mensajes de
estado (éxito, error, información). Utiliza la librería `colorama` para
dar estilo y color a la salida, mejorando la legibilidad y la experiencia
de usuario.

"""
from colorama import Fore, Style, Back

def mostrar_menu_principal():
    """
    Imprime el menú principal de la aplicación en la consola.

    Args:
        Esta función no recibe parámetros.
    La función no devuelve ningún valor.
    """
    print(Fore.CYAN + "\n====== MENÚ PRINCIPAL ======")
    print("1.📦 Gestionar Productos")
    print("2.📋 Gestionar Categorías")
    print("3.🔚 Salir del programa")
    print(Fore.CYAN + "==========================\n")

def mostrar_menu_productos():
    """
    Imprime el submenú de gestión de productos.

    Args:
        Esta función no recibe parámetros.
        La función no devuelve ningún valor.
    """
    print(Fore.CYAN + "\n--- Menú de Productos ---")
    print("1. ✅ Agregar producto")
    print("2. ✏️ Modificar producto")
    print("3. 👁️  Visualizar productos")
    print("4. 🔍 Buscar producto")
    print("5. ❌ Eliminar producto")
    print("6. 🔙 Volver al menú principal")
    print(Fore.CYAN + "-------------------------\n")

def mostrar_menu_categorias():
    """
    Imprime el submenú de gestión de categorías.

    Args:
        Esta función no recibe parámetros.
    La función no devuelve ningún valor.
    """
    print(Fore.CYAN + "\n--- Menú de Categorías ---")
    print("1. ✅  Agregar categoría")
    print("2. 👁️  Visualizar categorías")
    print("3. ✏️  Modificar categoría")
    print("4. ❌  Eliminar categoría")
    print("5. 🔙 Volver al menú principal")
    print(Fore.CYAN + "--------------------------\n")

def obtener_input(mensaje_prompt):
    """
    Obtiene una entrada del usuario con un estilo y color consistentes.

    Args:
        mensaje_prompt (str): El mensaje que se mostrará al usuario para
            solicitar la entrada.

    Retorna:
        un str: La entrada del usuario, sin espacios en blanco al inicio o al final.
    """
    return input(f"{Fore.CYAN}{mensaje_prompt}{Style.RESET_ALL}").strip()

def mostrar_lista_categorias(categorias):
    """
    Muestra una lista formateada de categorías con su ID y nombre.

    Si la lista está vacía, muestra un mensaje informativo y retorna False.

    Args:
        categorias: Una lista de tuplas, donde cada tupla
            representa una categoría con el formato `(id, nombre)`.

    Retorna:
       un booleano: `True` si se mostraron categorías, `False` si la lista estaba vacía.
    """
    if not categorias:
        mostrar_mensaje_info("No hay categorías registradas.")
        return False
    print(Fore.MAGENTA + "\n--- Categorías Registradas ---")
    for id_cat, nombre in categorias:
        print(f"ID: {id_cat} | Nombre: {nombre}")
    print(Fore.MAGENTA + "----------------------------\n")
    return True

def mostrar_lista_seleccion(items):
    """
    Muestra una lista de ítems numerada para que el usuario elija uno.
    Cada ítem se muestra con su índice y nombre, utilizando colores para
    mejorar la legibilidad.

    Args:
        items: Una lista de tuplas donde el segundo elemento
            (`item[1]`) es el nombre que se debe mostrar.

    La función no devuelve ningún valor.
    """
    for i, item in enumerate(items):
        print(f"{Fore.YELLOW}{i + 1}.{Style.RESET_ALL} {item[1]}") # item[1] es el nombre

def mostrar_lista_productos(productos):
    """
    Muestra una lista formateada de productos con todos sus detalles.

    Incluye ID, nombre, categoría y precio. Si la lista está vacía,
    muestra un mensaje informativo y retorna False.

    Args:
        productos: Una lista de tuplas con los datos del producto,
            en el formato `(id, nombre, categoria, precio)`.

    Retorna:
        un booleano: `True` si se mostraron productos, `False` si la lista estaba vacía.
    """
    if not productos:
        mostrar_mensaje_info(" No hay productos registrados.")
        return False
    print(Fore.MAGENTA + "\n--- Productos Registrados ---")
    for id_prod, nombre, categoria, precio in productos:
        print(f"{Fore.YELLOW}ID: {Style.RESET_ALL}{id_prod} | "
              f"{Fore.YELLOW}Nombre: {Style.RESET_ALL}{nombre} | "
              f"{Fore.YELLOW}Categoría: {Style.RESET_ALL}{categoria} | "
              f"{Fore.YELLOW}Precio: {Style.RESET_ALL}${precio}")
    print(Fore.MAGENTA + "---------------------------\n")
    return True

def mostrar_resultados_busqueda(resultados):
    """
    Muestra los resultados de una búsqueda de productos.

    Args:
        resultados: Una lista de tuplas con los productos
            encontrados, en el formato `(nombre, categoria, precio)`.
    La función no devuelve ningún valor.
    """
    print(Fore.MAGENTA + "\n--- Resultados de la búsqueda ---")
    for nombre, categoria, precio in resultados:
        print(f"Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
    print(Fore.MAGENTA + "-------------------------------\n")

def mostrar_mensaje_exito(mensaje):
    """
    Muestra un mensaje de éxito con formato (color verde y un check).

    Args:
        mensaje (str): El texto del mensaje a mostrar.
    La función no devuelve ningún valor.
    """
    print(Fore.GREEN + f"✅ {mensaje}")

def mostrar_mensaje_error(mensaje):
    """
    Muestra un mensaje de error resaltado (texto rojo sobre fondo blanco).

    Args:
        mensaje (str): El texto del mensaje de error a mostrar.

    La función no devuelve ningún valor.
    """
    print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}❌ {mensaje}{Style.RESET_ALL}")

def mostrar_mensaje_info(mensaje):
    """
    Muestra un mensaje informativo con formato (color amarillo y un ícono).

    Args:
        mensaje (str): El texto del mensaje informativo a mostrar.

    La función no devuelve ningún valor.
    """
    print(Fore.YELLOW + f"ℹ️ {mensaje}")

def mostrar_menu_modificar_producto():
    """
    Muestra las opciones disponibles para modificar un producto existente.

    Args:
        Esta función no recibe parámetros.
    La función no devuelve ningún valor.
    """
    print(Fore.CYAN + "\n--- ¿Qué desea modificar? ---")
    print("1. Nombre")
    print("2. Categoría")
    print("3. Precio")
    print("4. Finalizar modificación")
    print(Fore.CYAN + "----------------------------\n")