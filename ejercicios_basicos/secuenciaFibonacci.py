num1 = 0
num2 = 1
for i in range(1,100):
  suma=num1+num2
  num1=num2
  num2=suma
  print(suma)