from openatom.UNIVERSAL_CONSTANTS import *
from openatom.azimuthal_quantum_number import AzimuthalQNum

class PrincipalQNum():
    def __init__(self, shellIdx):
        self.label = self.assignShellLabel(shellIdx)
        self.principalQuantumNumVal = shellIdx + 1
        self.azimuthalArray = []
        self.azimuthalArray = [AzimuthalQNum(len(self.azimuthalArray)) for i in range(self.principalQuantumNumVal)]
    
    # shellArray.append(PrincipalQNum(len(shellArray)))
    def assignShellLabel(self, shellIdx):
        shellMap = {
            0 : 'K',
            1 : 'L',
            2 : 'M',
            3 : 'N',
            4 : 'O',
            5 : 'P'
        }
        return shellMap[shellIdx]