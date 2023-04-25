cadena = input("Introduce una cadena: ")


def function(cadena):
    value = True
    estado = 1
    for simbolo in cadena:
        if simbolo == "a" and estado == 1:
            estado = 1
            value = True
        elif simbolo == "b" and estado == 1:
            estado = 1
            value = True
        else:
            value = False
    return value


if function(cadena) is True:
    print("la cadena es valida")
else:
    print("Cadena no valida")
