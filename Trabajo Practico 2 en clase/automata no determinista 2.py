def funtion(cadena):
    value = True
    estado_actual = 1
    for letter in cadena:
        if estado_actual == 1:
            if letter == "a":
                estado_actual = 2
                corroborar = True
            elif letter == "b":
                estado_actual = 1
                corroborar = False
            else:
                value = False
        elif estado_actual == 2:
            if letter == "a":
                estado_actual = 1
            elif letter == "b":
                estado_actual = 7
            else:
                value = False
        elif estado_actual == 7:
            if letter == "b":
                estado_actual = 5
            elif letter == "a":
                value = False
                break
            else:
                value = False
        elif estado_actual == 6:
            if letter == "a":
                value = False
                break
            elif letter == "b":
                estado_actual = 5
            else:
                value = False
    if estado_actual == 2 and corroborar is True:
        value = True
    elif estado_actual == 2 and corroborar is False:
        value = False
    if estado_actual == 7:
        value = False
    else:
        value = True
    return value


cadena = input("enter chain: ")
result = funtion(cadena)
if result is True:
    print("La cadena es valida.")
else:
    print("La cadena no es valida.")
