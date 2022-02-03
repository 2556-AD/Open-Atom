from UNIVERSAL_CONSTANTS import *
from particle import ParticulateMatter

class Proton(ParticulateMatter):
    def __init__(
            self, 
            charge = PROTON_CHARGE,
            mass = PROTON_MASS, 
            velocity = 1, 
            xCoordinate = 0, 
            yCoordinate = 0, 
            zCoordinate = 0
        ):
        
        super().__init__(
            charge, 
            mass, 
            velocity, 
            xCoordinate, 
            yCoordinate, 
            zCoordinate
        )