from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from repository import cari_barang, nonaktifkan_barang
from barang_edit_form import BarangEditForm

class BarangListForm(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Master Data Inventaris")
        self.resize(600, 400)
        
        self.cari = QLineEdit()
        self.cari.setPlaceholderText("Cari kode atau nama barang...")
        
        self.tabel = QTableWidget(0, 5)
        self.tabel.setHorizontalHeaderLabels(["ID", "Kode Barang", "Nama Barang", "Kategori", "Kondisi"])
        
        self.bt_tambah = QPushButton("Tambah Barang")
        self.bt_edit = QPushButton("Edit Barang")
        self.bt_hapus = QPushButton("Hapus (Soft Delete)")
        
        row = QHBoxLayout()
        for b in (self.bt_tambah, self.bt_edit, self.bt_hapus): 
            row.addWidget(b)
            
        layout = QVBoxLayout(self)
        layout.addWidget(self.cari)
        layout.addWidget(self.tabel)
        layout.addLayout(row)
        
        self.cari.textChanged.connect(self.muat_data)
        self.bt_tambah.clicked.connect(self.tambah)
        self.bt_edit.clicked.connect(self.edit)
        self.bt_hapus.clicked.connect(self.hapus)
        
        # Otorisasi Hak Akses
        if user["role"] not in ("ADMIN", "STAFF"):
            for b in (self.bt_tambah, self.bt_edit, self.bt_hapus): 
                b.setEnabled(False)
                
        self.muat_data()
        
    def muat_data(self):
        rows = cari_barang(self.cari.text())
        self.tabel.setRowCount(0)
        for row in rows:
            i = self.tabel.rowCount()
            self.tabel.insertRow(i)
            self.tabel.setItem(i, 0, QTableWidgetItem(str(row["id"])))
            self.tabel.setItem(i, 1, QTableWidgetItem(row["kode_barang"]))
            self.tabel.setItem(i, 2, QTableWidgetItem(row["nama_barang"]))
            self.tabel.setItem(i, 3, QTableWidgetItem(row["nama_kategori"]))
            self.tabel.setItem(i, 4, QTableWidgetItem(row["kondisi"]))
            
    def id_terpilih(self):
        i = self.tabel.currentRow()
        return int(self.tabel.item(i, 0).text()) if i >= 0 else None
        
    def tambah(self):
        dlg = BarangEditForm(parent=self)
        if dlg.exec(): 
            self.muat_data()
            
    def edit(self):
        id_b = self.id_terpilih()
        if id_b is None:
            QMessageBox.information(self, "Pilih data", "Klik salah satu baris barang dahulu.")
            return
        dlg = BarangEditForm(id_b, self)
        if dlg.exec(): 
            self.muat_data()
            
    def hapus(self):
        id_b = self.id_terpilih()
        if id_b is None:
            QMessageBox.information(self, "Pilih data", "Klik salah satu baris barang dahulu.")
            return
            
        jawaban = QMessageBox.question(self, "Konfirmasi Hapus", "Yakin ingin menonaktifkan barang ini dari sistem?")
        if jawaban != QMessageBox.Yes: 
            return
            
        try:
            nonaktifkan_barang(id_b)
            self.muat_data()
        except Exception as exc:
            QMessageBox.warning(self, "Gagal", str(exc))
