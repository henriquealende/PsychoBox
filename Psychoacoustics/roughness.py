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
            globalRoughness, specificRoughness, Bark,_ = roughness_dw(timeData, samplingRate)
        else:
            specificRoughness = 0
            globalRoughness = 0
                   
        return (Bark, globalRoughness, specificRoughness)
            
    def roughnessECMA(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalLoudness, _, specificLoudness, Bark, _= roughness_ecma(timeData, samplingRate)
        else:
            specificLoudness = 0
            globalLoudness = 0
            
        return (Bark, globalLoudness, specificLoudness)