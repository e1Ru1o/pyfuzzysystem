from ..variable import LinguisticStatement, LinguisticVar

class Rule:
    '''
    Class for represent fuzzy 
    inference systems rules
    '''
    def __init__(self, linguistic, aggregate=None):

        if not isinstance(linguistic, LinguisticStatement):
            raise TypeError(f"`{linguistic.__class__.__name__} is not a valid LinguisticStatement")
        if not all(isinstance(x, LinguisticVar) for x in linguistic):
            raise TypeError('Malformed LinguisticStatement. Antecedent and consequences must be of type LinguisticVar')

        antecedent, *consequences = linguistic
        self.linguistic = linguistic
        self.consequences = consequences
        self.antecedent   = antecedent
        self.aggregation(aggregate)

    def aggregation(self, aggregate):
        self.aggregate = aggregate

    def __call__(self, input):
        value = self.antecedent(input)
        return {c.name:self.aggregate(c.set, value) for c in self.consequences}

    def __str__(self):
        return str(self.linguistic)
