from ..set import FuzzySet

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
        if key not in self.sets:
            raise KeyError(f"Set `{key}` not found in Var `{self.name}`")
        return self.sets[key]

    def __str__(self):
        return self.name
