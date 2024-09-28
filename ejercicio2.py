"""
EJERCICIO 2

Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por parámetros.

Por ejemplo: "210.010.090.180", devolvería "210.10.90.180"
"""

import sys

def trim_ip(string_ip):
    ip_parts = string_ip.split('.')
    ip_parts = [part.lstrip('0') for part in ip_parts]
    ip_output = '.'.join(ip_parts)
    return ip_output

def validate_ip(ip):
    subnumbers_list = ip.split('.')
    if len(subnumbers_list)!=4:
        return False
    for subnumber in subnumbers_list:
        if len(subnumber)>3:
            return False
        try:
            subnumber=int(subnumber)
            if not 0 <= subnumber <= 255:
                return False
        except ValueError:
            return False
    return True

# lista_ips = ['253.100.50.25', '192.168.1', '192.0168.1.255', '192.168.1.1.5', '192.168.-1.50', '192.168.abc.10', '192.168.1.10.', '192..1.10', '192.168.1.10 25', '300.300.300.300']
#
#
# for i in lista_ips:
#     i = trim_ip(i)
#     v = validate_ip(i)
#     print(v)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        ip = sys.argv[1]
        trimmed_ip = trim_ip(ip)
        if validate_ip(trimmed_ip):
            print("Valid IP", trimmed_ip)
        else:
            print("Noy valid ip: ", trimmed_ip)