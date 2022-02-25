def generaPares(limite):
    num=1
    while (num < limite):
        yield num*2
        num+=1

devuelve_pares=generaPares(10)
print(generaPares(10))

# for i in devuelve_pares:
#     print(i)
    
print(next(devuelve_pares))
print("Aquí podría ir más código...")
print(next(devuelve_pares))
print("Aquí podría ir más código...")
print(next(devuelve_pares))