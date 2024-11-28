import numpy as np
import wave
import sounddevice as sd

from PagesSetup.mainSettings import MainSettings
from PagesSetup.setRecorder import DeviceSelectionDialog

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (QFileDialog, QVBoxLayout, QWidget)


class UI_Buttons_Recorder():
    def __init__(self):
        super(UI_Buttons_Recorder, self).__init__()
    
    def initialParameters(self):
        self.is_recording = False
        self.is_playing = False
        self.audio_data = []
        self.stream = None
        self.nChannels = 0

    def toggle_recording(self):
        """Inicia ou para a gravação"""
        if self.ui.recordingButton_2.isChecked():
            indata = []
            samplerate = float(self.ui.samplingRate_Combo.currentText())
            # channels = self.INSERIR_CHANNES
            self.audio_data = []
            def callback(indata, status):
                """Função chamada automaticamente para captar áudio"""
                if status:
                    print(status)
                self.audio_data.append(indata[:, 0].copy())
            # Armazena os dados de áudio capturados

            self.stream = sd.InputStream(samplerate=samplerate, channels=1, callback=callback)
            self.audio_data.append(indata.copy())
            self.stream.start()
            self.is_recording = True
        else:
            if self.stream:
                self.stream.stop()
                self.stream.close()
                self.is_recording = False



    def save_audio(self):
        """Salva o áudio gravado em um arquivo WAV"""
        samplerate = float(self.ui.samplingRate_Combo.currentText())
        if not self.audio_data:
            return
        # Converte a lista de áudio para um array numpy 1D
        audio_array = np.concatenate(self.audio_data, axis=0)
        audio_array = (audio_array * 32767).astype(np.int16)  # Converte para int16 para o formato WAV

        # Salva o áudio no arquivo
        saveAdress = QFileDialog.getSaveFileName(self, 'Save File','', 'WAV files (*.wav)')
        savePathname = str(saveAdress[0])
        with wave.open(savePathname, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 2 bytes (16 bits)
            wf.setframerate(samplerate)
            wf.writeframes(audio_array.tobytes())

    def play_audio(self):
        play_instace = UI_Buttons_Recorder()
        play_instace.__init__()
        samplerate = float(self.ui.samplingRate_Combo.currentText())
        """Reproduz o áudio gravado"""
        if not self.is_playing and self.audio_data:
            self.is_playing = True
            self.play_stream = sd.OutputStream(samplerate, channels=1)
            self.play_stream.start()
            self.audio_to_play = np.concatenate(self.audio_data, axis=0)
            self.audio_to_play = self.audio_to_play.astype(np.float32)
            self.play_stream.write(self.audio_to_play)
            self.ui.pauseButton_2.setEnabled(True)
            self.ui.stopButton_2.setEnabled(True)
            

    def pause_audio(self):
        """Pausa a reprodução do áudio"""
        if self.is_playing:
            self.play_stream.abort()
            self.is_playing = False

    def stop_audio(self):
        """Para a reprodução do áudio"""
        if self.is_playing:
            self.play_stream.stop()
            self.is_playing = False

    def audio_callback(self, indata, frames, time, status):
        """Função de callback para capturar o áudio"""
        if status:
            print(status)
        # Adiciona o áudio gravado à lista de dados
        self.audio_data.append(indata.copy())

    def update_plot(self):
        """Atualiza o gráfico de áudio em tempo real"""
        if self.is_recording and self.audio_data:
            current_data = np.concatenate(self.audio_data, axis=0).flatten()
            if len(current_data) > len(self.plot_data):
                current_data = current_data[-len(self.plot_data):]
            self.plot_data = np.roll(self.plot_data, -len(current_data))
            self.plot_data[-len(current_data):] = current_data
            self.curve.setData(self.plot_data)

    def closeEvent(self, event):
        """Para o stream de áudio quando a janela é fechada"""
        if self.stream:
            self.stream.stop()
            self.stream.close()
        event.accept()
        
    def setMicrophone(self, channel):
        microfone_channel = []
        if channel == 1:
            microfone_channel = self.ui.setMicrophone_1
        elif channel == 2:
            microfone_channel = self.ui.setMicrophone_2
        if microfone_channel.isChecked():
            dialog = DeviceSelectionDialog("Gravação", self)
            dialog.exec_()
            self.nChannels = self.nChannels + 1
        else:
            self.nChannels = self.nChannels - 1

        if self.nChannels > 0:
            self.ui.recordingButton_2.setEnabled(True)
        else:
            self.ui.recordingButton_2.setEnabled(False)
            
    def setSource(self):
        if self.ui.setSource_1.isChecked():
            dialog = DeviceSelectionDialog("Reprodução", self)
            dialog.exec_()
            if self.ui.recordingButton_2.isEnabled():
                self.ui.playButton_2.setEnabled(True)
        else:
            self.ui.playButton_2.setEnabled(False)

            
            
        
        
        

        
