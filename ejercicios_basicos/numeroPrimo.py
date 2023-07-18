num = int(input("Ingrese un número: "))
cont = 0

for i in range(1, num+1):
    if num % i == 0:
        cont = cont + 1

if cont == 2:
    print("El número es primo")
else:
    print("El número no es primo")
