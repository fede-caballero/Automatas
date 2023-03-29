expr1 = str(input("Enter the expression to solve: "))

def solve(expr):
    terms = expr.split("+")
    addends = []
    multiples = []
    mult_sep = []
    prod_tot = []
    sum_list = []
    
    for term in terms:
        if term.isdigit():
            int_term = int(term)
            addends.append(int_term)
        else:
            multiples.append(term)
    
    if len(multiples) == 1:
        sep_mult = mult.split("*")
        mult_sep.append(sep_mult)
    
    elif len(multiples) > 1:
        for mult in multiples:
            groups = [int(x) for x in mult.split("*")]
            mult_sep.append(groups)
    
    for sub in mult_sep:
        product = sub[0] * sub[1]
        prod_tot.append(product)
        
    sum_list = addends + prod_tot
    
    total = sum(sum_list)
    
    print(f"El resultado a tu expresion es: {total}")

solve(expr1)
