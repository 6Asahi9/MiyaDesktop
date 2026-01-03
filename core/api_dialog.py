from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTextEdit,
    QPushButton, QLabel
)
from core.avatar_toggle import load_settings, save_settings

class ApiDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("API Key")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout(self)
        label = QLabel("Paste your API key below:")
        layout.addWidget(label)

        self.api_text = QTextEdit()
        layout.addWidget(self.api_text)

        ok_btn = QPushButton("confirm")  
        ok_btn.clicked.connect(self.save_and_close)
        layout.addWidget(ok_btn)

        self.load_existing_key()

    def load_existing_key(self):
        settings = load_settings()
        self.api_text.setPlainText(settings.get("api_key", ""))

    def save_and_close(self):
        api_key = self.api_text.toPlainText().strip()

        settings = load_settings()
        settings["api_key"] = api_key
        save_settings(settings)

        self.accept()
