from .system import InferenceSystem
from ..rule import MamdaniRule

class MamdaniSystem(InferenceSystem):
    '''
    Mamdani Inference System
    '''
    def __init__(self, defuzzify):
        super().__init__(MamdaniRule, defuzzify)
        