import random
numR = random.randint(1,5)
while True:
  num=int(input("Adivina el número: "))
  if num==numR:
    print("Adivinaste")
    break
  else:
    print("Incorrecto")