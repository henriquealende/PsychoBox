import os
import scipy.io.wavfile as wav
from scipy import signal
import numpy as np
from PySide2.QtWidgets import (QFileDialog)
from scipy.fft import fft

def getInitParameters(self):
    self.sliders = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    return self.sliders

def getAudio(filename):
    samplingRate, audioData = wav.read(str(filename))    
    audioData = audioData.astype(np.int16)
    return audioData, samplingRate

def setMono(timeData):
    shape = len(np.shape(timeData))
    if shape >= 2:
        timeData = timeData[:,0]
    return timeData

def applyOctaveFilter(self):
    centralFrequencies = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    filterFactor = np.power(2,1/(6))
    lowerFrequencyBand = centralFrequencies/filterFactor
    upperFrequencyBand = centralFrequencies*filterFactor
    bandEnergy = np.empty([len(centralFrequencies), len(self.timeData)])
    for n in range(len(centralFrequencies)):
        filter = signal.butter(N=6, Wn=np.array([lowerFrequencyBand[n], upperFrequencyBand[n]])/(self.samplingRate/2), 
                        btype='bandpass', analog=False, output='sos')
        bandEnergy[n] = signal.sosfiltfilt(filter, self.timeData)
    return bandEnergy

def getBandValue(freqData, samplingRate):
    N = len(freqData)
    centralFrequencies = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    filterFactor =  np.power(2,1/(6))
    upperFrequencies = centralFrequencies*filterFactor
    lowerFrequencies = centralFrequencies/filterFactor
    upperLoc = np.round((N/samplingRate)*upperFrequencies)
    lowerLoc = np.round((N/samplingRate)*lowerFrequencies)
    matrix = np.zeros([len(centralFrequencies), len(freqData)])
  
    for n in range(len(centralFrequencies)):
        matrix[n, int(lowerLoc[n]): int(upperLoc[n])] = freqData[int(lowerLoc[n]):int(upperLoc[n])]
    # for n in range(len(centralFrequencies)):
    #      matrix[n, lowerLoc[n]:upperLoc[n]] = 1 #freqData[lowerLoc[n]:upperLoc[n]]
    fCorrection = 4*(N/samplingRate)
    matrixSum = np.sum(matrix, axis=1)/fCorrection
    return matrixSum
    

def applySliders(self, linearSliderValues):
    '''Filter an input signal from the sliders curve inputed by the user
    Inputs: 
        inputSignal: input signal array in the time domain
        bandEnergy'''
    filterCorrection = sum(self.bandEnergy)-self.timeData
    bandEnergyFiltered = np.empty([len(self.sliders), len(self.timeData)])
    for n in range(len(self.sliders)):
        bandEnergyFiltered[n] = (self.bandEnergy[n]*(linearSliderValues[n]))
    filteredSignal = sum(bandEnergyFiltered) - filterCorrection
    return filteredSignal.astype(np.int16)

def saveAudio(self, timeData, samplingRate):
    saveAdress = QFileDialog.getSaveFileName(self, 'Save File','', 'WAV files (*.wav)')
    savePathname = str(saveAdress[0])
    wav.write(savePathname, samplingRate, timeData)
    savedFile = os.path.basename(str(savePathname))
    return savedFile

def getFFT(timeData, samplingRate):
    N = len(timeData)
    fC = 1.4    
    Yf = np.abs(fft(timeData))/N
    Yplot = fC*Yf[1:int(np.round(N/2+1))]
    f = samplingRate*(np.arange(1,N/2+1))/N   
    return f, 20*np.log10(Yplot/2e-5), Yplot