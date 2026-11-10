from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from barang_list_form import BarangListForm

class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle(f"SIMA (Sistem Manajemen Aset) - {user['nama']}")
        self.resize(400, 200)
        
        pusat = QWidget()
        layout = QVBoxLayout(pusat)
        
        info = QLabel(f"Halo, {user['nama']}!\nRole Anda saat ini adalah: {user['role']}")
        layout.addWidget(info)
        
        btn = QPushButton("Buka Master Data Inventaris")
        layout.addWidget(btn)
        
        btn.clicked.connect(self.buka_inventaris)
        self.setCentralWidget(pusat)
        
    def buka_inventaris(self):
        self.form_inv = BarangListForm(self.user)
        self.form_inv.show()
