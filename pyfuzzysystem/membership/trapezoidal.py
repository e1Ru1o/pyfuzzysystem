from .membership import Membership

class Trapezoidal(Membership):
    def __init__(self, a, b, c, d):
        assert a <= b <= c <= d, f"Params must hold a <= b <= c <= d"

        def trapezoidal(x):
            if x <= a or x >= d: return 0
            if b <= x <= c: return 1
            if x < b: return (x-a)/(b-a)
            return (d-x)/(d-c)

        super().__init__(trapezoidal, [a, b, c, d])
