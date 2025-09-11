# Database setup script untuk LENTERAMU
import subprocess
import sys
import os


def install_mysql_server():
    """Guide untuk instalasi MySQL Server"""
    print("=== PANDUAN INSTALASI MYSQL SERVER ===")
    print("1. Download MySQL Server dari: https://dev.mysql.com/downloads/mysql/")
    print("2. Install MySQL Server dengan username 'root' dan password kosong")
    print("3. Atau gunakan XAMPP/WAMP yang sudah include MySQL")
    print("4. Pastikan MySQL service berjalan di port 3306")
    print()


def create_database():
    """Create database lenteramu_db"""
    try:
        import pymysql

        # Connect to MySQL server
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            charset='utf8mb4'
        )

        cursor = connection.cursor()

        # Create database
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS lenteramu_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✓ Database 'lenteramu_db' created successfully!")

        # Show databases
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("Available databases:")
        for db in databases:
            print(f"  - {db[0]}")

        cursor.close()
        connection.close()

        return True

    except Exception as e:
        print(f"❌ Error creating database: {e}")
        print("Please make sure MySQL server is running and accessible")
        return False


def test_connection():
    """Test database connection"""
    try:
        import pymysql

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='lenteramu_db',
            charset='utf8mb4'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✓ Connected to MySQL version: {version[0]}")

        cursor.close()
        connection.close()

        return True

    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        return False


def main():
    print("=== LENTERAMU DATABASE SETUP ===")
    print()

    # Check if required packages are installed
    try:
        import pymysql
        print("✓ PyMySQL is installed")
    except ImportError:
        print("❌ PyMySQL not found. Installing...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "pymysql"])
        print("✓ PyMySQL installed successfully")

    print()

    # Guide for MySQL installation
    install_mysql_server()

    input("Press Enter after MySQL Server is installed and running...")

    # Create database
    print("Creating database...")
    if create_database():
        print()
        print("Testing connection...")
        if test_connection():
            print()
            print("✅ Database setup completed successfully!")
            print()
            print("Next steps:")
            print("1. Run: python init_db.py (to create tables and sample data)")
            print("2. Run: python app.py (to start the application)")
            print("3. Visit: http://localhost:5000")
        else:
            print("❌ Setup incomplete - connection test failed")
    else:
        print("❌ Setup failed - could not create database")


if __name__ == '__main__':
    main()
