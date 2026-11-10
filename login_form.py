from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from repository_auth import autentikasi

class LoginForm(QWidget):
    def __init__(self, on_login):
        super().__init__()
        self.on_login = on_login
        self.setWindowTitle("Login SIMA - Sistem Inventaris")
        self.resize(300, 150)
        
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        tombol = QPushButton("Login Aplikasi")
        
        form = QFormLayout()
        form.addRow("Username", self.username)
        form.addRow("Password", self.password)
        
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(tombol)
        
        tombol.clicked.connect(self.proses_login)
        
    def proses_login(self):
        user = autentikasi(self.username.text(), self.password.text())
        if not user:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah.")
            return
        self.on_login(user)
