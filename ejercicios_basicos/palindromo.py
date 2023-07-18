txt = input("Ingrese un texto: ")
reversed_txt = ''.join(reversed(txt))

if txt == reversed_txt:
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")
