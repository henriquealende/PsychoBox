import numpy as np
import wave
import sounddevice as sd
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog, QVBoxLayout, QWidget
from Utils.recording_utils import Recording_Utils as utr
import pyqtgraph as pg
from PagesSetup.setRecorder import DeviceSelectionDialog


class UI_Buttons_Recorder():
    def __init__(self, main_window):  # Adicione este parâmetro
        super().__init__()
        self.main_window = main_window
        self.ui = main_window.ui  # Acesso à UI da MainWindow
    
    def initialParameters(self):
        self.is_recording = False
        self.is_playing = False
        self.audio_data = []
        self.stream = None
        self.nChannels = 0
        
        # Configuração do plot com as cores especificadas
        self.plot_widget = pg.PlotWidget(title="Audio Signal")
        
        # Estilo do gráfico
        self.plot_widget.setBackground('#757575')  # Cor de fundo
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        
        # Configuração da curva
        self.curve = self.plot_widget.plot(pen={'color': '#f16637', 'width': 2})  # Cor da linha
        
        # Configuração dos eixos
        styles = {'color': 'white', 'font-size': '10px'}
        self.plot_widget.setLabel('left', 'Amplitude', **styles)
        self.plot_widget.setLabel('bottom', 'Time', **styles)
        self.plot_widget.setYRange(-1, 1)
        
        self.plot_data = np.zeros(1024)

        # Layout do gráfico
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.ui.recordingFrame.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: utr.update_plot(self))

    def toggle_recording(self):
        if self.ui.recordingButton_2.isChecked():
            samplerate = float(self.ui.samplingRate_Combo.currentText())
            self.audio_data = []
            self.ui.playButton_2.setEnabled(False)  # Desabilita play durante gravação

            def callback(indata, frames, time, status):
                if status:
                    print(status)
                self.audio_data.append(indata[:, 0].copy())

            self.stream = sd.InputStream(
                samplerate=samplerate,
                channels=1,
                callback=callback
            )
            self.stream.start()
            self.is_recording = True
            self.timer.start(100)

        else:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.is_recording = False
                self.timer.stop()
                # Habilita o botão play SE houver áudio gravado
                if len(self.audio_data) > 0:
                    self.ui.playButton_2.setEnabled(True)
                    

    def save_audio(self):
        samplerate = float(self.ui.samplingRate_Combo.currentText())
        if not self.audio_data:
            return
            
        audio_array = np.concatenate(self.audio_data, axis=0)
        audio_array = (audio_array * 32767).astype(np.int16)

        saveAdress = QFileDialog.getSaveFileName(
            self.main_window,  # Usa main_window como parent
            'Save File',
            '', 
            'WAV files (*.wav)'
        )
        savePathname = str(saveAdress[0])
        with wave.open(savePathname, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes(audio_array.tobytes())

    def play_audio(self):
        samplerate = float(self.ui.samplingRate_Combo.currentText())
        if not self.is_playing and self.audio_data and len(self.audio_data) > 0:
            self.is_playing = True
            self.play_stream = sd.OutputStream(samplerate, channels=1)
            self.play_stream.start()
            self.audio_to_play = np.concatenate(self.audio_data, axis=0).astype(np.float32)
            self.play_stream.write(self.audio_to_play)
            self.ui.pauseButton_2.setEnabled(True)
            self.ui.stopButton_2.setEnabled(True)
        else:
            self.ui.playButton_2.setEnabled(False)

    def pause_audio(self):
        if self.is_playing:
            self.play_stream.abort()
            self.is_playing = False

    def stop_audio(self):
        if self.is_playing:
            self.play_stream.stop()
            self.is_playing = False

    def setMicrophone(self, channel):
        microfone_channel = self.ui.setMicrophone_1 if channel == 1 else self.ui.setMicrophone_2
        if microfone_channel.isChecked():
            dialog = DeviceSelectionDialog("Gravação", self)  # Usa main_window como parent
            dialog.exec()
            self.nChannels += 1
        else:
            self.nChannels -= 1

        self.ui.recordingButton_2.setEnabled(self.nChannels > 0)
            
    def setSource(self):
        if self.ui.setSource_1.isChecked():
            dialog = DeviceSelectionDialog("Reprodução", self)  # Usa main_window como parent
            dialog.exec()
            self.ui.playButton_2.setEnabled(self.ui.recordingButton_2.isEnabled())
        else:
            self.ui.playButton_2.setEnabled(False)

    def closeEvent(self, event):
        if self.stream:
            self.stream.stop()
            self.stream.close()
        event.accept()