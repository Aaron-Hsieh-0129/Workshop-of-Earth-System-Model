import xarray as xr
import numpy as np

class TaiESM():
    def __init__(self, data):
        self.data = xr.open_dataset(data)
        
        self.LON = self.getVar("lon")
        self.LAT = self.getVar("lat")
        self.LON2, self.LAT2 = np.meshgrid(self.LON, self.LAT)
        # self.LEV_PRE = self.getLevPre()
    
    def getVar(self, var):
        if type(var) == str:
            return self.data[var].to_numpy()
        elif type(var) == list or type(var) == np.ndarray:
            retVal = []
            for i in range(len(var)):
                retVal.append(self.data[var[i]].to_numpy())
            return retVal
        
    def getLevPre(self):
        PS_tile = np.tile(self.getVar("PS"), (30, 1, 1))
        hybm_tile = np.tile(self.getVar("hybm"), (192, 288, 1)).swapaxes(0, 2).swapaxes(1, 2)
        PRS_lev = np.tile(self.getVar("P0")*self.getVar("hybm"), (192, 288, 1)).swapaxes(0, 2).swapaxes(1, 2) + PS_tile * hybm_tile
        return PRS_lev