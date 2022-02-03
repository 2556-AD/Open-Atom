from UNIVERSAL_CONSTANTS import PLANCKS_CONSTANT as h

class ParticulateMatter:
    def __init__(self, charge, mass, velocity, xCoordinate, yCoordinate, zCoordinate):
        self.charge = charge
        self.mass = mass
        self.velocity = velocity
        self.momentum = mass * velocity
        self.wavelength = h / self.momentum
        
        # location vector
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.zCoordinate = zCoordinate