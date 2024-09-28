
import sys

"""
EJERCICIO 1

Escribe un script que sume todos los números de una cadena de texto pasada por parámetros.

Por ejemplo: "Frogtek se fundó en 2010 y ahora tiene 40 empleados", devolvería "2050"
Por ejemplo: "Frogtek desarrolla un software para la gestión de tiendas de barrio", devolvería "0"

"""

def convert_number(input):
    input = input.replace(",", ".").rstrip('.')
    try:
        number= float(input)
        return number
    except ValueError:
        return 0

#string = "Frogtek se fundó en 2010, y ahora tiene 40 empleados y hay 20,1. ayer 23.1"

def process_string(string):
    splitted_string = string.split(" ")
    list_numbers = [convert_number(word) for word in splitted_string]
    total_number = sum(list_numbers)
    print(string)
    print(total_number)


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        string = sys.argv[1]
        process_string(string)

