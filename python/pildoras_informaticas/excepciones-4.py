import math

def calc_raiz(n1):
    if (n1 < 0):
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(n1) 
        
n1=int(input("Introduzca un número: "))
try:
    print(calc_raiz(n1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")