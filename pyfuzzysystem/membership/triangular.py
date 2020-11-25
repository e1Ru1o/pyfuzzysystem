from .membership import Membership

class Triangular(Membership):
    def __init__(self, a, m, b):
        assert a <= m <= b, f"Params must hold a <= m <= b"

        def triangular(x):
            if x <= a or x >= b: return 0
            if x <= m: return (x-a)/(m-a)
            return (b-x)/(b-m)

        super().__init__(triangular)
