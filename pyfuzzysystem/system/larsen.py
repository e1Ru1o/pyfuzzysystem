from .system import InferenceSystem
from ..rule import LarsenRule

class LarsenSystem(InferenceSystem):
    '''
    Larsen Inference System
    '''
    def __init__(self, defuzzify):
        super().__init__(LarsenRule, defuzzify)
        