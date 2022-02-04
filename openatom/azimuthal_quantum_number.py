from openatom.UNIVERSAL_CONSTANTS import *

class AzimuthalQNum:
    def __init__(self, subshellIdx):
        self.azimuthalQuantumNumVal = subshellIdx
        self.orbitalArray = []
        self.orbitalArray = [MagneticQNum(orbitalIdx) for orbitalIdx in range(-self.azimuthalQuantumNumVal, 2*self.azimuthalQuantumNumVal+1)]