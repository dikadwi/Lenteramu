from app import app, db
from models import User


def reset_default_passwords():
    with app.app_context():
        # Default passwords for different roles
        default_passwords = {
            'siswa': 'siswa123',
            'guru': 'guru123',
            'admin': 'admin123'
        }

        try:
            # Get all users
            users = User.query.all()

            for user in users:
                # Set default password based on role
                default_pwd = default_passwords.get(user.role, 'password123')
                user.set_password(default_pwd)
                print(
                    f"Reset password for user: {user.username} (role: {user.role})")

            # Save changes
            db.session.commit()
            print("\nSuccessfully reset all passwords!")
            print("\nDefault passwords:")
            print("Siswa: siswa123")
            print("Guru: guru123")
            print("Admin: admin123")

        except Exception as e:
            db.session.rollback()
            print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    reset_default_passwords()
