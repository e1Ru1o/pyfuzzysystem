from .membership import Membership

class Z(Membership):
    def __init__(self, a, c):
        assert a <= c, f"Params must hold a <= c"

        def z(x):
            if x <= a: return 1
            if x <= (a + c) / 2: 
                return 1 - 2 * ((x-a)/(c-a)) ** 2
            if x < c: 
                return 2 * ((c-x)/(c-a)) ** 2
            return 0

        super().__init__(z)
