from ..set import FuzzySet
from .formal import FuzzyFormal

class FuzzyVariable:
    '''
    Class for represent fuzzy variables 
    '''
    def __init__(self, name):
        self.name = name
        self.sets = {}

    def add(self, *set_args):
        '''
        Add ( and create ) a new fuzzy set 
        '''
        fset = FuzzySet(*set_args)
        self.sets[fset.name] = fset
        return self

    def __getitem__(self, key):
        '''
        Return a fuzzy formal representing 
        the variable set named key
        '''
        if key not in self.sets:
            raise KeyError(f"Set `{key}` not found in Var `{self.name}`")
        return FuzzyFormal(self.name, self.sets[key])

    def __str__(self):
        return self.name
