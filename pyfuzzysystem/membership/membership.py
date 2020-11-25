class Membership:
    '''
    Class for represent the membership
    function of a fuzzy set
    '''
    def __init__(self, function):
        self.func = function 

    def __call__(self, x):
        return self.func(x)
