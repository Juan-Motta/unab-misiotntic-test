from modules.utils import clear_console
from modules.register import register_match
from modules.results import show_results
from modules.clasification import show_clasification

def main_menu(matches):
    """
    Funcion principal para mostrar el menu principal de la aplicacion, se encarga de leer
    las entradas proporcionadas por el usuario y llamar a las funciones correspondientes a dicha entrada.
        register_match: Funcion que gestiona el registro de juegos
        show_results: Funcion encargada de mostrar el historial de resultados
        
    """
    clear_console()
    print_title("REGISTRO PARTIDOS DE LA UNAB")
    print_options({
        "0": "Salir",
        "1": "Registrar partido",
        "2": "Ver resultados",
        "3": "Tabla de clasificacion"
    })
    print()
    read_option(matches)
    
    
def print_title(title):
    print(f"\33[92m ********* {title} ************ \33[0m")
    print()

def print_options(options):
    for key, option in options.items():
        print(f"\33[92m {key}. \33[0m {option}")

def read_option(matches):
    while True:
        input_option = input("Ingrese una opcion valida: ")
        if input_option == "1":
            register_match(matches)
        elif input_option == "2":
            show_results(matches)
        elif input_option == "3":
            show_clasification(matches)
        elif input_option == "0":
            exit()
        else:
            print("\33[91m La opcion ingresada es invalida \33[0m")
            input("Presione cualquier tecla para intentar de nuevo ")
        main_menu(matches)