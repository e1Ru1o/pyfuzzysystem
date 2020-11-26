from collections import defaultdict

class InferenceSystem:
    '''
    Class for represent fuzzy 
    inference systems
    '''
    def __init__(self, rule, defuzzify):
        self.rules      = []
        self.rule_class = rule
        self.defuzzification(defuzzify)

    def add_rule(self, rule):
        self.rules.append(rule)

    def defuzzification(self, defuzzify):
        self.defuzzify = defuzzify
    
    def infer(self, input):
        output = self.rules[0](input)
        for rule in self.rules[1:]:
            for key, set in rule(input).items():
                output[key] += set
        return {key:self.defuzzify(set) for key, set in output}

    def __add__(self, linguistic):
        self.add_rule(self.rule_class(linguistic))
    