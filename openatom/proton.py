from openatom.UNIVERSAL_CONSTANTS import *
from openatom.particle import ParticulateMatter

class Proton(ParticulateMatter):
    def __init__(
            self, 
            charge = PROTON_CHARGE,
            mass = PROTON_MASS, 
            velocity = VAL_TENDS_TO_ZERO, 
            xCoordinate = 0, 
            yCoordinate = 0, 
            zCoordinate = 0
        ):
        
        super().__init__(
            charge = charge, 
            mass = mass, 
            velocity = velocity, 
            xCoordinate = xCoordinate, 
            yCoordinate = yCoordinate, 
            zCoordinate = zCoordinate
        )