# SIMA - Sistem Inventaris dan Manajemen Aset Organisasi

Aplikasi ini dibangun menggunakan Python, PySide6, dan SQLite sebagai pemenuhan Tugas Praktikum P11 Pemrograman Desktop.
Cocok untuk digunakan mengelola data barang dan peminjaman alat di organisasi.

## Cara Menjalankan

1. Pastikan Anda memiliki Python yang sudah terpasang.
2. Buka Terminal/Command Prompt di folder ini.
3. Install PySide6 dengan perintah:
   ```bash
   pip install PySide6
   ```
4. Jalankan aplikasi utama:
   ```bash
   python main.py
   ```
   *(Database `inventaris.db` beserta tabel dan data dummy akan terbuat secara otomatis saat program dijalankan untuk pertama kalinya).*

## Akun Login Dummy yang Tersedia:
- **Admin**: `admin` / Password: `Admin123!`
- **Staff (Pengurus)**: `staff` / Password: `Staff123!`
- **Anggota (Biasa)**: `anggota` / Password: `Anggota123!`
