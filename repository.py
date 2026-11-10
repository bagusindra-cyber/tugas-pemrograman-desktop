from database import get_connection

def cari_barang(kata_kunci=""):
    pola = f"%{kata_kunci.strip()}%"
    with get_connection() as conn:
        return conn.execute(
            '''SELECT b.id, b.kode_barang, b.nama_barang, k.nama_kategori, b.kondisi 
               FROM barang b JOIN kategori k ON b.kategori_id = k.id 
               WHERE b.aktif=1 AND (b.nama_barang LIKE ? OR b.kode_barang LIKE ?) 
               ORDER BY b.nama_barang''', 
            (pola, pola)
        ).fetchall()

def ambil_barang(id_barang):
    with get_connection() as conn:
        return conn.execute("SELECT * FROM barang WHERE id=?", (id_barang,)).fetchone()

def tambah_barang(kategori_id, kode, nama, kondisi):
    if not nama.strip() or not kode.strip(): raise ValueError("Kode dan Nama wajib diisi.")
    with get_connection() as conn:
        conn.execute("INSERT INTO barang(kategori_id, kode_barang, nama_barang, kondisi) VALUES(?,?,?,?)", 
                     (kategori_id, kode.strip(), nama.strip(), kondisi))

def simpan_perubahan_barang(id_barang, kategori_id, kode, nama, kondisi):
    if not nama.strip() or not kode.strip(): raise ValueError("Kode dan Nama wajib diisi.")
    with get_connection() as conn:
        conn.execute("UPDATE barang SET kategori_id=?, kode_barang=?, nama_barang=?, kondisi=? WHERE id=? AND aktif=1", 
                     (kategori_id, kode.strip(), nama.strip(), kondisi, id_barang))

def nonaktifkan_barang(id_barang):
    with get_connection() as conn:
        conn.execute("UPDATE barang SET aktif=0 WHERE id=? AND aktif=1", (id_barang,))

def ambil_kategori():
    with get_connection() as conn:
        return conn.execute("SELECT id, nama_kategori FROM kategori ORDER BY nama_kategori").fetchall()
