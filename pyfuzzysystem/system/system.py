from ..rule import Rule
from ..variable import LinguisticStatement

class InferenceSystem:
    '''
    Class for represent fuzzy 
    inference systems
    '''
    def __init__(self, rule, defuzzify):
        if not issubclass(rule, Rule):
            raise TypeError(f"{rule} is not a Rule class")
        self.rules      = []
        self.rule_class = rule
        self.defuzzification(defuzzify)

    def add_rule(self, rule):
        if not isinstance(rule, Rule):
            raise TypeError(f"`{rule.__class__.__name__} is not a valid Rule")
        self.rules.append(rule)

    def defuzzification(self, defuzzify):
        self.defuzzify = defuzzify
    
    def infer(self, input):
        if not isinstance(input, dict):
            raise TypeError(f"Infer `input` param must be a dict object")
        output = {}
        for rule in self.rules:
            for key, set in rule(input).items():
                try: output[key] += set
                except KeyError: output[key] = set
        return {key:self.defuzzify(set) for key, set in output.items()}

    def __add__(self, linguistic):
        self.add_rule(self.rule_class(linguistic))
        return self
    
    def __str__(self):
        rules = '\n'.join(str(r) for r in self.rules)
        return f"Rules:\n{rules}"
