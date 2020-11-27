class Rule:
    '''
    Class for represent fuzzy 
    inference systems rules
    '''
    def __init__(self, linguistic, aggregate=None):
        self.linguistic = linguistic
        antecedent, *consequences = linguistic
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
