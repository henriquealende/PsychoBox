import numpy as np

from mosqito.sq_metrics import roughness_dw
from mosqito.sq_metrics import roughness_ecma
class Roughness():
    def __init__(self):
        super(Roughness, self).__init__()         

        
        
    def roughnessDW(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalRoughness, specificRoughness, Bark,_ = roughness_dw(timeData, samplingRate, overlap = 0)
            globalRoughness = np.mean(globalRoughness)
            specificRoughness = np.sum(specificRoughness, axis = 1)
        else:
            specificRoughness = 0
            globalRoughness = 0
                   
        return (Bark, globalRoughness, specificRoughness)
            
    def roughnessECMA(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalRoughness, _, specificRoughness, Bark, _= roughness_ecma(timeData, samplingRate)
        else:
            specificRoughness = 0
            globalRoughness = 0
            
        return (Bark, globalRoughness, specificRoughness)