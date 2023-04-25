def function(chain):
    estado_actual = 1
    if len(chain) == 0:
        return False
    else:
        value = True
        for letter in chain:
            if estado_actual == 1:
                if letter == "a":
                    estado_actual = 2
                elif letter == "b":
                    estado_actual = 3
            elif estado_actual == 2:
                if letter == "a":
                    estado_actual = 2
                elif letter == "b":
                    estado_actual = 3
                else:
                    value = False
            elif estado_actual == 3:
                if letter == "c":
                    estado_actual = 3
                elif letter == "a":
                    estado_actual = 2
                elif letter == "b":
                    value = False
            elif value is False:
                break
        if (estado_actual == 2 or estado_actual == 3) and value is True:
            return True
        else:
            return False


cadena = input("Enter chain: ")
value = function(cadena)
if value == True:
    print("the acepted chain")
else:
    print("the chain not acepted")
