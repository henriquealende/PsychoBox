from scipy.io import loadmat
import numpy as np
from scipy.signal import fftconvolve, resample
import warnings

class Calibration():
    def __init__(self, ui=None):
        super(Calibration, self).__init__()

    def equalizeSignal(self, timeSignal=np.array([1, 0, 0, 0, 0]),
                       samplingRate=44100,
                       hats='HMSIII.2',
                       audioInterface='UCA222',
                       headPhone='HD58X'):
        '''
        Equalize a signal to playback in a headphone. The filter is load from a database
        according with the specified HATS, audio interface and headphone specification.
        '''

        # Carregando e tratando o filtro de audio:
        filename = 'eq_' + hats + '_' + audioInterface + '_' + headPhone + '.mat'
        try:
            filterData = loadmat("binauralTreatment//" + filename)
        except:
            warnings.warn("I cant find the specified HATS-audiointerface-headphones combination.", UserWarning)
            return None

        if samplingRate != filterData['samplingRate']:
            num_samples = int(len(timeSignal) * filterData['samplingRate'] / samplingRate)
            timeSignal = resample(timeSignal, num_samples)

        # tratando o sinal de audio:
        nChannels = timeSignal.ndim
        if nChannels == 1:
            warnings.warn("It is expected a binaural signal here. Becareful tu avoid stranger data!", UserWarning)
            eqSignal = np.vstack((
                fftconvolve(timeSignal, filterData['hcorrLeftMF'].flatten()),
                fftconvolve(timeSignal, filterData['hcorrRightMF'].flatten())
            )).transpose()
        if nChannels == 2:
            eqSignal = np.vstack((
                fftconvolve(timeSignal[:, 0], filterData['hcorrLeftMF'].flatten()),
                fftconvolve(timeSignal[:, 1], filterData['hcorrRightMF'].flatten())
            )).transpose()

        return eqSignal

    def applyHRIR(self, micSignal=np.array([1, 0, 0, 0, 0]),
                  samplingRate=44100,
                  hats="HMSIII.2"):

        try:
            hrir = loadmat("binauralTreatment\\hrir" + hats + ".mat")
        except:
            warnings.warn("I cant find the specified head related impulse reponse.", UserWarning)
            return None

        if samplingRate != hrir['samplingRate']:
            num_samples = int(len(micSignal) * hrir['samplingRate'] / samplingRate)
            micSignal = resample(micSignal, num_samples)

        binauralAudio = np.vstack((
            fftconvolve(micSignal, hrir['hrirLeft'].flatten()),
            fftconvolve(micSignal, hrir['hrirRight'].flatten())
        )).transpose()
        return binauralAudio

if __name__ == "__main__":
    cal = Calibration()
    binauralAudio = cal.applyHRIR(hats='HMSIII.2')
    print()
