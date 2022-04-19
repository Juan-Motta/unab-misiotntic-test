from modules.utils import clear_console, print_title

def show_results(matches):
    """"
    Funcion principal para mostrar juegos, se encarga de llamar a las funciones
        order_matches: encargado de ordenar la lista de juegos del mas reciente al mas antiguo
        print_results: encargado de imprimir en pantalla los juegos en el formato especificado
    """
    #[*matches] crea una copia del objeto matches para cortar la referencia al objeto original y no mutarlo
    ordered_matches = order_matches([*matches])
    print_results(ordered_matches)
    print()
    input("Presione cualquier tecla para volver al menu principal...")

def order_matches(matches):
    ordered_matches = []
    while len(matches) != 0:
        temporal_date = None
        for index, match in enumerate(matches):
            if not temporal_date:
                temporal_date = (index, match)
            if match['date'] > temporal_date[1]['date']:
                temporal_date = (index, match)
        ordered_matches.append(temporal_date[1])
        matches.pop(temporal_date[0])
    return ordered_matches

def print_results(matches):
    clear_console()
    print_title("RESULTADOS")
    print()
    for match in matches:
        print(f"\33[96m{match['date'].strftime('%d-%m-%Y')}\33[0m - {'UNAB'} ({match['unab_points']}) \33[92mVS\33[0m ({match['rival_points']}) {match['rival_name']}")

        
        
        
        
        