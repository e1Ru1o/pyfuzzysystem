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

        name       = f"{self.name}_U_{other.name}"
        membership = lambda x: self.aggregation(self.membership(x), other.membership(x))
        return FuzzySet(name, Membership(f), self.aggregation)
    
    def domain(self, *domain_args):
        return self.membership.domain(*domain_args)

    def __iter__(self):
        return iter(self.membership)

    def __str__(self):
        return self.name
        