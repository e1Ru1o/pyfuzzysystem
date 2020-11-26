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
        output = {}
        for rule in self.rules:
            for key, set in rule(input).items():
                try: output[key] += set
                except KeyError: output[key] = set
        return {key:self.defuzzify(set) for key, set in output.items()}

    def __add__(self, linguistic):
        self.add_rule(self.rule_class(linguistic))
        return self
    