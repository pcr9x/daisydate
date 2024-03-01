import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtGui import QPixmap
from assets.daisydate_ui import Ui_MainWindow
from datetime import datetime
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import Qt, QObject, Signal

class MainUI(QMainWindow):
    messageReceived = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.currentImgProfile = [
            self.ui.editPhoto1,
            self.ui.editPhoto2,
            self.ui.editPhoto3,
            self.ui.editPhoto4,
            self.ui.editPhoto5,
            self.ui.editPhoto6,
        ]

        self.currentImgIndex = 0
        self.setup_signals()
        self.hide_element()
        self.photo_edit_mapping = {
            self.ui.photo1: self.ui.editPhoto1,
            self.ui.photo2: self.ui.editPhoto2,
            self.ui.photo3: self.ui.editPhoto3,
            self.ui.photo4: self.ui.editPhoto4,
            self.ui.photo5: self.ui.editPhoto5,
            self.ui.photo6: self.ui.editPhoto6,
        }
        self.setup_websocket_connection()

    def setup_signals(self):
        """Connect signals to slots."""
        self.ui.btnSignin.clicked.connect(self.show_signin_page)
        self.ui.btnBackSignin.clicked.connect(self.show_main_page)
        self.ui.btnSignup.clicked.connect(self.show_signup_page)
        self.ui.btnBackSignup.clicked.connect(self.show_main_page)
        self.ui.btnSign_in.clicked.connect(self.show_suggested_page)
        self.ui.btnGetStarted.clicked.connect(self.show_signup_birthday_page)
        self.ui.btnBackBD.clicked.connect(self.show_signup_page)
        self.ui.btnNext.clicked.connect(self.show_signup_info_page)
        self.ui.btnBackInfo.clicked.connect(self.show_signup_birthday_page)
        self.ui.btnAlmostDone.clicked.connect(self.show_signup_photo_page)
        self.ui.btnBackPhoto.clicked.connect(self.show_signup_info_page)
        self.ui.btnWelcome.clicked.connect(self.show_suggested_page)

        for photo_widget in [
            self.ui.photo1,
            self.ui.photo2,
            self.ui.photo3,
            self.ui.photo4,
            self.ui.photo5,
            self.ui.photo6,
        ]:
            photo_widget.mousePressEvent = (
                lambda event, widget=photo_widget: self.openFileExplorerSignup(widget)
            )

        """Suggested Page"""
        self.ui.btnDiscover.clicked.connect(self.show_discover_page)
        self.ui.btnChat.clicked.connect(self.show_chat_page)
        self.ui.btnAccount.clicked.connect(self.show_account_page)
        self.ui.btnPreferences.clicked.connect(self.show_preferences_page)

        """Preferences Page"""
        self.ui.btnBackPref.clicked.connect(self.show_suggested_page)

        """Discover Page"""
        self.ui.btnSuggested_2.clicked.connect(self.show_suggested_page)
        self.ui.btnChat_2.clicked.connect(self.show_chat_page)
        self.ui.btnAccount_2.clicked.connect(self.show_account_page)
        self.ui.btnSearch.clicked.connect(self.show_search_page)

        """Search Page"""
        self.ui.btnCancel.clicked.connect(self.show_discover_page)
        self.ui.btnApply.clicked.connect(self.show_discover_page)

        """Chat Page"""
        self.ui.btnSuggested_3.clicked.connect(self.show_suggested_page)
        self.ui.btnDiscover_3.clicked.connect(self.show_discover_page)
        self.ui.btnAccount_3.clicked.connect(self.show_account_page)
        self.ui.chatWidget.mousePressEvent = self.show_user_chat_page()
        
        """User Chat Page"""
        self.ui.btnBackChat.clicked.connect(self.show_chat_page)
        self.ui.btnSend.clicked.connect(self.send_chat_message)

        """Account Page"""
        self.ui.btnSuggested_4.clicked.connect(self.show_suggested_page)
        self.ui.btnDiscover_4.clicked.connect(self.show_discover_page)
        self.ui.btnChat_4.clicked.connect(self.show_chat_page)
        self.ui.btnEdit.clicked.connect(self.show_edit_profile_page)
        self.ui.btnBkPhoto.clicked.connect(lambda: self.setImgProfile(0))
        self.ui.btnFwPhoto.clicked.connect(lambda: self.setImgProfile(1))

        """Edit Profile Page"""
        self.ui.btnDone.clicked.connect(self.show_account_page)
        for edit_photo_widget in self.currentImgProfile:
            edit_photo_widget.mousePressEvent = (
                lambda event, widget=edit_photo_widget: self.openFileExplorer(widget)
            )
        if self.ui.comboBoxMySchool.currentText() == "School":
            self.ui.label_mySchool.hide()
        else:
            self.ui.label_mySchool.setText(self.ui.comboBoxMySchool.currentText())

        # Connect messageReceived signal to update_chat_ui slot
        self.messageReceived.connect(self.update_chat_ui)

    def setup_websocket_connection(self):
        self.socket = QWebSocket()
        self.socket.error.connect(self.handle_error)
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.textMessageReceived.connect(self.on_text_received)
        # Connect to the WebSocket server
        self.socket.open(QUrl("ws://127.0.0.1:8000/ws"))

    def send_chat_message(self):
        message = self.ui.lineEditChat.text()
        if message:
            self.socket.sendTextMessage(message)
            self.ui.lineEditChat.clear()

    def handle_error(self):
        print("WebSocket error occurred.")

    def on_connected(self):
        print("Connected to WebSocket server.")

    def on_disconnected(self):
        print("Disconnected from WebSocket server.")

    def on_text_received(self, message):
        print("Message received:", message)
        self.messageReceived.emit(message)

    def show_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_signin_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_signup_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_signup_birthday_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_signup_info_page(self):
        birthdate = self.ui.dateEdit.date()
        current_date = datetime.now().date()

        age = current_date.year - birthdate.year()
        if (current_date.month, current_date.day) < (
            birthdate.month(),
            birthdate.day(),
        ):
            age -= 1

        if age < 18:
            self.ui.label_age_error.show()
            return

        self.ui.label_myAge.setText(str(age))
        self.ui.stackedWidget.setCurrentIndex(4)

    def show_signup_photo_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def show_suggested_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def show_preferences_page(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def show_discover_page(self):
        self.ui.stackedWidget.setCurrentIndex(8)

    def show_search_page(self):
        self.ui.stackedWidget.setCurrentIndex(9)

    def show_chat_page(self):
        self.ui.stackedWidget.setCurrentIndex(10)

    def show_user_chat_page(self):
        self.ui.stackedWidget.setCurrentIndex(11)

    def show_account_page(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def show_edit_profile_page(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def hide_element(self):
        self.ui.label_signin_error.hide()
        self.ui.label_signup_error.hide()
        self.ui.label_age_error.hide()
        self.ui.label_mySchool.hide()

    def openFileExplorer(self, label):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )
        if fileName:
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.ui.userImage.setPixmap(self.ui.editPhoto1.pixmap())
            self.ui.userImage.setScaledContents(True)

    def openFileExplorerSignup(self, label):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )
        if fileName:
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap)
            label.setScaledContents(True)  # Scale pixmap to fit QLabel

            # Update the corresponding edit photo widget
            edit_photo_widget = self.photo_edit_mapping.get(label)
            if edit_photo_widget:
                edit_photo_widget.setPixmap(pixmap)
                edit_photo_widget.setScaledContents(True)
                self.ui.userImage.setPixmap(self.ui.editPhoto1.pixmap())
                self.ui.userImage.setScaledContents(True)

    def setImgProfile(self, command):
        if command == 0 and self.currentImgIndex > 0:
            self.currentImgIndex -= 1
        elif command == 1 and self.currentImgIndex < len(self.currentImgProfile) - 1:
            next_photo_pixmap = self.currentImgProfile[
                self.currentImgIndex + 1
            ].pixmap()
            if next_photo_pixmap is not None and not next_photo_pixmap.isNull():
                self.currentImgIndex += 1

        # Get the edit photo widget corresponding to the current index
        edit_photo_widget = self.currentImgProfile[self.currentImgIndex]

        # Set the pixmap of ui.userImage to the pixmap of the edit photo widget
        self.ui.userImage.setPixmap(edit_photo_widget.pixmap())
        self.ui.userImage.setScaledContents(True)

    def update_chat_ui(self, message):
        label = QLabel(message)
        self.ui.chatBoxLayOut.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()

    sys.exit(app.exec())
