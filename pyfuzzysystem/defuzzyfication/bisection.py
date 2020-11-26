def bisection(fuzzy_set):
    '''
    Find the element that split the fuzzy set
    into two equal area parts
    '''
    domain = list(fuzzy_set)
    values = [fuzzy_set.membership(domain[0])]

    for x in domain[1:]:
        values.append(fuzzy_set.membership(value) + sums[-1])
    for i, x in enumerate(domain):
        if values[i] >= values[-1] / 2:
            return x   
