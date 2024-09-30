"""
EJERCICIO 2

Escribe un script que borre los ceros por la izquierda de una dirección IP pasada por parámetros.

Por ejemplo: "210.010.090.180", devolvería "210.10.90.180"
"""

import sys

def remove_zeros(string_ip: str) -> str:
    octets = string_ip.split('.')
    int_octets = []
    for octet in octets:
        try:
            octet=int(octet)
            int_octets.append(octet)
        except Exception as e:
            print(e, type(e))
            return ''

    ip_address = '.'.join(map(str, int_octets))
    return ip_address

def validate_ip(ip: str) -> bool:
    octets_list = ip.split('.')
    if len(octets_list)!=4:
        return False
    for octet in octets_list:
        if len(octet)>3:
            return False
        try:
            octet=int(octet)
            if not 0 <= octet <= 255:
                return False
        except ValueError:
            return False
    return True

# lista_ips = ['253.100.50.25', '192.168.1', '192.0168.1.255', '192.168.1.1.5', '192.168.-1.50', '192.168.abc.10', '192.168.1.10.', '192..1.10', '192.168.1.10 25', '300.300.300.300']



if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        ip = sys.argv[1]
        ip_modified = remove_zeros(ip)
        if validate_ip(ip_modified):
            line = f"IP inicial: {ip}, IP arreglada: {ip_modified}, IP válida"
        else:
            line = f"IP inicial: {ip}, IP arreglada: {ip_modified}  IP no válida"
        print(line)