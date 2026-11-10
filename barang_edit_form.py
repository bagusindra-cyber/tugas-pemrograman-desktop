from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QMessageBox
from repository import ambil_barang, tambah_barang, simpan_perubahan_barang, ambil_kategori

class BarangEditForm(QDialog):
    def __init__(self, id_barang=None, parent=None):
        super().__init__(parent)
        self.id_barang = id_barang
        self.setWindowTitle("Edit Barang" if id_barang else "Tambah Barang")
        self.resize(350, 200)
        
        self.kode = QLineEdit()
        self.nama = QLineEdit()
        self.kondisi = QComboBox()
        self.kondisi.addItems(["BAIK", "RUSAK", "HILANG"])
        
        self.kategori = QComboBox()
        self.kategori_map = {}
        
        for k in ambil_kategori():
            self.kategori.addItem(k["nama_kategori"], k["id"])
            self.kategori_map[k["id"]] = self.kategori.count() - 1
            
        form = QFormLayout(self)
        form.addRow("Kategori", self.kategori)
        form.addRow("Kode Barang", self.kode)
        form.addRow("Nama Barang", self.nama)
        form.addRow("Kondisi", self.kondisi)
        
        simpan = QPushButton("Simpan Data")
        batal = QPushButton("Batal")
        baris = QHBoxLayout()
        baris.addWidget(simpan)
        baris.addWidget(batal)
        form.addRow(baris)
        
        simpan.clicked.connect(self.simpan)
        batal.clicked.connect(self.reject)
        
        if id_barang: 
            self.muat_data()
            
    def muat_data(self):
        row = ambil_barang(self.id_barang)
        if not row:
            QMessageBox.warning(self, "Info", "Data tidak ditemukan.")
            self.reject()
            return
        self.kode.setText(row["kode_barang"])
        self.nama.setText(row["nama_barang"])
        self.kondisi.setCurrentText(row["kondisi"])
        idx = self.kategori_map.get(row["kategori_id"], 0)
        self.kategori.setCurrentIndex(idx)
        
    def simpan(self):
        kat_id = self.kategori.currentData()
        kd = self.kode.text().strip()
        nm = self.nama.text().strip()
        kon = self.kondisi.currentText()
        
        if not kd or not nm:
            QMessageBox.warning(self, "Validasi", "Kode dan Nama Barang wajib diisi.")
            return
            
        try:
            if self.id_barang:
                simpan_perubahan_barang(self.id_barang, kat_id, kd, nm, kon)
            else:
                tambah_barang(kat_id, kd, nm, kon)
        except Exception as exc:
            QMessageBox.critical(self, "Gagal", str(exc))
            return
            
        self.accept()
