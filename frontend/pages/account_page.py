from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

class AccountPage:
    def __init__(self, main_ui):
        self.main_ui = main_ui
        self.currentImgProfile = [
            self.main_ui.ui.editPhoto1,
            self.main_ui.ui.editPhoto2,
            self.main_ui.ui.editPhoto3,
            self.main_ui.ui.editPhoto4,
            self.main_ui.ui.editPhoto5,
            self.main_ui.ui.editPhoto6,
        ]

        self.currentImgIndex = 0
        self.setup_signals()

    def setup_signals(self):
        self.main_ui.ui.btnSuggested_4.clicked.connect(self.main_ui.show_suggested_page)
        self.main_ui.ui.btnDiscover_4.clicked.connect(self.main_ui.show_discover_page)
        self.main_ui.ui.btnChat_4.clicked.connect(self.main_ui.show_chat_page)
        self.main_ui.ui.btnEdit.clicked.connect(self.main_ui.show_edit_profile_page)
        self.main_ui.ui.btnBkPhoto.clicked.connect(lambda: self.setImgProfile(0))
        self.main_ui.ui.btnFwPhoto.clicked.connect(lambda: self.setImgProfile(1))

        """Edit Profile Page"""
        self.main_ui.ui.btnDone.clicked.connect(
            lambda: (self.main_ui.show_account_page(), self.update_profile())
        )

        for edit_photo_widget in self.currentImgProfile:
            edit_photo_widget.mousePressEvent = (
                lambda event, widget=edit_photo_widget: self.openFileExplorer(widget)
            )
        self.main_ui.ui.label_mySchool.hide()

    def openFileExplorer(self, label):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            label.parent(),
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)",
            options=options,
        )
        if fileName:
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.main_ui.ui.userImage.setPixmap(self.main_ui.ui.editPhoto1.pixmap())
            self.main_ui.ui.userImage.setScaledContents(True)

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
        self.main_ui.ui.userImage.setPixmap(edit_photo_widget.pixmap())
        self.main_ui.ui.userImage.setScaledContents(True)

    def update_profile(self):
        if self.main_ui.ui.comboBoxMySchool.currentText() == "School":
            self.main_ui.ui.label_mySchool.hide()
        else:
            self.main_ui.ui.label_mySchool.show()
            self.main_ui.ui.label_mySchool.setText(
                self.main_ui.ui.comboBoxMySchool.currentText()
            )
