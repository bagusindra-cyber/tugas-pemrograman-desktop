from database import get_connection
from security import hash_password

AKUN = [
    ("Ketua Umum / Admin", "admin", "Admin123!", "ADMIN"), 
    ("Pengurus Inventaris", "staff", "Staff123!", "STAFF"), 
    ("Anggota Himpunan", "anggota", "Anggota123!", "ANGGOTA")
]

with get_connection() as conn:
    for nama, username, password, role in AKUN:
        rr = conn.execute("SELECT id FROM roles WHERE nama=?", (role,)).fetchone()
        if rr:
            ada = conn.execute("SELECT id FROM users WHERE username=?", (username,)).fetchone()
            if not ada:
                conn.execute("INSERT INTO users(role_id, nama, username, password_hash) VALUES(?,?,?,?)", 
                             (rr["id"], nama, username, hash_password(password)))
print("Data user berhasil di-seed!")
