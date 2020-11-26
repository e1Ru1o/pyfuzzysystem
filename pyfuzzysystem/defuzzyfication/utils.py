def defuzzification_search(fuzzy_set, selector):
    '''
    Select the best element of 
    the fuzzy set using the given
    selector function
    '''
    best, selected = -1, None
    for x in fuzzy_set:
        value = fuzzy_set.membership(x)
        if selector(value, best):
            best, selected = value, x
    return selected 