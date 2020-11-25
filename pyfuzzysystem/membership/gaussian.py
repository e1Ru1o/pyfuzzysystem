from .membership import Membership
from .s import S
from .z import Z

class Gaussian(Membership):
    def __init__(self, b, d):
        s = S(b - d, b)
        z = Z(b, b + d)
        
        def gaussian(x):
            if x <= b: return s(x)
            return z(x)

        super().__init__(gaussian, [b - d, b, b + d])
