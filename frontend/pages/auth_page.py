from PySide6.QtWidgets import QMainWindow
from assets.daisydate_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from datetime import datetime


class AuthPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.photo_edit_mapping = {
            self.ui.photo1: self.ui.editPhoto1,
            self.ui.photo2: self.ui.editPhoto2,
            self.ui.photo3: self.ui.editPhoto3,
            self.ui.photo4: self.ui.editPhoto4,
            self.ui.photo5: self.ui.editPhoto5,
            self.ui.photo6: self.ui.editPhoto6,
        }
        self.setup_signals()
        self.hide_element()

    def setup_signals(self):
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

    def show_account_page(self):
        self.ui.stackedWidget.setCurrentIndex(12)

    def show_edit_profile_page(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def hide_element(self):
        self.ui.label_signin_error.hide()
        self.ui.label_signup_error.hide()
        self.ui.label_age_error.hide()
        self.ui.label_mySchool.hide()

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
