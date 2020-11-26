from .rule import Rule
from ..set import FuzzySet
from ..membership import Membership

class LarsenRule(Rule):
    def aggregate(self, set, value):
        f = lambda x: set.membership(x) * value
        membership = Membership(f, set.membership.points)
        return FuzzySet(f'scaled_{set.name}', membership, set.aggregation)
        