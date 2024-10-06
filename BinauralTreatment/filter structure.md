# Filter struct to equalize playback systems

## About the filename of the headphone equalization:
###	  Saved in .mat, binary format. Imported as a lib inside the Python
###	  Name structure: eq_hats_audioInterface_headpone.mat
	
# Contents of the file:
## The data is saved as a dictionary with the follow structure:

dictData = {"hcorrLeftMF": hcorrLeftMF, # equalization of the left channel 
            "hcorrRightMF": hcorrRightMF, # equalization of the righr channeçl
            "samplingRate": samplingRate, # sampling frequency of the filter
            "freqRange": [lowerFreq, higherFreq] # freq range: a bandpass is applied to avoid high gain in the filter
            }

## About the filename of the HRIR to be applied in mic signals:
### Also saved in .mat, binary format and imported in Python
# Contents of the file:
## The data is saved as a dictionary with the follow structure:

dictData = {"hrirLeft": hcorrLeftMF, # head related impulse response of the left ear 
            "hrirRight": hcorrRightMF, # head related impulse response of the right ear 
            "samplingRate": samplingRate, # sampling frequency of the impulse response
            "freqRange": [lowerFreq, higherFreq] # freq range: a bandpass is applied to the hrir
            }