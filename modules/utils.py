import os

def clear_console():
    """Metodo encargado de limpiar la consola"""
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def print_title(title):
    """Metodo encargado de imprimir un titulo en pantalla"""
    print(f"\33[92m ********* {title} ************ \33[0m")