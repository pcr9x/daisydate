from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QPixmap
from assets.daisydate_ui import Ui_MainWindow
from datetime import datetime
from PySide6.QtCore import QTimer, QUrl, QPoint


import sys
from PySide6.QtWidgets import QApplication
from pages.auth_page import AuthPage
from pages.suggested_page import SuggestedPage
from pages.discover_page import DiscoverPage
from pages.chat_page import ChatPage
from pages.account_page import AccountPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthPage()
    suggested_page = SuggestedPage(window)
    discover_page = DiscoverPage(window)
    chat_page = ChatPage(window)
    account_page = AccountPage(window)
    window.show()

    sys.exit(app.exec())
