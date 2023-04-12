expr = str(input("Ingresa la expresion a resolver: "))

def solve(expr):
    terms = expr.split("+")
    addends = []
    mult_raw = []
    mult_pre_results = []
    final_list = []
    
    #Recorro la expresion y separo los terminos con el simbolo "+"
    for term in terms:
        if term.isdigit():
            int_term = int(term)
            addends.append(int_term)
                    
        else:
            mult_raw.append(term)
    
    #Recorro la lista de los elementos que se estan multiplicando y separo por el simbolo "*"
    for mult in mult_raw:
        sep_mult = mult.split("*")
        num1 = int(sep_mult[0])
        num2 = int(sep_mult[1])
        
        result = num1 * num2
    #Agrego a la lista los resultados de las multiplicaciones que estan en la expresion
        mult_pre_results.append(result)
        
    #Sumo todo
    final_list = addends + mult_pre_results
    
    total = sum(final_list)
    
    print(f"El resultado de tu expresion es {total}")
 
solve(expr)
