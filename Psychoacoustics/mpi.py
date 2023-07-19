import numpy as np
import scipy.io.wavfile as wav
from scipy import signal

#from scipy.signal.signaltools import wiener
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.size'] = 16

class MPI():
    def __init__(self):
        super(MPI, self).__init__()
    def calculateMPI(self, filename, plot_A, plot_B):
        bandEnergy = self._applyFilter(filename)
        prominence = np.empty(21)
        for n in range(len(self.centralFrequencies)):
            self._impulseParameters(bandEnergy[n], False)
            prominence[n] = self.P
            
                    
        self._weightingFunction(False)        
        
        indexes = np.array([0, 6, 13, 21, 31, 44, 61, 81, 107, 141, 181, 231,
                            301, 381, 481, 611, 781, 981, 1241, 1581, 1980])
        weighting_mpi = self.weighting[indexes]
        MPI_value = prominence + weighting_mpi
        Bark = np.linspace(0.9867, 21.7292, 21)

        # MPI_total = np.sum(10.^ (MPI_value/10))
        if plot_A:
            _, ax = plt.subplots()  

            ax.axvspan(Bark[0], len(Bark), ymin = 0, ymax = 0.5, facecolor='red', alpha=0.2)
            ax.axvspan(Bark[0], len(Bark), 0.5, 1, facecolor='green', alpha=0.2)
            
            ax.plot(Bark, MPI_value, color='blue', linewidth=1, zorder=10)
            
            ax.set_ylim(0,10)
            ax.set_ylabel('MPI [dB]')
            ax.set_xlabel('Frequency [Bark]')
            ax.grid(True)
            
            plt.show()
            
        if plot_B:
            _, ax = plt.subplots()  
            ax.plot(Bark, prominence, color='blue', linewidth=1, zorder=10)   
            ax.set_ylim(0,10)
            ax.set_ylabel('Prominence Ratio [dB]')
            ax.set_xlabel('Frequency [Bark]')
            ax.grid(True)
            plt.show()
            
    def _applyFilter(self, filename):
        self.samplingRate, timeData = wav.read(filename) # sampling rate of the audio file
        timeData = timeData.astype(np.int16) # time vector of the audio file
        timeData = timeData/32768 # normalize the data to float32 .wav format 
        self.timeVector = np.linspace(0,len(timeData)/self.samplingRate,len(timeData))
        self.centralFrequencies = np.array([100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
                                            1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
        filterFactor = np.power(2,1/(6))
        lowerFrequencyBand = self.centralFrequencies/filterFactor
        upperFrequencyBand = self.centralFrequencies*filterFactor        
        
        dimension = timeData.ndim
        
        if dimension > 1:
            self.bandEnergy = np.empty([dimension, len(self.centralFrequencies), len(timeData)])
            for m in range(dimension):
                for n in range(len(self.centralFrequencies)):
                    filter = signal.butter(N=6, Wn=np.array([lowerFrequencyBand[n], upperFrequencyBand[n]])/(self.samplingRate/2), 
                                    btype='bandpass', analog=False, output='sos')
                    self.bandEnergy[m,n] = signal.sosfiltfilt(filter, timeData[:,m])
        else:
            self.bandEnergy = np.empty([len(self.centralFrequencies), len(timeData)])
            for n in range(len(self.centralFrequencies)):                    
                    filter = signal.butter(N=6, Wn=np.array([lowerFrequencyBand[n], upperFrequencyBand[n]])/(self.samplingRate/2), 
                                    btype='bandpass', analog=False, output='sos')
                    self.bandEnergy[n] = signal.sosfiltfilt(filter, timeData)                
      
        
    

    # def _impulseParameters(self):
    #     time_event = 200/1000
    #     window_width = time_event*self.samplingRate        
        
    #     self.prominence = np.empty(len(self.centralFrequencies))
    #     for n in range(len(self.centralFrequencies)):             
            
    #         bandEnergySF = self.bandEnergy[n,:]
    #         std_signal = np.std(bandEnergySF)         
    #         min_prominence = 5 * std_signal
    #         peaks, _ = signal.find_peaks(bandEnergySF, prominence=min_prominence) 

    #         max_peak_value = np.max(bandEnergySF[peaks])            
    #         max_peak_idx = []
            
    #         for m in peaks:
    #             if bandEnergySF[m] == max_peak_value:
    #                 max_peak_idx = m           
    #         windowed_bandEnergy = bandEnergySF[int(max_peak_idx-window_width/2):int(max_peak_idx+window_width/2)]
    #         nps_windowed_bandEnergy = 20*np.log10(np.abs(windowed_bandEnergy/2e-5))       
            
            
    #         try:
    #             mean_window = np.mean(nps_windowed_bandEnergy)
    #             max_window = np.max(nps_windowed_bandEnergy)                
    #             OR = (max_window - mean_window)/(15*time_event)
    #             LDI = (max_window - mean_window)            
    #             self.P = 3*np.log10(OR) + 2*np.log10(LDI)  

    #         except ValueError: 
    #             windowed_bandEnergy = 0
    #             self.P = 0                
    #         self.prominence[n] = self.P
        
                        
    #     print(self.prominence)
                    
                    
    def _impulseParameters(self):
        time_event = 200/1000
        window_width = time_event * self.samplingRate        

        num_channels = 1 if self.bandEnergy.ndim == 2 else self.bandEnergy.shape[0]

        self.prominence = np.empty((num_channels, len(self.centralFrequencies)))

        for channel in range(num_channels):
            if self.bandEnergy.ndim == 2:
                bandEnergySF = self.bandEnergy
            else:
                bandEnergySF = self.bandEnergy[channel, :, :]

            for n in range(len(self.centralFrequencies)):
                bandEnergySFFreq = bandEnergySF[n, :]

                std_signal = np.std(bandEnergySFFreq)
                min_prominence = 5 * std_signal
                peaks, _ = signal.find_peaks(bandEnergySFFreq, prominence=min_prominence)

                max_peak_value = np.max(bandEnergySFFreq[peaks])
                max_peak_idx = []

                for m in peaks:
                    if bandEnergySFFreq[m] == max_peak_value:
                        max_peak_idx = m
                windowed_bandEnergy = bandEnergySFFreq[int(max_peak_idx - window_width/2):int(max_peak_idx + window_width/2)]
                nps_windowed_bandEnergy = 20 * np.log10(np.abs(windowed_bandEnergy/2e-5))

                try:
                    mean_window = np.mean(nps_windowed_bandEnergy)
                    max_window = np.max(nps_windowed_bandEnergy)
                    OR = (max_window - mean_window) / (15 * time_event)
                    LDI = (max_window - mean_window)
                    P = 3 * np.log10(OR) + 2 * np.log10(LDI)
                except ValueError:
                    windowed_bandEnergy = 0
                    P = 0

                self.prominence[channel, n] = P
        print(self.prominence)
                
       
            
    def _weightingFunction(self, plot):
        
        dlo_values = np.array([0.0276, 0.0139, 0.0093, 0.0072, 0.0053, 0.0072, 0.0159])
        #std_values = np.array([0.0072, 0.0036, 0.0030, 0.0066, 0.0032, 0.0064, 0.0083])
        freq_values = np.array([250, 500, 1000, 2000, 3000, 4000, 8000])



        x1 = np.linspace(100, 10000, 1981)
        y1 = np.interp(x1, freq_values, dlo_values)
        inv = -y1
        self.weighting = 3000*np.log10((10+inv)/np.max(10+inv))
        if plot:
            plt.subplot(1, 2, 1)        
            plt.semilogx(x1, y1, linestyle='dashed', label='Interpolated')
            plt.semilogx(freq_values, dlo_values, 'o', markerfacecolor='orange', markersize=8, label='Experimental')
            
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('Just Noticeable Difference - JND')
            plt.xticks(freq_values, freq_values)
            plt.grid(True, which='both')
            plt.legend()
            
            plt.subplot(1, 2, 2)
     
            plt.semilogx(x1, self.weighting)
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('Weighting [dBFS]')
            plt.xticks(freq_values, freq_values)
            plt.grid(True, which='both')
            
            plt.show()
        
       