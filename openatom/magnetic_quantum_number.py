from openatom.UNIVERSAL_CONSTANTS import *
from openatom.electron import Electron

class MagneticQNum:
    def __init__(self, orbitalIdx):
        self.magneticQuantumNumVal = orbitalIdx
        self.electronArray = []
    
    def fillElectron(
            self,
            principalQuantumNumber,
            azimuthalQuantumNumber,
            magneticQuantumNumber,
            xCoordinate = 0, 
            yCoordinate = 0, 
            zCoordinate = 0
        ): # ): fyl des
        if len(self.electronArray) == 0:
            return Electron(
                principalQuantumNumber = principalQuantumNumber,
                azimuthalQuantumNumber = azimuthalQuantumNumber,
                magneticQuantumNumber = magneticQuantumNumber,
                spinQuantumNumber = 0.5, # +1/2
                xCoordinate = xCoordinate,
                yCoordinate = yCoordinate,
                zCoordinate = zCoordinate
            )
        elif len(self.electronArray) == 1:
            return Electron(
                principalQuantumNumber = principalQuantumNumber,
                azimuthalQuantumNumber = azimuthalQuantumNumber,
                magneticQuantumNumber = magneticQuantumNumber,
                spinQuantumNumber = -0.5, # -1/2
                xCoordinate = xCoordinate,
                yCoordinate = yCoordinate,
                zCoordinate = zCoordinate
            )