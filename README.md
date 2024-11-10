# PsychoBox
<p align = "center">
 <img width = "470" src = "/Resources/img/psychobox_logo.png">
</p>

## Introduction

Welcome to the PsychoBox Audio Analysis framework! PsychoBox is a comprehensive Python library crafted to facilitate manipulating, analyzing, and evaluating audio signals. With a focus on psychoacoustic metrics, this framework empowers users to delve into sound quality assessment and exploration effortlessly.

PsychoBox leverages [MosQiTo](https://github.com/Eomys/MoSQITo), a specialized library developed by Eomys for sound quality and psychoacoustic analysis, as one of its core dependencies. MosQiTo provides essential functionalities and algorithms that enable PsychoBox to perform precise and reliable evaluations in areas such as loudness, sharpness, roughness, and other psychoacoustic metrics. By integrating MosQiTo, PsychoBox brings advanced sound quality analysis to your fingertips with ease and flexibility.

## Features

- Signal Analysis: Seamlessly load audio files and generate insightful visualizations like waveforms and spectrograms.

- Advanced Filtering: Implement various filters including high-pass, low-pass, and band-pass to emphasize or attenuate specific frequency bands.

- Psychoacoustic Insights: Compute crucial psychoacoustic parameters such as loudness, masking thresholds, and perceptual audio quality scores.

- User-Friendly Interface: PsychoBox prioritizes user experience, making it accessible and intuitive even for those new to audio analysis.

## Documentation

Install Guide and Tutorials are available in the [Documentation](/Documentation). 
## Getting PsychoBox

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

PsychoBox is a Python framework designed to facilitate audio analysis with a focus on psychoacoustic metrics. Below are instructions on how to use the main functionalities of the framework. Make sure to follow the installation instructions provided in the `Documentation` folder before using PsychoBox.

### 1. Audio Filtering

1. **Launch PsychoBox** and navigate to the **Filters** section via the Menu.
2. **Import an audio file** (.wav) using the `import` button.
3. Once the audio is loaded, adjust the **frequency sliders** to apply filters to specific frequency bands.
4. Click `filter` to apply the filters and save the output file. The filtered audio will be saved as a .wav file.
5. You can review and manage all filtered and original audio files in the **audio bank**.

### 2. Audio Signal Analysis

1. Go to the **Psycho** section via the Menu and **import an audio file** (.wav).
2. After selecting the file, click `plot` to open the **plot configuration window**.
3. In this window, choose your desired **analysis type** from the `Metrics` ComboBox:
   - **Time Domain** to view the waveform.
   - **Frequency Domain** to view the spectrum (FFT will be applied automatically). You can select a linear or third-octave band display.
   - **Psychoacoustic Metrics** to apply metrics such as Loudness Zwicker, Loudness ECMA, Sharpness DIN, Roughness DW, and Roughness ECMA.
4. Export data as .csv and figures as .png for further analysis.

### 3. Contribute

We welcome contributions to help improve PsychoBox! Whether through suggestions, code contributions, or documentation, your support will help grow this tool for the psychoacoustic community.

### 4. Documentation

For more detailed guidance, please refer to the **Documentation** folder. This includes:
   - **Installation Guide**: A step-by-step guide for setting up PsychoBox.
   - **Application Tutorial**: Available in both English and Portuguese, covering in-depth usage instructions.

---

By following these steps, you’ll be able to explore the core functionalities of PsychoBox for your audio analysis needs. Enjoy!

## Contributing
We welcome contributions from the community! To report issues, propose enhancements, or contribute code, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

