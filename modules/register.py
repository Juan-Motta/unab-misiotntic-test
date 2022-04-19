from datetime import datetime

from modules.utils import clear_console, print_title


def register_match(matches):
    """
    Funcion principal para registrar juegos, se encarga de llamar a las funciones
        read_date: encargado de registrar y valida la fecha del partido
        read_name: encargado de registrar y validar el nombre del equipo contrario
        read_points: encargado de leer y validar el numero de goles
    """
    date = read_date("Ingrese la fecha del partido (DD-MM-AAAA): ")
    rival_name = read_name("Ingrese el nombre del equipo rival: ")
    rival_points = read_points(f"Ingrese el numero de goles del equipo {rival_name}: ")
    unab_points = read_points("Ingrese el numero de goles del equipo UNAB: ")
    result = generate_result(rival_points, unab_points)
    match = {
        'date': date,
        'rival_name': rival_name,
        'rival_points': rival_points,
        'unab_points': unab_points,
        'result': result
    }
    matches.append(match)
    print_match(match, matches)

def read_name(description):
    clear_console()
    print_title("REGISTRO DE PARTIDO")
    rival_name = input(description)
    return rival_name

def read_date(description):
    match_date = None
    date_is_invalid = True
    while date_is_invalid:
        try:
            clear_console()
            print_title("REGISTRO DE PARTIDO")
            match_date_input = input(description)
            match_date = datetime.strptime(match_date_input, "%d-%m-%Y")
            date_is_invalid = False
        except Exception as e:
            print("\33[91m La formato ingresado debe ser DD-MM-AAAA \33[0m")
            input("Presione cualquier tecla para intentar de nuevo...")
    return match_date

def read_points(description):
    points = 0
    points_is_invalid = True
    while points_is_invalid:
        clear_console()
        print_title("REGISTRO DE PARTIDO")
        poins_input = input(description)
        if poins_input.isnumeric() and int(poins_input) >= 0:
            points = poins_input
            points_is_invalid = False
        else:
            print("\33[91m El numero ingresado debe ser valido \33[0m")
            input("Presione cualquier tecla para intentar de nuevo...")
    return points 

def generate_result(rival_points, unab_points):
    if rival_points > unab_points:
        return 'D'
    if rival_points < unab_points:
        return 'V'
    if rival_points == unab_points:
        return 'E'

def print_match(match, matches):
    clear_console()
    print_title("REGISTRO DE PARTIDO")
    print()
    print("Resumen partido agregado")
    print()
    print(f"Fecha:............ {match['date']}")
    print(f"Nombre rival:..... {match['rival_name']}")
    print(f"Goles del rival:.. {match['rival_points']}")
    print(f"Goles de la UNAB:. {match['unab_points']}")
    print()
    add_another_input = input("Desea agregar otro partido? [Y/N]: ")
    if add_another_input.upper() == 'Y':
        register_match(matches)
    
    