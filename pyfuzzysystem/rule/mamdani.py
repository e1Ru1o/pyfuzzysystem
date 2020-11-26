from .rule import Rule
from ..set import FuzzySet
from ..membership import Membership

class MamdaniRule(Rule):
    def aggregate(self, set, value):
        f = lambda x: min(set.membership(x), value)
        membership = Membership(f, set.membership.points)
        return FuzzySet(f'truncated_{set}', membership, set.aggregation)
        