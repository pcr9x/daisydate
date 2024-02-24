import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from assets.daisydate_ui import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())