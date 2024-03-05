class DiscoverPage:
    def __init__(self, main_ui):
        self.main_ui = main_ui
        self.setup_signals()

    def setup_signals(self):
        self.main_ui.ui.btnSuggested_2.clicked.connect(self.main_ui.show_suggested_page)
        self.main_ui.ui.btnChat_2.clicked.connect(self.main_ui.show_chat_page)
        self.main_ui.ui.btnAccount_2.clicked.connect(self.main_ui.show_account_page)
        self.main_ui.ui.btnSearch.clicked.connect(self.main_ui.show_search_page)

        self.main_ui.ui.btnCancel.clicked.connect(self.main_ui.show_discover_page)
        self.main_ui.ui.btnApply.clicked.connect(self.main_ui.show_discover_page)
