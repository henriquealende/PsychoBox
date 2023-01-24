import os
import scipy.io.wavfile as wav
from scipy import signal
from scipy.signal.signaltools import wiener
import numpy as np
from PySide2.QtWidgets import (QFileDialog)
from scipy.fft import fft, fftfreq, fftshift


def getInitParameters(self):
    self.sliders = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    return self.sliders

def read_wav(filename):
    samplingRate, timeVector = wav.read(str(filename))
    timeVector = 2*(timeVector.astype(np.int16)/(2**16))
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

def getFFT(timeData, samplingRate):
    N = len(timeData)
    xf = fftfreq(N, 1/samplingRate)
    xf = fftshift(xf)
    yf = fft(timeData) 
    
    yplot= fftshift(yf)
    y = 1.0/N * np.abs(yplot)
    print(int(np.round(len(timeData)/2+1)))
    return xf[int(np.round(len(timeData)/2+1)):len(timeData)], 20*np.log10(y[int(np.round(len(timeData)/2+1)):len(timeData)]/2e-5)

def timeReverberation(self, bandEnergy, samplingRate):
    pass
