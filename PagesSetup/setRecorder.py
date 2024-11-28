from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QVBoxLayout, QLabel, QListWidget
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
            device_names = [dev['name'] for dev in devices if dev['max_input_channels'] > 0]
        elif self.device_type == 'Reprodução':
            device_names = [dev['name'] for dev in devices if dev['max_output_channels'] > 0]

        self.device_list.addItems(device_names)

    def device_selected(self, item):
        """Ação quando um dispositivo é selecionado"""
        selected_device = item.text()
        if self.device_type == 'Gravação':
            device_info = sd.query_devices(selected_device, 'input')
            sd.default.device[0] = device_info['name']
            print(f"Microfone Selecionado: {device_info['name']}")
        elif self.device_type == 'Reprodução':
            device_info = sd.query_devices(selected_device, 'output')
            sd.default.device[1] = device_info['name']
            print(f"Alto-falante Selecionado: {device_info['name']}")
        self.accept()  # Fechar a janela ao selecionar
