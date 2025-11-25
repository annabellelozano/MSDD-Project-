import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt

'''
General Notes:

'''

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Login")
        self.setFixedSize(300, 200)
        self.initUI()

    def initUI(self):
        # Labels
        self.label_user = QLabel("Username:")
        self.label_pass = QLabel("Password:")

        # Input fields
        self.user_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.user_input)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        # Very basic check
        if username == "admin" and password == "1234":
            self.open_menu()
        if username == "justin" and password == "5678":
            self.open_menu()
        if username == "annabelle" and password == "2468":
            self.open_menu()
        else:
            QMessageBox.warning(self, "Error", "Incorrect username or password.")

    def open_menu(self):
        self.menu = MenuWindow()
        self.menu.show()
        self.close()


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Market Investment Fantasy League - Main Menu")
        self.setFixedSize(600, 600)
        self.initUI()

    def initUI(self):
        title = QLabel("Main Menu")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        trade_btn = QPushButton("Trade") #takes you to another screen that says pick a stock to trade, then "input how many you want to trade"
        miniGame_btn = QPushButton("Mini Games") #takes you to another screen that has 1 mini game, multiple choice game
        stockInfo_btn = QPushButton("Stock Info") #take you to a table of "current stocks" but just make up values
        settings_btn = QPushButton("Settings") #takes you to a settings page, does nothing
        quit_btn = QPushButton("Quit") #already does what its supossed to do
        quit_btn.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(trade_btn)
        layout.addWidget(miniGame_btn)
        layout.addWidget(stockInfo_btn)
        layout.addWidget(settings_btn)
        layout.addWidget(quit_btn)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
