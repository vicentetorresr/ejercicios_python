def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        return True
    else:
        return False

contrasena = input("Ingrese una contraseña: ")

if validar_contrasena(contrasena):
    print("La contraseña cumple con los requisitos.")
else:
    print("La contraseña no cumple con los requisitos.")
