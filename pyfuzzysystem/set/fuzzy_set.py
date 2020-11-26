from ..membership import Membership

class FuzzySet:
    '''
    Class for represent fuzzy set
    '''
    def __init__(self, name, membership, aggregation=max):
        self.name       = name
        self.membership = membership
        self.aggregation = aggregation

    def __add__(self, other):
        if not isinstance(other, FuzzySet):
            raise TypeError(f"unsupported operand type(s) for +: 'FuzzySet' and '{other.__class__.__name__}'")

        name     = f"({self.name}_U_{other.name})"
        function = lambda x: self.aggregation(self.membership(x), other.membership(x))
        points   = self.membership.points + other.membership.points
        points.sort()
        return FuzzySet(name, Membership(function, points), self.aggregation)
    
    def domain(self, **domain_args):
        return self.membership.domain(**domain_args)

    def __iter__(self):
        return iter(self.membership)

    def __str__(self):
        return self.name
        