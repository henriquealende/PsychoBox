import numpy as np
from mosqito.sq_metrics import sharpness_din_st
from Psychoacoustics.loudness_zwk import Loudness_ZWK

loud_zwk = Loudness_ZWK()

class Sharpnes_DIN():
    def __init__(self):
        super(Sharpnes_DIN, self).__init__()        
    
    def sharpnessCalculation(self, timeData, samplingRate):
        if len(timeData) > 0:
            self.globalSharpness = sharpness_din_st(timeData, samplingRate, weighting="din")
        else:
            self.globalSharpness = 0
            
    def specificSharpnessCalculation(self, timeData, samplingRate):        
    # Bark scale
        if len(timeData) > 0:
            Bark, _, sL = loud_zwk.loudnessCalculation(timeData, samplingRate)
            z = np.arange(1, 241) / 10

            # Small value to avoid divide-by-zero
            sm = np.sqrt(np.finfo(float).eps)  
            
            g = np.ones_like(z)
            g[z > 15.8] = 0.15 * np.exp(0.42 * (z[z > 15.8] - 15.8)) + 0.85
            g[158:208] *= np.linspace(1, 1.035, 50)
            g[209:] *= 1.035
            norm_cst = 0.10687977124128878

            # Sharpness Computation
            num = norm_cst * (g * z * sL) + sm
            specificSharpness = np.squeeze(num / (np.sum(sL) + sm))  # Remove axis specification
        else:
            specificSharpness = 0  
        return(Bark, specificSharpness)
              