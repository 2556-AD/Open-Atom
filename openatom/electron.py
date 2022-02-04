from openatom.particle import ParticulateMatter
from openatom.UNIVERSAL_CONSTANTS import *

class Electron(ParticulateMatter):
    def __init__(
                self,
                principalQuantumNumber,
                azimuthalQuantumNumber,
                magneticQuantumNumber,
                spinQuantumNumber,
                charge = ELECTRON_CHARGE,
                mass = ELECTRON_MASS, 
                velocity = VAL_TENDS_TO_ZERO,
                xCoordinate = 0, 
                yCoordinate = 0, 
                zCoordinate = 0
            ):

        super().__init__(
                charge = ELECTRON_CHARGE,
                mass = mass,
                velocity = velocity,
                xCoordinate = xCoordinate, 
                yCoordinate = yCoordinate, 
                zCoordinate = zCoordinate
            )
        self.charge = charge
        self.principalQuantumNumber = principalQuantumNumber
        self.azimuthalQuantumNumber = azimuthalQuantumNumber
        self.magneticQuantumNumber = magneticQuantumNumber
        self.spin = spinQuantumNumber

    def __str__(self):
        return 'electron at '+self.xCoordinate+','+self.yCoordinate+','+self.zCoordinate