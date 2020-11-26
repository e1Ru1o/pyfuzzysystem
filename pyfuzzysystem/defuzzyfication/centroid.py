def centroid(fuzzy_set):
    '''
    Find the element that represent 
    the fuzzy set center
    '''
    num, den = 0, 0
    for x in fuzzy_set:
        value = fuzzy_set.membership(x)
        num += x * value
        den += value
    return num / den  
