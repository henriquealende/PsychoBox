from widget import *
import scipy.io.wavfile as wav
from scipy import signal
from scipy.signal.signaltools import wiener
import numpy as np

def getInitParameters(self):
    self.sliders = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    return self.sliders

def read_wav(filename):
    samplingRate, timeVector = wav.read(str(filename))
    #if timeVector.dtype == 'int16':
    #    timeVector = timeVector/(2**15)
    #elif timeVector.dtype == 'int32':
    #    timeVector = timeVector/(2**31)
    timeVector = timeVector.astype(np.int16)
    return timeVector, samplingRate

def setMono(timeVector):
    shape = len(np.shape(timeVector))
    if shape >= 2:
        timeVector = timeVector[:,0]
    return timeVector

def thirdOctaveFilter(self, timeVector, samplingRate):
    centralFrequencies = self.sliders    
    filterFactor = np.power(2,1/(6))
    lowerFrequencyBand = centralFrequencies/filterFactor
    upperFrequencyBand = centralFrequencies*filterFactor
    bandEnergy = np.empty([len(centralFrequencies), len(timeVector)])
    for n in range(len(centralFrequencies)):
        filter = signal.butter(N=4, Wn=np.array([lowerFrequencyBand[n], upperFrequencyBand[n]])/(samplingRate/2), 
                        btype='bandpass', analog=False, output='sos')
        bandEnergy[n] = signal.sosfiltfilt(filter, timeVector)
    return bandEnergy


def applySliders(self, timeVector, bandEnergy, linearSliderValues):
    print(linearSliderValues)
    filterCorrection = sum(bandEnergy)-timeVector
    bandEnergyFiltered = np.empty([len(self.sliders), len(timeVector)])
    for n in range(len(self.sliders)):
        bandEnergyFiltered[n] = (bandEnergy[n]*(linearSliderValues[n]))
    filteredSignal = sum(bandEnergyFiltered) - filterCorrection
    return filteredSignal.astype(np.int16)


def save_wav(self, timeVector, samplingRate):
    saveAdress = QFileDialog.getSaveFileName(self, 'Save File','', 'WAV files (*.wav)')
    savePathname = str(saveAdress[0])
    wav.write(savePathname, samplingRate, timeVector)
    savedFile = os.path.basename(str(savePathname))
    return savedFile


def timeReverberation(self, bandEnergy, samplingRate):
    from scipy.misc import face
