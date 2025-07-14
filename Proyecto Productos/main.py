 # main.py
from colorama import init
import database as db
import ui
import productos
import categorias

def main():
    """Punto de entrada principal de la aplicación."""
    init(autoreset=True)
    db.inicializar_db()

    while True:
        if db.contar_categorias_db() == 0:
            ui.mostrar_mensaje_error("¡ATENCIÓN! No hay categorías en el sistema.")
            ui.mostrar_mensaje_info(" El primer paso es crear al menos una categoría.")
            categorias.gestionar_categorias()
            continue

        ui.mostrar_menu_principal()
        opcion = ui.obtener_input("Seleccione una opción: ")

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
