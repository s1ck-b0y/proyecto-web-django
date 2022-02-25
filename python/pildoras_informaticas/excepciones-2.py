def div():
    try:
        n1=float(input("Introduzca el primer número: "))
        n2=float(input("Introduzca el segundo número: "))
        print("La division es: " + str(n1/n2))
    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    finally:
        print("Cálculo finalizado")

div()