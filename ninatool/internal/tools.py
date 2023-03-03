from scipy.constants import pi, h, elementary_charge

Phi0 = h / (2 * elementary_charge)

class unitsConverter(object):
    
    def __init__(self):
        
        self.__current_units = 1e-6    
    
    @property
    def current_units(self):
        return(self.__current_units)
    
    @property
    def inductance_units(self):
        return(Phi0 / (2 * pi * self.current_units))
    
    @property
    def energy_units(self):
        return(Phi0  * self.current_units / (2 * pi))
    
    @property
    def capacitance_units(self):
        return(pi * elementary_charge ** 2 / (Phi0 * self.current_units))
    
    @property
    def frequency_units(self):
        return(self.energy_units / h)
    
    @current_units.setter
    def current_units(self, value):
        self.__current_units = value