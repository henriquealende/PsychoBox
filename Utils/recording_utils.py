import numpy as np

class Recording_Utils:
    @staticmethod
    def update_plot(recorder_instance):
        """Atualiza o gráfico com os dados da instância do recorder"""
        if recorder_instance.is_recording and recorder_instance.audio_data:
            # Concatena todos os chunks de áudio
            current_data = np.concatenate(recorder_instance.audio_data, axis=0).flatten()
            
            # Mantém apenas os últimos pontos do buffer
            if len(current_data) > len(recorder_instance.plot_data):
                current_data = current_data[-len(recorder_instance.plot_data):]
            
            # Atualiza a curva do gráfico
            recorder_instance.curve.setData(current_data)