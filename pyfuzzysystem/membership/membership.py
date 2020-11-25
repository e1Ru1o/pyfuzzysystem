from numpy import arange

class Membership:
    '''
    Class for represent the membership
    function of a fuzzy set
    '''
    def __init__(self, function, points):
        self.func   = function 
        self.points = points

    def __call__(self, x):
        return self.func(x)

    def domain(self, step=0.05):
        d = list(arange(self.points[0], self.points[-1], step))
        d.extend(self.points)
        d.sort()
        return d

    def __iter__(self):
        return iter(self.domain())
