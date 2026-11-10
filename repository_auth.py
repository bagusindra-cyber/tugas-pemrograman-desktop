from database import get_connection
from security import verify_password

def autentikasi(username, password):
    with get_connection() as conn:
        row = conn.execute(
            '''SELECT u.id, u.nama, u.username, u.password_hash, r.nama AS role 
               FROM users u JOIN roles r ON r.id=u.role_id 
               WHERE u.username=? AND u.aktif=1''', 
            (username.strip(),)
        ).fetchone()
    
    if row and verify_password(password, row["password_hash"]):
        return {"id": row["id"], "nama": row["nama"], "username": row["username"], "role": row["role"]}
    return None
