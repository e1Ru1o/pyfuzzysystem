class LinguisticVar:
    '''
    Class for support fuzzy propositions
    '''
    def __init__(self, union=max, intersection=min):
        self.intersect(intersection)
        self.join(union)

    def join(self, union):
        self.union = union
        return self

    def intersect(self, intersection):
        self.intersection = intersection
        return self

    def __and__(self, other):
        if not isinstance(other, LinguisticVar):
            raise ValueError(f'Unsoported operand (+) for LinguisticVar and `{other.__class__.__name__}`')
        return AndLinguisticVar(self, other, self.union, self.intersection)

    def __or__(self, other):
        if not isinstance(other, LinguisticVar):
            raise ValueError(f'Unsoported operand (+) for LinguisticVar and `{other.__class__.__name__}`')
        return OrLinguisticVar(self, other, self.union, self.intersection)

    def __invert__(self):
        return NotLinguisticVar(self, self.union, self.intersection)

    def __rshift__(self, other):
        if not isinstance(other, LinguisticStatement):
            raise ValueError(f'Unsoported operand (>>) for LinguisticVar and `{other.__class__.__name__}`')
        return LinguisticStatement(self, other.consequences)

    def __pos__(self):
        return LinguisticStatement(None, [self])

class LinguisticStatement:
    '''
    Class for represent an antecedent,
    consequences pair
    '''
    def __init__(self, antecedent, consequences):
        self.antecedent   = antecedent
        self.consequences = consequences
    
    def __add__(self, other):
        if not isinstance(other, LinguisticStatement):
            raise ValueError(f'Unsoported operand (+) for LinguisticStatement and `{other.__class__.__name__}`')
        self.consequences.append(other)
        return self

    def __iter__(self):
        return iter([self.antecedent, *self.consequences])

    def __str__(self):
        return f"{self.antecedent} => {', '.join(str(x) for x in self.consequences)}"

class BinaryLinguisticVar(LinguisticVar):
    '''
    Base class for AND and OR proposition operations
    '''
    def __init__(self, left, right, *linguistic_args):
        super().__init__(*linguistic_args)
        self.left  = left
        self.right = right

class AndLinguisticVar(BinaryLinguisticVar):
    '''
    AND porposition operation
    '''
    def __call__(self, *args, **kwargs):
        left  = self.left(*args, **kwargs)
        right = self.right(*args, **kwargs)
        return self.intersection(left, right)

    def __str__(self):
        return f"({self.left} and {self.right})"

class OrLinguisticVar(BinaryLinguisticVar):
    '''
    OR porposition operation
    '''
    def __call__(self, *args, **kwargs):
        left  = self.left(*args, **kwargs)
        right = self.right(*args, **kwargs)
        return self.union(left, right)

    def __str__(self):
        return f"({self.left} or {self.right})"

class NotLinguisticVar(LinguisticVar):
    '''
    NOT proposition operator
    '''
    def __init__(self, var, *linguistic_args):
        super().__init__(*linguistic_args)
        self.var = var

    def __call__(self, *args, **kwargs):
        return 1 - self.var(*args, **kwargs)

    def __str__(self):
        return f"(not {self.var})"
