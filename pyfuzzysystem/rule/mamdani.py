from .rule import Rule
from ..set import FuzzySet
from ..membership import Membership

class MamdaniRule(Rule):
    def __init__(self, linguistic):
        def mamdani(set, value):
            f = lambda x: min(set.membership(x), value)
            membership = Membership(f, set.membership.points)
            return FuzzySet(f'truncated_{set}', membership, set.aggregation)
        super().__init__(linguistic, mamdani)
        