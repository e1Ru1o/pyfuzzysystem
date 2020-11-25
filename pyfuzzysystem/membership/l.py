from .membership import Membership

class L(Membership):
    def __init__(self, a, m):
        assert a <= m, f"Params must hold a <= m"

        def l(x):
            if x <= a: return 1
            if x < m: return (m-x)/(x-a)
            return 0

        super().__init__(l, [a, m])
