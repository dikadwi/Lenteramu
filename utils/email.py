from flask_mail import Mail, Message
from flask import current_app

mail = Mail()


def send_verification_email(user_email, verification_token):
    """
    Mengirim email verifikasi ke pengguna
    """
    msg = Message('Verifikasi Akun Lenteramu',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user_email])

    verification_url = f"{current_app.config['BASE_URL']}/auth/verify/{verification_token}"

    msg.body = f'''Selamat datang di Lenteramu!

Untuk memverifikasi akun Anda, silakan klik link berikut:
{verification_url}

Link ini akan kadaluarsa dalam 24 jam.

Jika Anda tidak merasa mendaftar di Lenteramu, abaikan email ini.

Salam,
Tim Lenteramu
'''

    msg.html = f'''
    <h2>Selamat datang di Lenteramu!</h2>
    <p>Untuk memverifikasi akun Anda, silakan klik link berikut:</p>
    <p><a href="{verification_url}">Verifikasi Akun</a></p>
    <p>Link ini akan kadaluarsa dalam 24 jam.</p>
    <p>Jika Anda tidak merasa mendaftar di Lenteramu, abaikan email ini.</p>
    <br>
    <p>Salam,<br>Tim Lenteramu</p>
    '''

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def send_reset_password_email(user_email, reset_token):
    """
    Mengirim email reset password ke pengguna
    """
    msg = Message('Reset Password Lenteramu',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user_email])

    reset_url = f"{current_app.config['BASE_URL']}/auth/reset-password/{reset_token}"

    msg.body = f'''Anda telah meminta untuk mereset password Anda di Lenteramu.

Untuk mereset password Anda, silakan klik link berikut:
{reset_url}

Link ini akan kadaluarsa dalam 1 jam.

Jika Anda tidak meminta reset password, abaikan email ini.

Salam,
Tim Lenteramu
'''

    msg.html = f'''
    <h2>Reset Password Lenteramu</h2>
    <p>Anda telah meminta untuk mereset password Anda di Lenteramu.</p>
    <p>Untuk mereset password Anda, silakan klik link berikut:</p>
    <p><a href="{reset_url}">Reset Password</a></p>
    <p>Link ini akan kadaluarsa dalam 1 jam.</p>
    <p>Jika Anda tidak meminta reset password, abaikan email ini.</p>
    <br>
    <p>Salam,<br>Tim Lenteramu</p>
    '''

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
