class SuggestedPage:
    def __init__(self, main_ui):
        self.main_ui = main_ui
        self.setup_signals()

    def setup_signals(self):
        self.main_ui.ui.btnDiscover.clicked.connect(self.main_ui.show_discover_page)
        self.main_ui.ui.btnChat.clicked.connect(self.main_ui.show_chat_page)
        self.main_ui.ui.btnAccount.clicked.connect(self.main_ui.show_account_page)
        self.main_ui.ui.btnPreferences.clicked.connect(
            self.main_ui.show_preferences_page
        )

        self.main_ui.ui.btnBackPref.clicked.connect(self.main_ui.show_suggested_page)
