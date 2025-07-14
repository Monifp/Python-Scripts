 # ui.py
from colorama import Fore, Style, Back

def mostrar_menu_principal():
    print(Fore.CYAN + "\n====== MENÚ PRINCIPAL ======")
    print("1. Gestionar Productos")
    print("2. Gestionar Categorías")
    print("3. Salir del programa")
    print(Fore.CYAN + "==========================\n")

def mostrar_menu_productos():
    print(Fore.CYAN + "\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Modificar producto") # Nueva opción
    print("3. Visualizar productos")
    print("4. Buscar producto")
    print("5. Eliminar producto")
    print("6. Volver al menú principal")
    print(Fore.CYAN + "-------------------------\n") 

def mostrar_menu_categorias():
    print(Fore.CYAN + "\n--- Menú de Categorías ---")
    print("1. Agregar categoría")
    print("2. Visualizar categorías")
    print("3. Modificar categoría")
    print("4. Eliminar categoría")
    print("5. Volver al menú principal")
    print(Fore.CYAN + "--------------------------\n")

def obtener_input(mensaje_prompt):
    """Obtiene una entrada del usuario con un estilo consistente."""
    return input(f"{Fore.CYAN}{mensaje_prompt}{Style.RESET_ALL}").strip()

def mostrar_lista_categorias(categorias):
    """Muestra una lista formateada de categorías."""
    if not categorias:
        mostrar_mensaje_info("No hay categorías registradas.")
        return False
    print(Fore.MAGENTA + "\n--- Categorías Registradas ---")
    for id_cat, nombre in categorias:
        print(f"ID: {id_cat} | Nombre: {nombre}")
    print(Fore.MAGENTA + "----------------------------\n")
    return True

def mostrar_lista_seleccion(items):
    """Muestra una lista numerada para que el usuario elija."""
    for i, item in enumerate(items):
        print(f"{Fore.YELLOW}{i + 1}.{Style.RESET_ALL} {item[1]}") # item[1] es el nombre

def mostrar_lista_productos(productos):
    """Muestra una lista formateada de productos."""
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
    """Muestra los resultados de una búsqueda."""
    print(Fore.MAGENTA + "\n--- Resultados de la búsqueda ---")
    for nombre, categoria, precio in resultados:
        print(f"Nombre: {nombre}, Categoría: {categoria}, Precio: ${precio}")
    print(Fore.MAGENTA + "-------------------------------\n")

def mostrar_mensaje_exito(mensaje):
    print(Fore.GREEN + f"✅ {mensaje}")

def mostrar_mensaje_error(mensaje):
    """Muestra un mensaje de error con fondo blanco, texto rojo y en negrita."""
   
    print(f"{Back.WHITE}{Fore.RED}{Style.BRIGHT}❌ {mensaje}{Style.RESET_ALL}")

def mostrar_mensaje_info(mensaje):
    print(Fore.YELLOW + f"ℹ️ {mensaje}")

def mostrar_menu_modificar_producto():
    """Muestra las opciones para modificar un producto."""
    print(Fore.CYAN + "\n--- ¿Qué desea modificar? ---")
    print("1. Nombre")
    print("2. Categoría")
    print("3. Precio")
    print("4. Finalizar modificación")
    print(Fore.CYAN + "----------------------------\n")