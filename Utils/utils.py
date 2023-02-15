import os
import scipy.io.wavfile as wav
from scipy import signal
import numpy as np
from PySide2.QtWidgets import (QFileDialog)
from scipy.fft import fft
import yulewalker as yw

def getInitParameters(self):
    self.sliders = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    return self.sliders

def read_wav(filename):
    samplingRate, timeVector = wav.read(str(filename))    
    #timeVector = 2*(timeVector.astype(np.int16)/(2**16))
    timeVector = timeVector.astype(np.int16)
    return timeVector, samplingRate

def setMono(timeVector):
    shape = len(np.shape(timeVector))
    if shape >= 2:
        timeVector = timeVector[:,0]
    return timeVector

def thirdOctaveFilter(timeVector, samplingRate):
    centralFrequencies = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
    1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
    filterFactor = np.power(2,1/(6))
    lowerFrequencyBand = centralFrequencies/filterFactor
    upperFrequencyBand = centralFrequencies*filterFactor
    bandEnergy = np.empty([len(centralFrequencies), len(timeVector)])
    for n in range(len(centralFrequencies)):
        filter = signal.butter(N=6, Wn=np.array([lowerFrequencyBand[n], upperFrequencyBand[n]])/(samplingRate/2), 
                        btype='bandpass', analog=False, output='sos')
        bandEnergy[n] = signal.sosfiltfilt(filter, timeVector)
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
    

def applySliders(self, inputSignal, bandEnergy, linearSliderValues):
    '''Filter an input signal from the sliders curve inputed by the user
    Inputs: 
        inputSignal: input signal array in the time domain
        bandEnergy'''

    filterCorrection = sum(bandEnergy)-inputSignal
    bandEnergyFiltered = np.empty([len(self.sliders), len(inputSignal)])
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
    fC = 1.4    
    Yf = np.abs(fft(timeData))/N
    Yplot = fC*Yf[1:int(np.round(N/2+1))]
    f = samplingRate*(np.arange(1,N/2+1))/N   
    return f, 20*np.log10(Yplot/2e-5), Yplot

