from .membership import Membership

class Gamma(Membership):
    def __init__(self, a, m):
        assert a <= m, f"Params must hold a < m"

        def gamma(x):
            if x <= a: return 0
            if x < m: return (x-a)/(m-a)
            return 1

        super().__init__(gamma, [a, m])
