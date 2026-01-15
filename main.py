import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from ui.main_window import MainWindow
from core.path import ASSETS_PATH


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(ASSETS_PATH / "miya.ico")))

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
