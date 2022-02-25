def add(n1,n2):
    return (n1+n2)

def sub(n1, n2):
    return n1-n2

def mul(n1,n2):
    return (n1*n2)

def div(n1,n2):
    try:
        return (n1/n2)
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return ("Operción errónea")

while True:
    try:
        n1=int(input("Introduce el primer operando:"))
        n2=int(input("Introduce el segundo operando:"))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Inténtelo de nuevo.")

op=input("Introduce la operación a realizar (suma, resta, multiplica, divide):")

if (op == "suma"):
    print(add(n1,n2))
elif (op == "resta"):
    print(sub(n1,n2))
elif (op == "multiplica"):
    print(mul(n1,n2))
elif (op == "divide"):
    print(div(n1,n2))
else:
    print("Operación no completada")

print("Operación ejecutada. Continuación de ejecución del programa")