import random
import string

def generar_caracteres_aleatorios(longitud):
    
    caracteres = string.ascii_letters + string.digits
    
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))
    return cadena_aleatoria


longitud_cadena = 10


cadena = generar_caracteres_aleatorios(longitud_cadena)
print("Cadena aleatoria generada:", cadena)