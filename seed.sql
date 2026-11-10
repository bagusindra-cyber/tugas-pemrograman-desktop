INSERT OR IGNORE INTO roles (nama) VALUES ('ADMIN'), ('STAFF'), ('ANGGOTA');
INSERT OR IGNORE INTO kategori (nama_kategori) VALUES ('Elektronik'), ('ATK'), ('Dokumentasi'), ('Ruangan');
INSERT OR IGNORE INTO barang (kategori_id, kode_barang, nama_barang, kondisi, aktif) 
VALUES 
(1, 'ELK-001', 'Proyektor Epson EPS-X', 'BAIK', 1), 
(3, 'DKM-001', 'Kamera Canon EOS 60D', 'BAIK', 1),
(1, 'ELK-002', 'Sound System Portable', 'BAIK', 1),
(2, 'ATK-001', 'Papan Tulis Whiteboard', 'BAIK', 1);
