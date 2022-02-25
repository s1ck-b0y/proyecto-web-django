N = 10
for i in range(N):
    print(f"{i}.Hello world");

email=False
mi_email=input("Introduce tu direccion de email: ")

for i in mi_email:
    if (i=="@"):
        email=True
if email:
    print("Email es correcto")
else:
    print("Email es incorrecto")

name=input("Introduce tu nombre: ")
count=0
for i in name:
    if (i == " "):
        continue
    count+=1
print(count)