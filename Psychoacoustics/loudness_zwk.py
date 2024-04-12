import numpy as np

from mosqito.sq_metrics import loudness_zwst
class Loudness_ZWK():
    def __init__(self):
        super(Loudness_ZWK, self).__init__()         

        
        
    def loudnessCalculation(self, timeData, samplingRate):
        shape = len(np.shape(timeData))
        if shape >= 2:
            timeData = timeData[:,0] 
        if len(timeData) > 0:
            globalLoudness, specificLoudness, Bark = loudness_zwst(timeData, samplingRate, field_type="free")
        else:
            specificLoudness = 0
            globalLoudness = 0
            
        return (Bark, globalLoudness, specificLoudness)