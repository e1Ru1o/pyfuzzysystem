from ..membership import Membership

class FuzzySet:
    '''
    Class for represent fuzzy set
    '''
    def __init__(self, name, membership, agregation=max):
        self.name       = name
        self.membership = membership
        self.agregation = agregation

    def __add__(self, other):
        if not isinstance(other, FuzzySet):
            raise TypeError(f"unsupported operand type(s) for +: 'FuzzySet' and '{other.__class__.__name__}'")

        name       = f"{self.name}_U_{other.name}"
        membership = lambda x: self.agregation(self.membership(x), other.membership(x))
        return FuzzySet(name, Membership(f), self.agregation)
    