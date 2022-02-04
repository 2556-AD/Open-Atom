from openatom.UNIVERSAL_CONSTANTS import *
from openatom.particle import ParticulateMatter

class Neutron(ParticulateMatter):
    def __init__(
            self, 
            charge = NEUTRON_CHARGE,
            mass = NEUTRON_MASS, 
            velocity = VAL_TENDS_TO_ZERO, 
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