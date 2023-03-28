def solve(operation):
    terms = operation.split("+")
    operands = []
    for term in terms:
        factors = term.split("*")
        operands.append(factors)

    num_operands = len(operands)
    products = [1] * num_operands
    for i in range(num_operands):
        for factor in operands[i]:
            products[i] *= int(factor)

    return sum(products)


operacion = input("Ingresa la operacion a resolver: ")
resultado = solve(operacion)
print(f"El resultado de la operación '{operacion}' es: {resultado}")
