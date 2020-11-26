from .linguistic import LinguisticVar

class FuzzyFormal(LinguisticVar):
    '''
    Linguistic variable attached 
    to a fuzzy variable set
    '''
    def __init__(self, fuzzy_var_name, fuzyy_set, *linguistic_args):
        super().__init__(*linguistic_args)
        self.name = fuzzy_var_name
        self.set  = fuzyy_set

    def __call__(self, input):
        return self.set.membership(input[self.name])

    def __str__(self):
        return f'{self.name}:{self.set}'
