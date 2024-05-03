import numpy as np

from mosqito.sq_metrics import loudness_zwst
from mosqito.sq_metrics import loudness_ecma
class Loudness():
    def __init__(self):
        super(Loudness, self).__init__()         

        
        
    def loudnessZWK(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalLoudness, specificLoudness, Bark = loudness_zwst(timeData, samplingRate, field_type="free")
        else:
            specificLoudness = 0
            globalLoudness = 0
                   
        return (Bark, globalLoudness, specificLoudness)
            
    def loudnessECMA(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalLoudness, _, specificLoudness, Bark, _= loudness_ecma(timeData, samplingRate)
        else:
            specificLoudness = 0
            #globalLoudness = 0
            
        return (Bark, globalLoudness, specificLoudness)