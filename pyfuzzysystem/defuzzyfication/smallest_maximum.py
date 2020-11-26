from .utils import defuzzification_search

def smallest_maximum(fuzzy_set):
    '''
    Find the smallest element that has 
    maximum membership value
    '''
    return defuzzification_search(fuzzy_set, lambda x, y: x > y) 