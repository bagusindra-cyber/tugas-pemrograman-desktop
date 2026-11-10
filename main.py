import sys
import sqlite3
from PySide6.QtWidgets import QApplication
from login_form import LoginForm
from main_window import MainWindow
from database import get_connection

def init_db():
    try:
        with get_connection() as conn:
            with open('schema.sql', 'r') as f:
                conn.executescript(f.read())
            with open('seed.sql', 'r') as f:
                conn.executescript(f.read())
    except Exception as e:
        print("Sistem mendeteksi database sudah ada atau terinisialisasi.")

def main():
    app = QApplication(sys.argv)
    
    # 1. Jalankan inisialisasi tabel dasar
    init_db()
    
    # 2. Jalankan pembuatan akun (akan skip otomatis jika sudah ada)
    try:
        import seed_users
    except Exception as e:
        pass
        
    windows = {}
    
    def setelah_login(user):
        windows["utama"] = MainWindow(user)
        windows["utama"].show()
        windows["login"].close()
        
    windows["login"] = LoginForm(setelah_login)
    windows["login"].show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
