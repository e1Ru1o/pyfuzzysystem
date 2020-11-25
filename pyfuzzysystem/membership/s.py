from .membership import Membership

class S(Membership):
    def __init__(self, a, c):
        assert a <= c, f"Params must hold a <= c"

        def s(x):
            if x <= a: return 0
            if x <= (a + c) / 2: 
                return 2 * ((x-a)/(c-a)) ** 2
            if x < c: 
                return 1 - 2 * ((c-x)/(c-a)) ** 2
            return 1

        super().__init__(s)
