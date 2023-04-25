def function(chain):
    inicial_status = 1
    if len(chain) == 0:
        value = False
        return value
    else:
        value = True
        for letters in chain:
            if inicial_status == 1:
                if letters == "a":
                    inicial_status = 2
                elif letters == "b":
                    inicial_status = 3
                else:
                    value = False
                    break
            elif inicial_status == 2:
                if letters == "a":
                    inicial_status = 4
                elif letters == "b":
                    inicial_status = 3
                else:
                    value = False
                    break
            elif inicial_status == 3:
                if letters == "a":
                    inicial_status = 2
                elif letters == "b":
                    inicial_status = 5
                else:
                    value = False
                    break
            elif inicial_status == 4:
                if letters == "a":
                    inicial_status = 4
                elif letters == "b":
                    inicial_status = 3
                else:
                    value = False
                    break
            elif inicial_status == 5:
                if letters == "a":
                    inicial_status = 2
                elif letters == "b":
                    inicial_status = 5
                else:
                    value = False
                    break
            elif value is False:
                break
        if inicial_status == 1 or inicial_status == 3 or inicial_status == 4:
            value = False
            return value
        else:
            value = True
            return value


chain = input("enter the chain: ")
value = function(chain)
if value is True:
    print("the chain acepted")
else:
    print("the chain not acepted")
