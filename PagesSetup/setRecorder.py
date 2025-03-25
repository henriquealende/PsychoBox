from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
import sounddevice as sd

class DeviceSelectionDialog(QDialog):
    def __init__(self, device_type, parent=None):
        super(DeviceSelectionDialog, self).__init__(parent)
        self.setWindowTitle(f"Selecionar Dispositivo de {device_type}")
        self.device_type = device_type

        # Layout da janela
        layout = QVBoxLayout()

        # Label para instruções
        label = QLabel(f"Selecione um dispositivo de {device_type}:")
        layout.addWidget(label)

        # Lista para exibir dispositivos
        self.device_list = QListWidget()
        self.populate_device_list()
        layout.addWidget(self.device_list)

        # Conectar ao clique na lista
        self.device_list.itemClicked.connect(self.device_selected)

        # Configurar layout da janela
        self.setLayout(layout)

    def populate_device_list(self):
        """Popula a lista com dispositivos de entrada ou saída"""
        devices = sd.query_devices()
        if self.device_type == 'Gravação':
            device_info = [(i, dev['name']) for i, dev in enumerate(devices) if dev['max_input_channels'] > 0]
        elif self.device_type == 'Reprodução':
            device_info = [(i, dev['name']) for i, dev in enumerate(devices) if dev['max_output_channels'] > 0]

        # Adiciona à lista exibida o número e o nome do dispositivo
        for i, name in device_info:
            item_text = f"[{i}] {name}"  # Formato: [Número] Nome
            item = QListWidgetItem(item_text)
            item.device_index = i  # Armazenando o índice do dispositivo
            self.device_list.addItem(item)

    def device_selected(self, item):
        """Ação quando um dispositivo é selecionado"""
        device_index = item.device_index  # Pega o índice do dispositivo
        devices = sd.query_devices()
        selected_device = devices[device_index]['name']  # Pega o nome do dispositivo pelo índice

        if self.device_type == 'Gravação':
            sd.default.device[0] = device_index
            print(f"Microfone Selecionado: {selected_device}")
        elif self.device_type == 'Reprodução':
            sd.default.device[1] = device_index
            print(f"Alto-falante Selecionado: {selected_device}")
        
        self.accept()  # Fechar a janela ao selecionar
