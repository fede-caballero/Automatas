chain = input("Ingresa tu expresion: ")


def solve(chain):
    list_mult = []
    spl_1 = chain.split("+")
    for i in spl_1:
        spl_2 = i.split("*")
        list_mult.append(spl_2)
    num_sum = 0
    result = 0
    num_mult = 0
    for terms in list_mult:
        result += num_mult
        num_mult = 1
        for mult in terms:
            if len(terms) != 1:
                num_mult *= int(mult)
            elif len(terms) == 1:
                num_sum += int(mult)
                result += num_sum
                num_mult = 0
    result += num_mult
    print("El resultado es: ", int(result))


solve(chain)
