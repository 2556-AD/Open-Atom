class electron:
    def __init__(self):
        self.charge = -1.6022e-19
        self.mass = 9.109e-31

class proton:
    def __init__(self):
        self.charge = 1.6022e-19
        self.mass = 1.672e-27

class neutron:
    def __init__(self):
        self.charge = 0
        self.mass = 1.675e-27

class atom:
    def __init__(self, protonCount, neutronCount, electronCount):
        self.protons = [proton() for p in range(protonCount)]
        self.electrons = [electron() for e in range(electronCount)]
        self.neutrons = [neutron() for n in range(neutronCount)]
    
    # def probeAtom(self):
    #     print(self.protons)
    
# temp = electronCount 5,3
# counter =1      2
# shell = [2,3]
# while temp>0:
#   as = 2**counter   2,4
#   if(temp>=as):
#       shell.append(as)
#   else:
#       shell.append(temp)
#   temp -= as
#   counter += 1
