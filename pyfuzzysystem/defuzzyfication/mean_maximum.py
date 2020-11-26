def mean_maximum(fuzzy_set):
    '''
    Find the mean of the elements with
    maximum membership value
    '''
    top, values = -1, None
    for x in fuzzy_set:
        value = fuzzy_set.membership(x)
        if value > top:
            top, values = value, []
        if value == top:
            values.append(x)
    return sum(values) / len(values)