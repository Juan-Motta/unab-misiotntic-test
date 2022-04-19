from modules.utils import clear_console, print_title

def show_clasification(matches):
    """
    Funcion principal para mostrar la clasificacion del equipo, se encarga de llamar a las funciones
        print_clasification: encargado de imprimir la informacion de la clasificacion
        get_data: encargado de calcular la informacion requerida
    """
    team_info = get_data(matches)
    print_clasification(team_info)
    input("Presione cualquier tecla para volver al menu...")

def print_clasification(info):
    clear_console()
    print_title("CLASIFICACION UNAB")
    print()
    print(f"Partidos jugados..... {info['total']}")
    print(f"\33[92mPartidos ganados\33[0m..... {info['won']}")
    print(f"\33[93mPartidos empatados\33[0m... {info['tied']}")
    print(f"\33[91mPartidos perdidos\33[0m.... {info['lost']}")
    print(f"\33[94mPuntos obtenidos\33[0m..... {info['points']}")
    print()

def get_data(matches):
    total_matches = len(matches)
    won_matches = 0
    lost_matches = 0
    tied_matches = 0
    points = 0
    for match in matches:
        if match['result'] == 'V':
            won_matches += 1
            points += 3
        if match['result'] == 'D':
            lost_matches += 1
        if match['result'] == 'E':
            tied_matches += 1
            points += 1
    return {
        'total': total_matches,
        'won': won_matches,
        'lost': lost_matches,
        'tied': tied_matches,
        'points': points
    }
        