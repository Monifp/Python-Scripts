# main.py
"""
Módulo principal y punto de entrada para la aplicación de gestión. 🚀

Este script actúa como el orquestador central del sistema. Es responsable de:
- Inicializar componentes clave como la base de datos y la librería de colores para la UI.
- Ejecutar el bucle principal de la aplicación, que presenta el menú al usuario.
- Validar pre-condiciones críticas, como la existencia de categorías antes de operar.
- Delegar las acciones del usuario a los módulos especializados (`productos`, `categorias`).

Dependencias:
- colorama: Para dar formato de color a la salida en la consola.
- database: Módulo de bajo nivel para la interacción con la base de datos.
- ui: Módulo para todos los elementos de la interfaz de usuario (menús, mensajes).
- productos: Módulo de lógica de negocio para la gestión de productos.
- categorias: Módulo de lógica de negocio para la gestión de categorías.
"""
from colorama import init
import database as db
import ui
import productos
import categorias

def main():
    """
    Ejecuta el ciclo de vida principal de la aplicación.

    Esta función inicializa la base de datos y la consola, y luego entra en un
    bucle infinito que presenta el menú principal. Antes de mostrar el menú,
    verifica si existe al menos una categoría en el sistema; si no es así,
    fuerza al usuario a crear una para garantizar la integridad de los datos
    al añadir productos.
    
    No recibe argumentos ni devuelve ningún valor.
    """
    init(autoreset=True)
    db.inicializar_db()

    while True:
        if db.contar_categorias_db() == 0:
            ui.mostrar_mensaje_error("¡ATENCIÓN! No hay categorías en el sistema.")
            ui.mostrar_mensaje_info(" Se necesita crear al menos UNA categoría para poder avanzar.")
            categorias.gestionar_categorias()
            continue

        ui.mostrar_menu_principal()
        opcion = ui.obtener_input(" Seleccione una opción: ")

        if opcion == '1':
            productos.gestionar_productos()
        elif opcion == '2':
            categorias.gestionar_categorias()
        elif opcion == '3':
            ui.mostrar_mensaje_exito("Saliendo del programa. ¡Gracias!")
            break
        else:
            ui.mostrar_mensaje_error("Opción inválida.")

if __name__ == "__main__":
    main()
