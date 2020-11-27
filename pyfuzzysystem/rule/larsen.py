from .rule import Rule
from ..set import FuzzySet
from ..membership import Membership

class LarsenRule(Rule):
    def __init__(self, linguistic):
        def larsen(set, value):
            f = lambda x: set.membership(x) * value
            membership = Membership(f, set.membership.points)
            return FuzzySet(f'scaled_{set}', membership, set.aggregation)
        super().__init__(linguistic, larsen)
        