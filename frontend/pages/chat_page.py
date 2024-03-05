from PySide6.QtWebSockets import QWebSocket
from PySide6.QtCore import QObject, Signal, QUrl, QPoint
from PySide6.QtWidgets import QLabel

class ChatPage(QObject):
    messageReceived = Signal(str)

    def __init__(self, main_ui):
        super().__init__()
        self.main_ui = main_ui
        self.setup_signals()

    def setup_signals(self):
        self.main_ui.ui.btnSuggested_3.clicked.connect(self.main_ui.show_suggested_page)
        self.main_ui.ui.btnDiscover_3.clicked.connect(self.main_ui.show_discover_page)
        self.main_ui.ui.btnAccount_3.clicked.connect(self.main_ui.show_account_page)
        self.main_ui.ui.chatWidget.mousePressEvent = self.show_user_chat_page

        """User Chat Page"""
        self.main_ui.ui.btnBackChat.clicked.connect(self.main_ui.show_chat_page)
        self.main_ui.ui.btnSend.clicked.connect(self.send_chat_message)

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

    def show_user_chat_page(self, event):
        local_pos = self.main_ui.ui.chatWidget.mapFromGlobal(event.globalPosition())
        mouse_point = QPoint(local_pos.x(), local_pos.y())

        if self.main_ui.ui.chatWidget.rect().contains(mouse_point):
            self.main_ui.ui.stackedWidget.setCurrentIndex(11)
            self.setup_websocket_connection()

    def handle_error(self):
        print("WebSocket error occurred.")

    def on_connected(self):
        print("Connected to WebSocket server.")

    def on_disconnected(self):
        print("Disconnected from WebSocket server.")

    def on_text_received(self, message):
        print("Message received:", message)
        self.messageReceived.emit(message)

    def update_chat_ui(self, message):
        label = QLabel(message)
        self.main_ui.ui.chatBoxLayOut.addWidget(label)
