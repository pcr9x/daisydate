import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from assets.daisydate_ui import Ui_MainWindow

# from assets import resources_rc


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_signals()
        self.hide_error_message()

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

        """User Chat Page"""
        self.ui.btnBackChat.clicked.connect(self.show_chat_page)

        """Account Page"""
        self.ui.btnSuggested_4.clicked.connect(self.show_suggested_page)
        self.ui.btnDiscover_4.clicked.connect(self.show_discover_page)
        self.ui.btnChat_4.clicked.connect(self.show_chat_page)
        self.ui.btnEdit.clicked.connect(self.show_edit_profile_page)

        """Edit Profile Page"""
        self.ui.btnDone.clicked.connect(self.show_account_page)

    def show_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def show_signin_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_signup_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_signup_birthday_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def show_signup_info_page(self):
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

    def hide_error_message(self):
        self.ui.label_signin_error.hide()
        self.ui.label_signup_error.hide()
        self.ui.label_age_error.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec())
