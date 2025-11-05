from app import db
from models import User
from werkzeug.security import generate_password_hash

admin = User.query.filter_by(username='admin').first()
if admin:
    admin.password_hash = generate_password_hash(
        'bandung*Aa?', method='pbkdf2:sha256')
    db.session.commit()
    print("✅ Password admin berhasil diperbarui.")
else:
    print("❌ User admin tidak ditemukan.")
